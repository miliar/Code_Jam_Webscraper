#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;

int main() {
    int t;
    scanf("%d ",&t);
    For(i1,t) {
        ll vys1=-1,vys2=-2;
        ll n,p;
        scanf("%lld %lld ",&n,&p);
        if(p==(1ll<<n)) {
            printf("Case #%d: %lld %lld\n",i1+1,p-1,p-1);
            continue;
        }
        //ratanie vys2
        ll mam=1ll<<n;
        vys2=(1ll<<n)-1ll;
        ll kolko=1ll;
        while(mam>p) {
            mam/=2ll;
            vys2-=kolko;
            kolko*=2ll;
        }
        //ratanie vys1
        mam=1ll<<(n-1ll);
        vys1=0;
        kolko=1ll<<(n-2ll);
        ll pric=2ll;
        while(p>mam) {
            mam+=kolko;
            kolko/=2ll;
            vys1+=pric;
            pric*=2ll;
        }
        printf("Case #%d: %lld %lld\n",i1+1,vys1,vys2);
    }
return 0;
}
