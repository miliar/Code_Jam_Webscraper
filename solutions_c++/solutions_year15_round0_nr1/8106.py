#include <iostream>
#include <string.h>
#include <cstdio>
using namespace std;

int smax;
int audience[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long int T;
    unsigned long long int total_audience=0;
    unsigned long long int ans=0;
    cin>>T;
    for(long long int m=1;m<=T;m++)
    {
        cin>>smax;
        for(int i=0;i<=smax;i++)
        {
            scanf("%1lld",&audience[i]);
        }
        for(int i=0;i<=smax;i++)
        {

            if(i>(total_audience))
            {
                ans=ans+(i-total_audience);
                total_audience=total_audience+(i-total_audience);
            }
            total_audience=total_audience+audience[i];
        }
        cout<<"Case #"<<m<<": "<<ans<<endl;
        total_audience=0;
        ans=0;
    }


    return 0;
}
