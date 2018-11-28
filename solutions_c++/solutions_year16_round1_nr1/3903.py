//never give up  try to code every time
#include<bits/stdc++.h>
#define s(a) scanf("%d",&a)
#define S(a)  scanf("%lld",&a)
#define p(a) puts("a")
#define loop(a) for(int i=0;i<a;i++)
#define mx(x,y) x>y?x:y
#define mn(x,y) x>y?y:x
#define lld long long
#define ld long
#define mod 1000000007
#define max 100005
#define pb(a)  push_back(a)
#define pp(a) pop_back(a)
#define code_lover int main
using namespace std;
code_lover()
{
	freopen("love.txt","r",stdin);
	freopen("loveu.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	 {
	 	string s;
	 	cin>>s;
	 	string a,b;
	 	char c=s[0];
	 	a+=s[0];
	 	for(int i=1;i<s.size();i++)
	 	{
	 		if(s[i]>=c)
	 		   b+=s[i],c=s[i];
	 		   else
	 		   a+=s[i];
		 }
		 reverse(b.begin(),b.end());
		 printf("Case #%d: ",i);
		 cout<<b<<a<<endl;
	 	        
	 }
	
return 0;
}

