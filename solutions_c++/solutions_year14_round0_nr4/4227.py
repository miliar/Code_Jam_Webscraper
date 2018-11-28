#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
        freopen("E.in", "r", stdin);
        freopen("E.out", "w", stdout);
        int T;
        cin >> T;
        for (int i = 0; i < T; i ++) {
                int N;
                cin >> N;
                vector<double> Naomi;
                vector<double> Naomi1;
                vector<double> Ken;
                for (int j = 0; j < N; j ++) {
                        double tmp;
                        cin >> tmp;
                        Naomi.push_back(tmp);
                        Naomi1.push_back(tmp);
                }
                for (int j = 0; j < N; j ++) {
                        double tmp;
                        cin >> tmp;
                        Ken.push_back(tmp);
                }

                sort(Naomi.begin(), Naomi.end());
                sort(Naomi1.begin(), Naomi1.end());
                sort(Ken.begin(), Ken.end());

                int cnt = 0;

                int score = 0;

                for (int i = 0; i < Naomi.size();) {
                        while(cnt < N && Ken[cnt] < Naomi[i]) {
                                cnt ++;
                        }
                        if (i >= cnt) {
                                Naomi.erase(Naomi.begin() + i);
                        } else {
                               i ++;
                               score ++;
                        }
                }

                int score1 = 0;

                cnt = 0;

                for (int i = Naomi1.size() - 1; i >= 0; i --) {
                        while (cnt < N && Ken[N - 1 - cnt] > Naomi1[i]) {
                                cnt ++;
                        }
                        if (Naomi1.size() - 1 - i >= cnt) {
                                Naomi1.erase(Naomi1.begin() + i);
                                score1 ++;
                        }
                }

                cout << "Case #" << i + 1 << ": " << score << " "  << score1 << endl;
        }  
        return 0;
}
