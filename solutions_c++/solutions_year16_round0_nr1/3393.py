#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll n, tn, org, t, i, mx, cnt, r, tot, _t;
int main() {
    cin>>t;
    for(_t = 1; _t <= t; _t++) {
        cin>>n;
        mx = (1<<10)-1;
        tot = 0;
        cnt = 0;
        org = n;
        while(tot != mx && cnt < 1e5) {
            tn = n;
            while(tn) {
                r = tn%10;
                tn /= 10;
                tot = tot | 1<<r;
            }


            cnt++;
            n += org;
        }
        if(tot != mx) {
            printf("Case #%lld: INSOMNIA\n", _t);
        }
        else {
            printf("Case #%lld: %lld\n", _t, n-org);
        }
    }

    return 0;
}
