#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int seen[10];
ll tot, in;

int tc, tcn;
int main(){
    scanf(" %d", &tc);
    while(tc--){
        scanf(" %lld", &in);
        if(!in){
            printf("Case #%d: INSOMNIA\n", ++tcn);
            continue;
        }
        tot = 0;
        memset(seen, 0, sizeof seen);
        while(!*(min_element(seen,seen+10))){
            tot += in;
            for(ll x=tot;x;x/=10) seen[x%10] |= 1;
        }
        printf("Case #%d: %lld\n", ++tcn, tot);
    }
}
