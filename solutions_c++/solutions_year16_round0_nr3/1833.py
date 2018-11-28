#include <bits/stdc++.h>
using namespace std;

int cnt[1 << 16];

long long transform(vector<int> num, int k)
{
    long long ret = 0;
    for(int i = 0; i < num.size(); i++) {
        ret = ret * k + num[i];
    }
 //   cout << ret << endl;
    return ret;
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    for(int i = 1; i < 1 << 16; i++) {
        for(int j = 0; j < 16; j++) if(i >> j & 1) {
            cnt[i] ++;
        }
    }
    int T, ca = 1;
    cin >> T;
    while(T--) {
        int N, J;
        cin >> N >> J;
        cout << "Case #" << ca << ":" << endl;
        vector<int> base;
        base.push_back(1);
        for(int i = 1; i < N - 1; i++) base.push_back(0);
        base.push_back(1);
        for(int i = 0; i < N; i++) {
            cout << base[i] ;
        }
        for(int i = 2; i <= 10; i++) {
            if(i & 1) {
                cout << " " << 2;
            } else {
                cout << " " << i + 1;
            }
        }
        cout << endl;
        vector<int> odd;
        vector<int> even;
        for(int i = 1; i < N - 1; i += 2) odd.push_back(i);
        for(int i = 2; i < N - 1; i += 2) even.push_back(i);
        int hehe = 0;
        for(int i = 1; i < 1 << odd.size(); i++) {
            for(int j = 1; j < 1 << even.size(); j++) {
                if((cnt[i]  == cnt[j] )) {
                    vector<int> tmp = base;
                    for(int k = 0; k < odd.size(); k++) {
                        if(i >> k & 1) {
                            tmp[odd[k]] = 1;
                        }
                    }
                    for(int k = 0; k < even.size(); k++) {
                        if(j >> k & 1) {
                            tmp[even[k]] = 1;
                        }
                    }
                    for(int k = 0; k < N; k++) {
                        cout << tmp[k] ;
                    }
                    for(int k = 2; k <= 10; k++) {
                        if(k & 1) {
                            cout << " " << 2;
                        } else {
                            cout << " " << k + 1;
                        }
                    }
                    cout << endl;
                    ++hehe;
                    if(hehe == J - 1) return 0;
                }
            }
        }
    }
    return 0;
}
