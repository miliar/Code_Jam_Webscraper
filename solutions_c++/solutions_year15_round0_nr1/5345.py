#include<bits/stdc++.h>
using namespace std;

#define l long long
#define pb(x) push_back(x)

int main()
{
    int t;
    cin>>t;
    for(int ix=1;ix<=t;ix++)
    {
        int n;
        string str;
        cin>>n>>str;
        int ans=0,peoplestanding=0;
        for(int i=0;i<str.length();i++)
        {
            if(str[i]=='0')
            ;
            else if(peoplestanding>=i)
            {
                peoplestanding+=(str[i]-'0');
            }
            else
            {
                ans+=(i-peoplestanding);
                peoplestanding =i+(str[i]-'0');

            }//cout<<ans<<" "<<peoplestanding<<endl;
        }
        cout<<"Case #"<<ix<<": "<<ans<<endl;
    }
}
