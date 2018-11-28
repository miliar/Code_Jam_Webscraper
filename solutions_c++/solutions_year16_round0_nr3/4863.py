#include <iostream>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <fstream>

using namespace std;

const int INF = 10000000;




int main()
{
    //ifstream cin ("Users/Roman/Desktop/GCJ/output.txt");
    //ofstream cout ("Users/Roman/Desktop/GCJ/output.txt");
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout.setf(ios_base::fixed);
    cout.precision(28);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        int n, m;
        cin >> n >> m;
        n--;
        cout << "Case #1:\n";
        int mx = (1 << n);
        int add = (1 << n);
        n++;
        //cout << mx << endl;
        for (int i = 1, k = 0; i < mx && k < m; i += 2) {
            int temp = i + add;
            vector < int > x(n, 0);
            for (int j = 0; j < n; ++j) {
                x[j] = temp % 2;
                temp /= 2;
            }
            vector < int > ans;
            for (int base = 2; base <= 10; ++base) {
                long long num = 0;
                for (int j = 0; j < x.size(); ++j) {
                    num *= base;
                    num += x[j];
                }
                for (long long j = 2; j * j <= num; ++j) {
                    if (num % j == 0) {
                        ans.push_back(j);
                        break;
                    }
                }
            }
            if (ans.size() == 9) {
                k++;
                for (int j = 0; j < x.size(); ++j) {
                    cout << x[j];
                }
                cout << " ";
                for (int j = 0; j < 9; ++j) {
                    cout << ans[j] << " ";
                }
                cout << endl;
            }
        }
    }
    return 0;
}