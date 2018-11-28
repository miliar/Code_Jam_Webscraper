#include<bits/stdc++.h>
using namespace std;
 int main()
 {
int t,i,smax,trm,ans,cnt;
string s;

cin>>t;
for(trm=1;trm<=t;trm++)
{
cin>>smax;
cin>>s;
cnt=s[0]-'0';
ans=0;
for(i=1;i<=smax;i++)
{
    if(i>cnt && s[i]-'0')
        {ans+=(i-cnt);
          cnt+=(i-cnt);
        }
    cnt+=(s[i]-'0');
}

cout<<"Case #"<<trm<<": "<<ans<<endl;
}



 }
