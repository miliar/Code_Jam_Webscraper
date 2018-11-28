#include<bits/stdc++.h>
using namespace std;

#define ll long long int


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string a;
    ll t,j,n,friends,start,i,next;

    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>n;
        cin>>a;

        friends=0;
        start=a[0]-'0';
        for(i=1;i<=n;i++)
        {
            next=a[i]-'0';
            if(!next)
                continue;
            else
            {
                if(i<=start)
                    start+=next;
                else
                {
                    friends+=i-start;
                    start+=friends+next;
                }
            }
        }

        cout<<"Case #"<<j<<": "<<friends<<"\n";
    }
    return 0;
}
