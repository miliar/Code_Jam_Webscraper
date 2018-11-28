#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <sstream>
using namespace std;
typedef long long LL;
#define VI vector<int>
#define SIZE(A) ((int)A.size())
#define ALL(a) a.begin(),a.end()
#define LEN(A) ((int)A.length())
#define MS(A) memset(A,0,sizeof(A))
#define MAX(a,b) ((a>=b)?(a):(b))
#define MIN(a,b) ((a>=b)?(b):(a))
#define II pair<int,int>
#define MP make_pair
#define X first
#define Y second
#define PB push_back
#define FOUND(A,x) (A.find(x)!=A.end())
#define TRACE(x) cerr << #x << " : " << x << endl
#define _ << " " <<

#define INF (int(1e9))
#define INFL (LL(1e18))

//int dx[] = {-1,0,1,0}, dy[] = {0,1,0,-1};
//int dx[] = {1,1,1,0,0,-1,-1,-1}, dy[] = {1,0,-1,1,-1,1,0,-1};

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, a, n) for(int i = a; i < n; i++)
#define REV(i, a, n) for(int i = a; i > n; i--)
#define FORALL(it,A) for(it=A.begin(); it!=A.end();it++)
#define DEB(n) cout<<"(<<< DEBUG "<<n<<" >>>)"<<endl;
int main()
{
	int t;
	cin>>t;
	int tc=0;
	while(t--)
	{
		tc++;
		string s;
		cin>>s;
		reverse(s.begin(),s.end());
		int ans=0;
		int sz=s.size(),i=0;
		while(i<sz && s[i]=='+')
			i++;
		for(;i<sz;i++)
		{
			if(i==0)
			{
				ans++;
			}
			else if(s[i]==s[i-1])
			{
			}
			else if(s[i]!=s[i-1])
				ans++;
		}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}


	return 0;
}

