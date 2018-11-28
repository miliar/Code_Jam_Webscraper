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
const int sz=100000 + 5;
const int mod=1000000000 + 7;

using namespace std;
typedef long long int ll;

ll c[sz],cc[sz];

int main()
{
    freopen("Ain.in","r",stdin);
    freopen("Aout.in","w",stdout);
    int t,T;
    ll i,j,k,m,e,n,cnt,h,res;
    cnt=0;
    scanf("%d",&t);
    T=t;
    e=(1ll<<10ll)-1ll;
    while(t--)
    {
        scanf("%lld",&n);

        k=0;
        m=0;
        ms(0,cc);
        ms(0,c);
        //ms(0,c1);
        printf("Case #%d: ",T-t);
        if(!n)
        {
            printf("INSOMNIA\n");
            continue;
        }
        while(n)
            m|=1ll<<(n%10ll),c[k]=cc[k++]=n%10ll,n/=10ll;
        ///int c1;
        for( ;m!=e ; )
        {
            h=0ll;
            for(j=0;j<k;j++)
            {
                //c1[j]=c[j];
                c[j]=(cc[j]+c[j]+h);
                h=c[j]/10ll;
                c[j]%=10ll;
                m|=(1ll<<c[j]);
            }
            if(h) c[k++]=1ll,m|=2ll;
            //if(m==e) cnt++,printf("%d\n",i);
            //res=i;
        }
        --k;
        //printf("%d\n",c1);
        while(!c[k]) k--;
        while(k>=0) printf("%d",c[k--]);
        puts("");
        ///if(c1==1000) break;
        ///cnt++;
    }

   // printf("%d\n",cnt);

    return 0;
}
