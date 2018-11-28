/*input
5
-
-+
+-
+++
--+-

*/
#include <bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x);
#define slld(x) scanf("%lld",&x);
#define ss(x) scanf("%s",x);
#define sc(x) scanf("%c",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define bit(x,i) (x&(1<<i))  //select the bit of position i of x
#define lowbit(x) ((x)&((x)^((x)-1))) //get the lowest bit of x
#define pc1(x) cout<<x<<" "<<endl;
#define pc2(x,y) cout<<x<<" "<<y<<" "<<endl;
#define pc3(x,y,z) cout<<x<<" "<<y<<" "<<z<<" "<<endl;
#define pc4(w,x,y,z) cout<<w<<" "<<x<<" "<<y<<" "<<z<<" "<<endl;
#define pce(x) cout<<x<<endl;
#define ps0() cout<<endl;
#define ps1(x) cout<<#x<<" ";
#define ps2(x,y) cout<<#x<<" "<<y<<" "<<endl;
#define ps3(x,y,z) cout<<#x<<" "<<y<<" "<<z<<" "<<endl;
#define ps4(w,x,y,z) cout<<#w<<" "<<x<<" "#y<<" "<<z<<" "<<endl;
#define pse(x) cout<<#x<<endl;
#define GET_MACRO(_0, _1, _2, _3, _4, NAME, ...) NAME
#define GET_MACRO1(_1, _2, _3, _4, NAME, ...) NAME
#define ps(...) \
		do{if (DEBUG) GET_MACRO(_0, ##__VA_ARGS__, ps4, ps3, ps2, ps1, ps0)(__VA_ARGS__)} while(0);
#define pc(...) \
 		do{if (DEBUG) GET_MACRO1(__VA_ARGS__, pc4, pc3, pc2, pc1)(__VA_ARGS__)} while(0);
#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI; 

#define DEBUG 0

string rev(string a)
{
	string b="";
	int l=a.size()-1;
	for(int i=l;i>=0;i--)
	{
		if(a[i]=='-')
			b+='+';
		else if(a[i]=='+')
			b+='-';
	}
	return b;
}
bool check(string s)
{
	for(int i=0;i<s.size();i++)
	{
		if(s[i]=='-')
			return false;
	}
	return true;
}
bool check1(string s)
{
	for(int i=0;i<s.size();i++)
	{
		if(s[i]=='+')
			return false;
	}
	return true;
}

int main()
{
	// string a="----";
	// cout<<rev(a.substr(1,2));
	READ("B-large.in")
	WRITE("question2_out_large.txt")
	int t,c,l,k,n;
	string s;
	sd(t)
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		cin>>s;
		pc(s)
		n=s.size();
		l=s.size()-1;
		c=0;
		while(l>=0)
		{
			pc(s)
			if(s[l]=='+')
			{
				l--;
				continue;
			}
			k=0;
			while(s[k]=='+')
				k++;
			if(k!=0)
			{
				c++;
				s=rev(s.substr(0,k))+s.substr(k);
			}
			s=rev(s.substr(0,l+1))+s.substr(l+1,n-l-1);
			l--;
			c++;
			pc(s)
		}
		printf("%d\n",c);
	}	
}
