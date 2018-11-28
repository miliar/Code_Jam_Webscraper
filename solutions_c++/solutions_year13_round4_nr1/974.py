#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <stack>

using namespace std;

int main() {
        ifstream fin("A-small-attempt0.in");
        ofstream fout("A-small-attempt0.out");
        int T;
        fin >> T;
        for (int casenum = 1; casenum <= T; ++casenum) {
                int N, M;
                fin >> N >> M;
                int cost = 0;
                vector<pair<int,int>> vec;
                for (int i = 0; i < M; ++i) {
                        int o, e, p;
                        fin >> o >> e >> p;
                        int n = e - o;
                        cost += (n == 0 ? 0 : n * N - n * (n - 1) / 2) * p;
                        vec.push_back(make_pair(o, -p));
                        vec.push_back(make_pair(e, p));
                }
                sort(vec.begin(), vec.end());
                int n = 2 * M;
                stack<pair<int,int>> stk;
                int total = 0;
                for (int i = 0; i < n; ++i) {
                        if (vec[i].second < 0)
                                stk.push(make_pair(vec[i].first, -vec[i].second));
                        else {
                                int t = vec[i].second;
                                while (t > 0) {
                                        int num = stk.top().second;
                                        if (t >= num) {
                                                t -= num;
                                                int k = vec[i].first - stk.top().first;
                                                total += (k == 0 ? 0 : k * N - k * (k - 1) / 2) * num;
                                                stk.pop();
                                        } else {
                                                int j = stk.top().first;
                                                stk.pop();
                                                int k = vec[i].first - j;
                                                total += (k == 0 ? 0 : k * N - k * (k - 1) / 2) * t;
                                                num -= t;
                                                stk.push(make_pair(j, num));
                                                t = 0;
                                        }
                                }
                        }
                }
                int ans = (cost - total) % 1000002013;
                fout << "Case #" << casenum << ": " << ans <<'\n';
        }
        fin.close();
        fout.close();
        //system("pause");
        return 0;
}