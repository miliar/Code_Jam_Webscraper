# include <iostream>
using namespace std;
int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int case_,n,a,b;
cin>>case_;
int ans;
for(int j=1;j<=case_;j++)
{
cin>>n>>a>>b;
ans=0;
if(n==1)
{
ans=1;
}
else if(n==2)
{
if(a%2==1 && b%2==1 )
ans=0;
else
ans=1;
}
else if(n==3)
{
if(a==2&&b==3 || a==3&&b==2 || a==3&&b==4 || a==4&&b==3 || a==3&&b==3)
ans=1;
else
ans=0;
}
else if(n==4)
{
if(a==4&&b==4 || a==3&&b==4 || a==4&&b==3)
ans=1;
else
ans=0;
}
if(ans==1)
cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
else
cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
}
return 0;
}