#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<list>
#include<algorithm>
#define prime  1000002013
using namespace std;
int T;
int m,n;
int o[3000],e[3000],p[3000];
long long cost1;
long long cost2;


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin>>T;
    for (int tt=1; tt<=T; ++tt)
    {
        cin>>n>>m;
        cost1=cost2=0;
        for (int i=1; i<=m; ++i)
        {
            cin>>o[i]>>e[i]>>p[i];
            cost1+=(((n+n-(e[i]-o[i]-1))*(e[i]-o[i])/2)%prime)*p[i]%prime;
            cost1%=prime;
            //cout<<e[i]<<"  "<<o[i]<<endl;
            //cout<<cost1<<" "<<((n+n-(e[i]-o[i]-1))*(e[i]-o[i]))/2<<endl;
        }
        //cout<<cost1<<endl;
        for (int i=m+1; i<=2*m; ++i)
        {
            o[i]=e[i-m];
            p[i]=-p[i-m];
        }
        for (int i=1; i<=2*m-1; ++i)
            for (int j=i+1; j<=2*m; ++j)
                if ((o[i]>o[j]) || ((o[i]==o[j] && (p[i]<p[j]))))
                {
                    int temp=o[i]; o[i]=o[j]; o[j]=temp;
                    temp=p[i]; p[i]=p[j]; p[j]=temp;
                }
       // for (int i=1; i<=2*m; ++i) cout<<o[i]<<" "<<p[i]<<endl;
        for (int i=1; i<=2*m; ++i)
        {
            if (p[i]<0)
            {
                for (int j=i-1; j>=1; --j)
                {
                    if (p[i]+p[j]<0)
                    {
                        cost2+=(((n+n-(o[i]-o[j]-1))*(o[i]-o[j])/2)%prime)*p[j]%prime;
                        p[i]+=p[j];
                        p[j]=0;
                        cost2%=prime;
                    }
                    else
                    {
                        cost2+=(((n+n-(o[i]-o[j]-1))*(o[i]-o[j])/2)%prime)*(-p[i])%prime;
                        p[j]+=p[i];
                        p[i]=0;
                        cost2%=prime;
                    }
                    //cout<<i<<"  "<<j<<" "<<p[i]<<"  "<<p[j]<<" "<<cost2<<endl;
                    if (p[i]==0) break;
                }
            }
        }
        //cout<<cost2<<endl;
        cost1+=prime;
        cost1-=cost2;
        cost1%=prime;
        cout<<"Case #"<<tt<<": "<<cost1<<endl;

    }
    return 0;
}
