#include<bits/stdc++.h>
#define f(i,a,n) for(int i=a;i<n;i++)
#define S second
#define F first
#define Sc(n) scanf("%lld",&n)
#define scc(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define sp(a) scanf("%lld %lld",&a.first,&a.second)
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define all(a) a.begin(),a.end()
#define sc(n) scanf("%d",&n)
#define It iterator
#define SET(a,b) memset(a,b,sizeof(a))
#define DRT()  int t,t1=0; cin>>t; while(t1++<t)
// inbuilt functions
// __gcd,  __builtin_ffs,     (returns least significant 1-bit, __builtin_ffsll(1)=1)
// __builtin_clz,             (returns number of leading zeroes in 
// __builtin_popcount,
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> vi;
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define trv(s,it) for(auto it:s)
int ar[][3]={{1,0,0},{1,1,0},{1,2,1},{2,3,3},{5,5,6},{11,10,11},{22,21,21},{43,43,42},{85,86,85},{170,171,171},{341,341,342},{683,682,683},{1366,1365,1365}};
char O[]="PRS";
int main()
{	DRT()
	{	int n,r,p,ss,fl;
		string s,t;
		s.clear();
		t.clear();
		cout<<"CASE #"<<t1<<": ";
		cin>>n>>r>>p>>ss;
		if(p==ar[n][0] && r==ar[n][1] && ss==ar[n][2])
		{	fl=0;
		}
		else if(ss==ar[n][0] && p==ar[n][1] && r==ar[n][2])
		{	fl=2;
		}
		else if(r==ar[n][0] && ss==ar[n][1] && p==ar[n][2])
		{	fl=1;
		}
		else
		{	cout<<"IMPOSSIBLE\n"; continue;}
		s=O[fl];
		while(s.size()!=(1<<n))
		{	f(i,0,s.size())
			if(s[i]=='S')
			{	if(s.size()*2>=(1<<(n-1)))
				{t.pb('P');	t.pb('S');}
				else
				{	t.pb('S');t.pb('P');}
			}
			else if(s[i]=='R')
			{	if(s.size()==(1<<(n-1)))
				{t.pb('R'); t.pb('S');}
				else
				{t.pb('S'); t.pb('R');}
			}
			else
			{	t.pb('P'); t.pb('R');}
			s.clear();
			s=t;
			t.clear();
		}
		cout<<s<<endl;
	}
}


