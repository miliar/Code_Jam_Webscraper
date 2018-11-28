#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<utility>
#include<set>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cmath>
#include<cctype>


#define pb push_back
#define mp make_pair
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define ren(i,a,b) for(int i=a;i>=b;i--)
#define ff first
#define ss second
#define pll pair<long long int,long long int>
#define pii pair<int,int>
#define vll vector<long long int>  
#define vii vector<int>
#define gi(n) scanf("%d",&n)
#define gll(n) scanf("%lld",&n)
#define gstr(n) scanf("%s",n)
#define gl(n) cin >> n
#define oi(n) printf("%d",n)
#define oll(n) printf("%lld",n)
#define ostr(n) printf("%s",n)
#define ol(n) cout << n
#define os cout<<" "
#define on cout<<"\n"
#define o2(a,b) cout<<a<<" "<<b
#define all(n) n.begin(),n.end()
#define present(s,x) (s.find(x) != s.end()) 
#define cpresent(s,x) (find(all(s),x) != s.end()) 
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
using namespace std;
 
typedef unsigned long long int ull;
typedef long long int ll;
typedef vector<vector<ll> > mat;



bool ok(string s)
{
	int n=s.length();
	for(int i=0;i<n;i+=2)
	if(s[i]==s[i+1])
	return false;
	if(n==2)
	return true;
	string a;
	for(int i=0;i<n;i+=2)
	{
		if((s[i]=='P'&&s[i+1]=='R')||(s[i]=='R'&&s[i+1]=='P'))
		a+='P';
		else if((s[i]=='S'&&s[i+1]=='R')||(s[i]=='R'&&s[i+1]=='S'))
		a+='R';
		else if((s[i]=='P'&&s[i+1]=='S')||(s[i]=='S'&&s[i+1]=='P'))
		a+='S';
	}
	return ok(a);
}

int main()
{ios_base::sync_with_stdio(false);
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,t1=0;
gl(t);
while(t--)
{
	set<string> dp[15];
	t1++;
	ol("Case #");ol(t1);ol(": ");
	int n,r,p,s;
	cin>>n>>r>>p>>s;
	if(r>0&&p>0)dp[1].insert("PR");	if(r>0&&s>0)dp[1].insert("RS");	if(p>0&&s>0)dp[1].insert("PS");
	
	rep(i,2,n)
	{
		tr(dp[i-1],it)
		{
			tr(dp[i-1],it1)
			{
				string s1=*it+*it1;
				int a=0,b=0,c=0;
				rep(j,0,s1.length()-1)
				{
					if(s1[j]=='R')a++;
					if(s1[j]=='P')b++;
					if(s1[j]=='S')c++;
				}
				if(a<=r&&b<=p&&c<=s)
				{
					if(ok(s1))
					dp[i].insert(s1);
				}
			}
		}
	}
	if(dp[n].size()>0)
	{
		ol(*dp[n].begin());on;
	}	
	else
	{
		ol("IMPOSSIBLE\n");
	}
}
return 0;
}
