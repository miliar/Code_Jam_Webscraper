#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second

using namespace std;

int t, n;
string s;

int main() {
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        //cout << i << endl;
        vector <char> mas;
        vector <int> num_let[105];
        bool flag = false;
        for (int j = 0; j < n; ++j) {
            //cout << j << endl;
            if (j == 0) {
                cin >> s;
                int prev = 0;
                mas.puba(s[0]);
                for (int k = 1; k < (int) s.size(); ++k) {
                    if (s[k] != s[k - 1]) {
                        num_let[(int) mas.size() - 1].puba(k - prev);
                        mas.puba(s[k]);
                        prev = k;
                    }
                }
                num_let[(int) mas.size() - 1].puba((int) s.size() - prev);
                   
            } else {
                vector <char> temp;
                cin >> s;
                int prev = 0;
                temp.puba(s[0]);
                for (int k = 1; k < (int) s.size(); ++k) {
                    if (s[k] != s[k - 1]) {
                        num_let[(int) temp.size() - 1].puba(k - prev);
                        temp.puba(s[k]);
                        prev = k;
                    }
                }
                num_let[(int) mas.size() - 1].puba((int) s.size() - prev);
                
                if (temp != mas) {
                    printf("Case #%d: Fegla Won\n", i + 1);
                    flag = true;
                    break;
                }
            }
            
        }
        if (flag) {
            continue;
        }
        //cout << "@" << endl;
        int ans = 0;
        for (int j = 0; j < 105; ++j) {                
            if (!num_let[j].size()) {
                continue;
            }
            int sum = 0;
            for (int k = 0; k < (int) num_let[j].size(); ++k) {
                sum += num_let[j][k];
            }
            sum /= (int) num_let[j].size();
            //cout << j << " " << sum << endl;
            int mem = 1e9;
            for (int k = -1; k < 2; ++k) {
                int ttemp = 0;
                for (int i2 = 0; i2 < (int) num_let[j].size(); ++i2) {
                    ttemp += abs(num_let[j][i2] - sum - k);
                }
                mem = min(mem, ttemp);
            }
            ans += mem;
        }
        printf("Case #%d: %d\n", i + 1, ans);
        /*
        for (int j = 0; j < (int) mas.size(); ++j) {
            cout << mas[j].ff << " " << mas[j].ss << endl;
        }*/
    }
    return 0;   
}