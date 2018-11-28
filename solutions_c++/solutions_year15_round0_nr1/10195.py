#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main()
{
    ll t,l;
    cin>>t;
    for(l=1;l<=t;l++)
    {
        int n,i,j,cnt,sum;
        string s;
        cin>>n;
        cin>>s;
        cnt=0;
        sum=s[0]-'0';
        for(i=1;i<=n;i++)
        {
            j=s[i]-'0';
            if(j)
            {
                if(sum<i)
                {
                    cnt+=(i-sum);
                    sum=i;
                }
                sum+=j;
            }
        }
        cout<<"Case #"<<l<<": "<<cnt<<endl;
    }
    return 0;
}
