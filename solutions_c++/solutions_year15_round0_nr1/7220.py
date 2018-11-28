#include<iostream>
#include<stdio.h>
#include<math.h>
#include<cstring>
#include<stdlib.h>
#include<map>
#include<algorithm>
#include<climits>
#include<set>
#include<vector>
#include<stack>
#include<queue>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    long long int t,T;
    cin>>t;
    T=t;

    while(t--)
    {
        char s[10001];
        long long int Smax,Scurrent=0,ans=0,i,delta=0;

        cin>>Smax;
        cin>>s;

        //cout<<s<<endl;
        for(i=0;i<=Smax;i++)
        {
            delta=0;

            if(Scurrent<i && s[i]!='0' && i!=0)
            {
                delta=i-Scurrent;
                Scurrent+=delta;
                ans+=delta;
            }

            Scurrent+=(s[i]-'0');

        }
        cout<<"Case #"<<T-t<<": "<<ans<<endl;

    }

    return 0;
}
