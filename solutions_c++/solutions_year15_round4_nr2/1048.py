/*Author:rednivrug15*/
#include<bits/stdc++.h>
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define ll long long
#define MOD 1000000007

long long power(long long a,long long b,long long mod)
{
    long long ret=1;

    while(b)
    {
        if(b%2==1)
            ret=(ret*a)%mod;
        b/=2;
        a=(a*a)%mod;
    }
    return ret;
}

int gcd(int a,int b)
{
    return b==0?a:gcd(b,a%b);
}


double temp(double v0,double v1,double x0,double x1)
{
    return (v0*x0+v1*x1)/(v0+v1);
}

double vol(double x,double y)
{
    return x+y;
}

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for(int test=1; test<=t; test++)
    {
            int n;
            printf("Case #%d: ",test);
            double  C,v;
            scanf("%d",&n);
            cin>>v>>C;

            double c[n],r[n];

            for(int i=0; i<n; i++)
                cin>>r[i]>>c[i];


            if(c[0]>c[1] && n==2)
            {
                swap(c[0],c[1]);
                swap(r[0],r[1]);
            }

            if(n==1)
            {
                if(c[0]==C)
                    printf("%.6lf\n",(v/r[0]));
                else
                    puts("IMPOSSIBLE");
            }

            else
            {
                   if(c[0]>C || c[1]<C)
                    puts("IMPOSSIBLE");

                   else if(c[0]==c[1])
                   {
                       if(c[0]==C)
                        printf("%.6lf\n",v/(r[0]+r[1]));
                       else
                        puts("IMPOSSIBLE");
                   }

                   else
                   {
                     double V1=(C*v-v*c[1])/(c[0]-c[1]);
                     double V2=v-V1;

                     double ans=max(V1/r[0],V2/r[1]);
                     printf("%.6lf\n",ans);
                   }
            }
    }
    return 0;
}
