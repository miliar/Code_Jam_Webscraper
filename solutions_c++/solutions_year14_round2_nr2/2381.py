#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
    int t,a,b,k,ans;
    cin>>t;
    for(int s=1;s<=t;s++)
    {
        cin>>a>>b>>k;
        ans=0;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if((i&j)<k)
                    ans++;
            }
        }
        cout<<"Case #"<<s<<": "<<ans<<endl;
    }

}
