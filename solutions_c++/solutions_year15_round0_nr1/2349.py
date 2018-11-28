#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<fstream>

using namespace std;

int main()
{
fstream cin("A-large.in",ios::in);
fstream cout("A-large.out",ios::out);
int t;
cin>>t;
int c=1;
while(t--)
{
	int n;
	cin>>n;
	string s;
	cin>>s;
	int ans=0;
	int cnt=s[0]-'0';
	for (int i=1;i<=n;i++)
	  {
	  if ((i)>cnt&&s[i]!='0')
	    {
	    ans+=(i)-cnt;
	    int p=cnt;
	    cnt+=(i)-p;
		}
		cnt+=(s[i]-'0');
	  }
	cout<<"Case #"<<c++<<": "<<ans<<endl;
		
}	
return 0;	
}
