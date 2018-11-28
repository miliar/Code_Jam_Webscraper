#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n;
    string s;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        int sum=0,ans=0,c1=0,c2=0;
        cin>>n>>s;
        for(int i=0;i<n;i++)
        {
            c1=int(s[i]-'0');
            c2=int(s[i+1]-'0');
            sum+=c1;
            if(sum<i+1)
            {
                ans+=i+1-sum;
                sum+=i+1-sum;
            }
        }
        sum+=c2;
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
    return 0;
}
