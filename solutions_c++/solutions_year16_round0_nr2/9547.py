#include <bits/stdc++.h>
#define IOS ios::sync_with_stdio(0);
using namespace std;



int f(string p)
{
    int total=0,moves=0;
    for(int i=0;i<p.size();++i){if(p[i]=='+'){++total;}}
    if(total==p.size()) return moves;
    while(total!=p.size())
    {
        ///cout<<p<<endl;
        if(p[0]=='-')
        {
            for(int i=0;p[i]!='+'&&i<p.size();++i)
            {
                p[i]='+';
            }
        }else
        if(p[0]=='+')
        {
            for(int i=0;p[i]!='-'&&i<p.size();++i)
            {
                p[i]='-';
            }
        }
        ++moves;
        total=0;
        for(int i=0;i<p.size();++i){if(p[i]=='+')++total;}
    }
    return moves;
}

int main()
{
   IOS
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   int cases;
   cin>>cases;
   string p;
   for(int i=1;i<=cases;++i)
   {
       cin>>p;
       cout<<"Case #"<<i<<": "<<f(p)<<endl;
   }
}
