#include<iostream>
#include<string>
using namespace std;
int main()
{
    int i,j,k,t,n;
    string s;
    cin>>t;
    j=1;
    while(t--)
    {
        cin>>n;
        cin>>s;
        int ans=0;
        int now=0;
        for(i=0;i<=n;i++)
        {
            if(s[i]>0 && now+ans<i)
            {
                ans = i-now;
            }
            now+=(s[i]-'0');
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
        j++;
    }
}
