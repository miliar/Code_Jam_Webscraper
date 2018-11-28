#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        string s;
        cin>>s;
        int n=s.size();
        string ans="";
        for(int i=0;i<n;i++)
        {
            int sz=ans.size();
            if(sz==0) ans=s[i];
            else
            {
                char ch=ans[0];
                if(ch<=s[i]) ans=s[i]+ans;
                else ans=ans+s[i];
            }
        }
        printf("Case #%d: ",c);
        cout<<ans<<endl;
    }
return 0;
}
