#include <iostream>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <set>
using namespace std;
typedef unsigned long long ll;
ll t[100][70];
int main() {
    int tt;
    cin>>tt;
    for(int i = 1; i <= tt; ++i) {
        cout<<"Case #"<<i<<": ";
        int n;
        cin>>n;
        cin>>ws;
        unordered_map<string, int> st;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < 70; ++j) t[i][j] = 0;
            string s;
            getline(cin, s);
            string q;
            for(int j = 0; j < s.size(); ++j) {
                q.push_back(s[j]);
                if(j == s.size()-1 || s[j+1] == ' ') {
                    ++j;
                    int w = 0;
                    if(st.count(q)) {
                        w = st[q];
                    }
                    else {
                        w = st.size();
                        st[q] = w;
                    }
                    t[i][w/64] |= 1ull<<(w%64);

                    q.clear();
                }
            }
        }
        int ans = 0;
        ll fr[70] = {0};
        ll en[70] = {0};
        for(int i = 0; i < 70; ++i) {
            fr[i] = t[1][i];
            en[i] = t[0][i];
        }
        if(n == 2) {
            for(int i = 0; i < 70; ++i) {
                fr[i] = t[1][i];
                en[i] = t[0][i];
                ans += __builtin_popcount(fr[i]&en[i]);
            }
            cout<<ans<<'\n';
        }
        else {
            ans = 1e9;
            for(int i = 0; i < (1<<(n-2)); ++i) {
                ll fr2[70] = {0};
                ll en2[70] = {0};
                memcpy(fr2, fr, sizeof fr);
                memcpy(en2, en, sizeof en);
                int ans2 = 0;

                for(int j = 0; j < n-2; ++j) {
                    if(i & (1<<j)) {
                        for(int k = 0; k < 70; ++k) {
                            fr2[k] |= t[j+2][k];
                        }
                    }
                    else {
                        for(int k = 0; k < 70; ++k) {
                            en2[k] |= t[j+2][k];
                        }
                    }
                }
                for(int i = 0; i < 70; ++i) {
                    ll q = fr2[i]&en2[i];
                    ans2 += __builtin_popcount(q&0xFFFFFFFF) + __builtin_popcount(q>>32);
                }
                ans = min(ans, ans2);
            }
            cout<<ans<<'\n';
        }
    }
}
