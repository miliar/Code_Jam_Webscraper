#include<bits/stdc++.h>
#define f(i,a,n) for(int i=a;i<n;i++)
#define S second
#define F first
#define Sc(n) scanf("%lld",&n)
#define scc(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define sp(a) scanf("%lld %lld",a.first,a.second)
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define all(a) a.begin(),a.end()
#define sc(n) scanf("%d",&n)
#define It iterator
#define SET(a,b) memset(a,b,sizeof(a))
// inbuilt functions
#define DRT()  int t,t1; cin>>t; while(t1++<t)
// __gcd,  __builtin_ffs,     (returns least significant 1-bit, __builtin_ffsll(1)=1)
// __builtin_clz,             (returns number of leading zeroes in 
// __builtin_popcount,
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> vi;
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define trv(s,it) for(auto it:s)
string s,s1;
int check()
{	
		f(i,0,s.size())
			if(s[i]!='+')
				break;
			else if(i==s.size()-1)
				s.clear();
		if(s.empty())
			return 0;
	return 1;
}
int func(int t1)
{	int n,a=0;
	while(check())
	{	
		int i=0;
		if(s[0]=='+')
		{	while(s[i]=='+')
			s[i++]='-';
			a++;
		}
		i=s.size()-1;
		while(s[i--]=='+')
			s.pop_back();
		n=s.size()-1;
		f(i,0,n+1)
			s1.pb((s[i]=='+')?'-':'+');
		a++;
		s=s1;
		s1.clear();
//		cout<<s<<endl;
	}
		cout<<"Case #"<<t1<<": "<<a<<"\n"; 
}
int main()
{	DRT()	
	{	cin>>s;
		func(t1);
	}
}


