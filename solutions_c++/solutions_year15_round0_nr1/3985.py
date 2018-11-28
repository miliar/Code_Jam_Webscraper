#include <bits/stdc++.h>

using namespace std;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,cas=0,x,i,cunt,ans,maxx;
    string s;
    cin>>t;
    while(t--)
    {
        cas++;
        printf("Case #%d: ",cas);
        cin>>maxx;
        cin>>s;
        x = s.length();
        cunt=s[0]-'0',ans=0;
        for(i=1;i<x;i++) {
            if( i > cunt ) {
                ans += i - cunt;
                cunt += i - cunt;
            }
            cunt += s[i]-'0';
        }
        printf("%d\n",ans);
    }
}
