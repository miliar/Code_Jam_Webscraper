#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pair<int,int> >
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(;c<'0'||c>'9';c=getchar())if(c=='-')sign=-1;
    for(num=0;c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

double A[1003];
vector<int> V;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        int n=getnum(),k=getnum();

        double ans=0;

        for(int i=1;i<=n;i++)scanf("%lf",A+i);

        for(int i=0;i<(1<<n);i++)
        {
            if(__builtin_popcount(i)!=k)continue;

            for(int x=i,j=1;x>0;x/=2,j++)
            {
                if(x&1)V.pb(j);
            }

            double tot=0.0;

            for(int j=0;j<(1<<k);j++)
            {
                if(__builtin_popcount(j)!=k/2)continue;

                double val=1.0;

                for(int l=0;l<k;l++)
                {
                    double temp;
                    if(j&(1<<l))temp=A[V[l]];
                    else temp=1.00-A[V[l]];
                    val*=temp;
                }

                tot+=val;
            }

            //cout<<tot<<' ';

            ans=max(ans,tot);
            V.clear();
        }
        printf("Case #%d: ",cases);
        cout<<fixed<<ans<<endl;
    }
}
