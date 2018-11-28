#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define  get(a) scanf("%lld", &a)
#define  out(a) printf("%lld", a)
ll i,j,k,x,y,z;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("16Bl.out","w",stdout);
ll t;
cin>>t;
for(i=1;i<=t;i++)
{ll dnt=0; j=0; bool temp=false; ll ans;
	string s; cin>>s;  char c;
	if(s[0]=='-')
	{dnt++; temp=true;}
	
for(j=1;j<s.size();j++)
if(s[j]=='-'&&s[j-1]=='+')
dnt++;
cout<<"Case #"<<i<<": "<<dnt*2-temp<<endl;
}

   return 0;

}


