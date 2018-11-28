//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000000 + 5;
const int mod=1000000000 + 7;

using namespace std;
typedef long long int ll;

int main()
{
    freopen("Din.in","r",stdin);
    freopen("Dout.in","w",stdout);
    ll t,T,i,j,k,l,K,C,S;
    scanf("%lld",&t);
    T=t;
    while(t--)
    {
        scanf("%lld %lld %lld",&K,&C ,&S);
        printf("Case #%lld:",T-t);
        if(C==1 && S<K) {printf(" IMPOSSIBLE\n");continue;}
        for(i=1;i<=K;i++) printf(" %lld",i);
        printf("\n");
    }

    return 0;
}
