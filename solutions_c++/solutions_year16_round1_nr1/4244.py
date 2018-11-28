#include <iostream>
#include <cstdio>
using namespace std;
const int MAXN=1005;
int T;
char ch;
string s,ans;
int main()
{
    //freopen("DATA.txt","r",stdin);
    freopen("large.1.in","r",stdin);
    freopen("large.1.out","w",stdout);
    scanf("%i",&T);
    for (int t=1;t<=T;t++)
    {
        cin>>s;
        ans=s[0];
        for (int i=1;i<s.length();i++)
        {
            ch=s[i];
            if (ch>=ans[0])ans=ch+ans;
            else ans+=ch;
        }
        cout<<"Case #"<<t<<": "<<ans<<'\n';
    }
}
