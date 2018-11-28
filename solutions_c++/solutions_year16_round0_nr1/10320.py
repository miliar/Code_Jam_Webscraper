#include<bits/stdc++.h>
using namespace std;

#define sc scanf
#define pf printf
#define ll long long
#define vi vector<int>
#define mp make_pair
#define pb push_back

#define MAX 1<<31
#define MIN -(1<<31)
#define out freopen("outA.txt","w",stdout)
#define in freopen("A.in","r",stdin)

int main()
{
    in;
    out;
    int t,n,cas=1;
    sc("%d",&t);
    while(t--)
    {
        sc("%d",&n);
        int d=0,m=n,i,t;
        for(i=1;i<=2000;i++)
        {
            m=i*n;
            t=m;
            while(m)
            {
                d |= (1<<(m%10));
                m/=10;
            }
            if(d == 1023)
                break;
        }
        if(t==0)
        {
            pf("Case #%d: INSOMNIA\n",cas++);
        }
        else
            pf("Case #%d: %d\n",cas++,t);
    }
    return 0;
}

