#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
set<int> s;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,b;long long int n,m,a;
    cin>>T;
    int TT=0;
    while(T--)
    {TT++;
        s.clear();
        FOR(i,0,9)
        s.insert(i);
        cin>>n;
        m=n;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",TT);
            else
        while(1)
        {
            a=n;
            while(a>0)
            {
                b=a%10;
                s.erase(b);
                a=a/10;
            }
            if(s.empty())
            {printf("Case #%d: %lld\n",TT,n);break;}
            n=n+m;
        }
    }
    return 0;
}
