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
bool more(vector<pair<int, char> > V)
{
	for(int i=0;i<V.size();i++)
	{
		if(V[i].X>0)
			return true;
	}
	return false;
}
int main()
{
	
	int t;
	cin>>t;
	int tc=0;
	while(t--)
	{
		tc++;
		int n;
		cin>>n;
		vector<pair<int, char> > V;
		for(int i=0;i<n;i++)
		{
			int num;
			cin>>num;
			V.push_back(MP(num, 'A'+ i));
		}
		sort(V.begin(),V.end());
		cout<<"Case #"<<tc<<": ";
		while(more(V))
		{
			cout<<V[V.size()-1].Y;
			V[V.size()-1].X--;
			int prev = V.size()-2;
			int third= V.size()-3;
			if(V[prev].X>0 && ((third<0)|| V[third].X< V[prev].X))
			{
				cout<<V[prev].Y;
				V[prev].X--;
			}
			cout<<" ";
			
			sort(V.begin(),V.end());
		}
		cout<<endl;
	}



	return 0;
}
