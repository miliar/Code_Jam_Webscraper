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

vector<string> input;

bool checkWon(string str)
{
	int i=0,j=0;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(input[i][j] != str[0])
				break;
		}
		if(j==4)
			return true;
	}
	
	for(j=0;j<4;j++)
	{
		for(i=0;i<4;i++)
		{
			if(input[i][j] != str[0])
				break;
		}
		if(i==4)
			return true;
	}
	
	i=0;j=0;
	while(i<4 && input[i][j] == str[0])
		i++,j++;
	if(i==4)
		return true;
	
	i =0; j=3;
	while(i<4 && input[i][j] == str[0])
		i++,j--;
	if(i==4)
		return true;
	
	return false;
}

int main()
{
	int t;
	s(t);
	for(int tt = 1; tt<=t; tt++)
	{
		int iT=-1,jT=-1;
		bool period = false;
		input.clear();
		REP(i,4)
		{
			string str;
			cin >> str;
			REP(j,4)
			{
				if(str[j]=='T')
				{
					iT = i;
					jT = j;
				}
				else if(str[j]=='.')
					period = true;
			}
			input.pb(str);
		}
		if(iT!=-1)
			input[iT][jT] = 'X';
		string ans ="";
		if(checkWon("X"))
			ans = "X won";
		else
		{
			if(iT!=-1)
				input[iT][jT] = 'O';
			if(checkWon("O"))
				ans = "O won";
			else if(period)
				ans = "Game has not completed";
			else
				ans = "Draw";
		}
		cout << "Case #"<< tt <<": "<< ans << endl;
	}
	return 0;
}

