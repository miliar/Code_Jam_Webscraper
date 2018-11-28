#include<iostream>
#include<string>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int caseNo=1;
    while(t-->0)
    {
        string s;
        cin>>s;
        string ans;
        int n=s.size();

        ans=s[0];
        
        for(int i=1;i<n;i++)
        if(ans[0]<=s[i])
        ans=s[i]+ans;
        else
        ans=ans+s[i];
        
        cout<<"Case #"<<caseNo<<": "<<ans<<endl;
        caseNo++;
    }
    return 0;
}
