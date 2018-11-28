#include<bits/stdc++.h>
using namespace std;
 
typedef long long int lli;
   
#define pc(x) putchar_unlocked(x);
#define gc() getchar_unlocked();
#define F(i, n) for(i = 0;i < n; ++i)
#define M 1000003
 
 lli mint(lli a,lli b)
 {
		if(a<b)
		return a;
		else return b;
		}
 
int main()
{
lli x=1,t;
cin>>t;
while(t--)
{lli n,i;
cin>>n;
string s;
cin>>s;
lli ans=0,a=s[0]-'0';
for(i=1;i<n+1;i++)
{if(s[i]!='0')
{
	if(a>=i)
a+=s[i]-'0';
else 
{
	ans+=i-a;
	a+=s[i]-'0'+i-a;
}
}
}
cout<<"Case #"<<x<<": "<<ans<<"\n";	
x++;}
	
	return 0;
}  
