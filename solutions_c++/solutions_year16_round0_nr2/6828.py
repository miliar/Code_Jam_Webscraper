#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
int p=1;
while(t--)
{
char s[1016];
memset(s,0,sizeof(s));
cin>>s;
int c=0;
for(int i=0;i<strlen(s);i++)
if(s[i]=='+')
c++;
if(c==strlen(s))
{
cout<<"Case #"<<p<<": 0\n";
p++;
continue;
}
c=0;
int ans=0;
while(c!=strlen(s))
{
c=0;
if(s[0]=='+')
{
int ind=0;
for(int i=1;i<strlen(s);i++)
if(s[i]=='-')
{
ind=i;
break;
}
if(ind==0)
                break;
int p=0;
for(int i=0;i<ind;i++)
{
s[i]='-';
p=1;
}
if(p==1)
ans++;
}
else
{
int ind=0;
for(int i=1;i<strlen(s);i++)
if(s[i]=='+')
{
ind=i;
break;
}
if(ind==0)
{
                ans++;
                break;
}
int p=0;
for(int i=0;i<ind;i++)
{
s[i]='+';
//cout<<s[i]<<endl;
p=1;
}
//cout<<s<<endl;
if(p==1)
ans++;
}
for(int i=0;i<strlen(s);i++)
if(s[i]=='+')
c++;
if(c==strlen(s))
break;
}
cout<<"Case #"<<p<<": "<<ans<<endl;
p++;
}
return 0;
}
