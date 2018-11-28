#include <iostream>
#include<cstdio>
using namespace std;

int main() {
int t,s;
cin>>t;
for(int j=1;j<=t;j++)
{
cin>>s;
int m=0;
int ans=0,b=0;
for(int i=0;i<=s;i++)
{
scanf("%1d",&b);
if(m<i && b!=0)
{
ans=(i-m)+ans;
m=m+ans;
}
m=m+b;

}
cout<<"Case #"<<j<<":"<<" "<<ans<<"\n";
}

	return 0;
}