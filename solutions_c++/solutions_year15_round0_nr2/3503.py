#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll dine[1010];
int main()
{
    ll t,d,i,j,temp,ans,maxx,var=0;
    ifstream in("a.txt");
    ofstream out("b.txt");
    in>>t;
    while(t--)
    {
        var++;
        in>>d;
        for(i=1;i<=d;i++)
            in>>dine[i];
            maxx=0;
        for(i=1;i<=d;i++)
        {
            if(maxx<dine[i])
                maxx=dine[i];
        }
        ans=maxx;
        for(i=1;i<=maxx;i++)
        {
            temp=0;
            for(j=1;j<=d;j++)
            {
                if(dine[j]>i)
                    {temp+=(dine[j]/i-1);
                if(dine[j]%i>0)
                    temp++;
                    }
            }
            if((temp+i)<ans)
                ans=temp+i;
        }
        out<<"Case #"<<var<<": "<<ans<<endl;
    }
}
