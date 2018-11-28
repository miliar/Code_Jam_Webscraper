#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>

using namespace std;

#define s(n)					scanf("%d",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define pb						push_back
#define mp	 					make_pair
#define EPS						1e-9
#define fill(a,v) 				memset(a, v, sizeof(a))
#define SZ(v)					((int)(v.size()))
#define all(x)					x.begin(), x.end()
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())
#define FF						first
#define SS						second
#define T(t)           			int t;scanf ("%d",&t);while (t--)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define FOR(i,a,b)				for(int i=a;i<b;i++)
#define REP(i,n)				FOR(i,0,n)
#define debug(args...)			{dbg,args; cerr<<endl;}

struct debugger
{
	template<typename T> debugger& operator , (const T& v)
	{
		cerr<<v<<" ";
		return *this;
	}
} dbg;

void debugarr(int * arr,int n)
{
	cout<<"[";
	for(int i=0;i<n;i++)
		cout<<arr[i]<<" ";
	cout<<"]"<<endl;
}

void debugvec(vector <int> arr)
{
	cout<<"[";
	for(int i=0;i<SZ(arr);i++)
		cout<<arr[i]<<" ";
	cout<<"]"<<endl;
}

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef pair<double,double> PDD;

int main()
{
	int t;
	s(t);
	for(int tt=1; tt<=t; tt++)
	{
		int n,m,i,j;
		s(n); s(m);
		int mat[n][m];
		REP(i,n)
			REP(j,m)
				s(mat[i][j]);
		bool row[n], col[m];
		
		fill(row,false);
		fill(col,false);
		
		for(i=0;i<n;i++)
		{
			for(j=1;j<m;j++)
			{
				if(mat[i][j]!=mat[i][j-1])
					break;
			}
			if(j==m)
				row[i] = true;
		}
		
		for(j=0;j<m;j++)
		{
			for(i=1;i<n;i++)
			{
				if(mat[i][j]!=mat[i-1][j])
					break;
			}
			if(i==n)
				col[j] = true;
		}
		bool pos = true;
		for(i=0;i<n && pos;i++)
		{
			int num = -1;
			int maxCol = -1;
			for(j=0;j<m && pos;j++)
			{
				if(!col[j])
				{
					if(num==-1 || num == mat[i][j])
						num = mat[i][j];
					else
						pos = false;
				}
				else
				{
					maxCol = maX(maxCol, mat[i][j]);
				}
			}
			if(pos && num!=-1 && maxCol>num)
				pos = false;
		}
		cout << "Case #" << tt << ": "<< (pos ? "YES" : "NO") << endl;
	}
	return 0;
}

