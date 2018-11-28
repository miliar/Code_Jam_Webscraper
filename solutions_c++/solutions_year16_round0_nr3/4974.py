
//~        Author : Sarvesh Mahajan                             
//               IIIT,Hyderabad                                   
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ifndef ONLINE_JUDGE
#define DEBUG
#endif

#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define For(i,a,b) for(i=a;i<b;i++)
#define loop(i,b) for(i=0;i<b;i++)
#define Loop(i,b) for(i=1;i<=b;i++)
#define pi(n) cout<<n<<' '
#define si(n) cin>>n
#define int long long 
const int MOD=1e9+7;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef long long LL;
#define F first
#define S second
#define sz(x) (int) x.size()
#define pLL(x) cout<<x<<' '
#define fill(x,c) memset(x,c,sizeof(x))
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
inline void add(LL &x,LL y,int mod=MOD) { x+=y;if(x>=mod) x-=mod;}
inline void sub(LL &x,LL y,int mod=MOD) { x-=y;if(x<0) x+=mod;}
inline LL mult(LL x,LL y,int mod=MOD) { return (x*y)%mod;}
inline bool isset(int mask,int idx) { return (mask>>idx)&1;}
int expo(LL b,LL e,int mod=MOD) { LL ret=1;while(e) { if(e&1) ret=mult(ret,b,mod); b=mult(b,b,mod);e>>=1;} return ret;}

#ifdef DEBUG
#define DB(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
       cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
       const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define DB(...)
#endif








/*#ifdef DEBUG
#define DB(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DB2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DB3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#else
#define DB(x)
#define DB2(x,y)
#define DB3(x,y,z)
#endif
*/


string binary(int n)
{
	string ret="";
	while(n)
	{
		char ch=(n&1)+'0';
		ret+=ch;
		n/=2;
	}

	reverse(ret.begin(),ret.end());
	return ret;
}

int get(string s,int base)
{
	int ret=0;
	int curr=1;
	for(int i=s.size()-1;i>=0;--i)
	{
		ret+=curr*(s[i]-'0');
		curr*=base;
	}
	return ret;
}

int div(int n)
{
	for(int i=2;i*i<=n;++i)
	{
		if(n%i == 0)
			return i;
	}

	return 0;
}

int a[20];

#undef int
int main()
{
#define int long long
ios_base::sync_with_stdio(false);
int n,t,m,l,k,ans,i,j,res=0,fl;
t=1;
cin>>(t);
int T=t;
Loop(t,T)
{
	cout<<"Case #"<<t<<":\n";
	cin>>n>>m;
	int ct=0;
	for(i=(1<<n)-1;i>=0,ct<m;i-=2)
	{
		string s=binary(i);
		for(j=2;j<=10;++j)
		{
			int num=get(s,j);
//			if(j == 10) DB(i,num);
			int v=div(num);
			if(!v)
				break;
			else a[j]=v;
		}

		if(j>10)
		{
			ct++;
			cout<<s<<' ';

		        for(k=2;k<10;++k)
			cout<<a[k]<<' ';
		        cout<<a[10]<<'\n';
		}
			
	}

		

}
return 0;
}
