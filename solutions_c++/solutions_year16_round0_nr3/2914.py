
#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll i, n, k, j, l, t, _t, sz, f, cnt, num, res;
string s, tmp;
vector<string> v, vs;
vector<int> p;
ll vis[10015];

ll convert(string s, ll base) {
    ll l = s.length();
    ll ans = 0;
    for(ll i = 0; i < l; i++) {
        ans = ans*base + s[i] - '0';
    }
    return ans;
}
int main()
{
    cin>>t;
    for(_t = 1; _t <= t; _t++) {
        cin>>n>>k;
        memset(vis, 0, sizeof vis);
        s = "1000000000000001";
        v.push_back(s);
        for(i = 1; i <= 14; i++) {
            sz = v.size();
            for(j = 0; j < sz; j++) {
                tmp = v[j];
                tmp[i] = '1';
                v.push_back(tmp);
            }
        }
        cnt = 0;
        memset(vis, 0, sizeof vis);
        for(i = 2; i <= 10004; i++) {
            if(!vis[i]) {
                p.push_back(i);
                for(j = i; j <= 10004; j += i) {
                    vis[j] = 1;
                }
            }
        }
        for(i = 0; i < v.size(); i++) {
            f = 1;
            for(j = 2; j <= 10; j++) {
                num = convert(v[i], j);
                res = 0;
                for(l = 0; l < p.size(); l++) {
                    if(num%p[l] == 0) {
                        res = 1;
                        break;
                    }
                }
                if(!res) f = 0;
            }
            if(f) {
                vs.push_back(v[i]);
                cnt++;
            }
            if(cnt >= k) break;
        }
        printf("Case #%lld:\n", _t);
        for(i = 0; i < vs.size(); i++) {
            cout<<vs[i];
            for(j = 2; j <= 10; j++) {
                num = convert(vs[i], j);
                for(k = 2; k*k <= num; k++) {
                    if(num%k == 0) {
                        cout<<" "<<k;
                        break;
                    }
                }
            }
            cout<<endl;
        }
    }
    return 0;
}
