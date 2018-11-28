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

bool ar[100000005];
int prime[100000005];
void seivePrime(void)
{
    int n,i,v,j;
    prime[0]=2;
    n=1;v=sqrt(sz)+1;
    for(i=3;i<=v;i+=2)
    {
        if(!ar[i])
        {
            for(j=i*i;j<sz;j+=2*i)
                ar[j]=1;
            prime[n++]=i;//ps2(" ",prime[n-1]);
        }
    }
    for(j=i;j<sz;j+=2)
    if(!ar[j])
        prime[n++]=j;//ps2(" ",prime[n-1]);
    return;
}
ll vec[11];
int main()
{
    freopen("Cin.in","r",stdin);
    freopen("Cout.in","w",stdout);
    ll t,T,i,j,k,l,a,b,c,d,N,J,cnt;
    scanf("%lld",&t);
    T=t;
    while(t--)
    {
        cnt=0;
        scanf("%lld %lld",&N,&J);
        printf("Case #%lld:\n",T-t);
        a=1ll<<(N-1);
        for(i=1;i<a;i+=2)
        {
            for(k=2;k<=10;k++)
            {
                b=k;
                c=1;
                for(j=1;j<N-1;j++)
                {
                    if(i&(1ll<<j))
                    {
                        c+=b;
                    }
                    b=b*k;
                }
                //b=b*k;
                c+=b;
                d=1ll+sqrt(c);
                for(l=2;l<d;l++)
                {
                    if(c%l==0){vec[k]=l; break;}
                }
                if(l==d) break;
            }
            if(k==11)
            {
                printf("1");
                for(j=N-2;j;j--)
                {
                    if(i&(1ll<<j)) printf("1");
                    else printf("0");
                }
                printf("1");
                for(b=2;b<=10;b++)
                {
                    printf(" %lld",vec[b]);
                }
                puts("");
                cnt++;
                if(cnt==J)
                    break;
            }
        }
    }

    return 0;
}
