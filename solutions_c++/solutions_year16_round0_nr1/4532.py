#include <bits/stdc++.h>

using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define pd(x) printf("%d",x)
#define pull(x) printf("%llu",x)
#define pll(x) printf("%lld",x)

#define pn() printf("\n")
#define loop(i, a, b) for (int i = int(a); i < int(b); i++)
#define MAXN 1000005
typedef long long int ll;
typedef unsigned long long int ull;

int d[10];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out_large1CAs.txt","w",stdout);
    int t,n,flag;
    ll a,tmp,e;
    cin>>t;
    loop(k,1,t+1){
        cin>>n;
        if(n==0){
            cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
        }
        else{
            a=0;
            loop(i,0,10)d[i]=0;
            flag=1;
            while(flag){
                a+=n;
                tmp=a;
                while(tmp>0){
                    e=tmp%10;
                    tmp=tmp/10;
                    d[e]=1;
                }
                loop(i,0,10){
                    if(d[i]==0){
                        flag=1;
                        break;
                    }
                    else flag=0;
                }
            }
            cout<<"Case #"<<k<<": "<<a<<endl;
        }
    }

    return 0;
}








