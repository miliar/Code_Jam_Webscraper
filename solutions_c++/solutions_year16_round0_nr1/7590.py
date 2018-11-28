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
int mark(int *dig,int num)
{
	while(num)
	{
		dig[num%10]=1;
		num/=10;
	}
	for(int i=0;i<10;i++)
	{
		if(!dig[i])
			return 0;
	}
	return 1;
}
int main()
{
	int t;
	cin>>t;
	int tc=1;
	while(t--)
	{
		int i;
		cin>>i;
		if(i==0)
		{
			cout<<"Case #"<<tc++<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int dig[10];
		MS(dig);
		int fg=0;
		for(int j=1;j<1000;j++)
		{
			int num=j*i;
			if(mark(dig,num))
			{
				cout<<"Case #"<<tc++<<": "<<num<<endl;
				fg=1;
				break;
			}
		}
		if(!fg)
		{
			cout<<"Case #"<<tc++<<": "<<"INSOMNIA"<<endl;
		}
	}
	return 0;
}

