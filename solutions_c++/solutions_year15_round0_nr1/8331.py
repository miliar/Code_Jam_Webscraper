#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int t,i,k;
    cin>>t;

    for(i=1;i<=t;i++)
    {

        int smax;
        char shy[10005];

        cin>>smax>>shy;

        long long ans=0,nowup=0;

        for(k=0;k<=smax;k++)
        {

            if(shy[k]!='0')
            {
                if(nowup>=k)
                 {
                    nowup=nowup+shy[k]-48;
                 }
            else
                {
                    ans=ans+(k-nowup);
                    nowup=nowup+ (k-nowup) + shy[k]-48;
                }
            }

        }
        cout<<"Case #"<<i<<": "<<ans<<"\n";

    }
    return 0;
}
