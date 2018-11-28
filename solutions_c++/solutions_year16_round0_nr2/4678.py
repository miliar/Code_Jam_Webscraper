#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<LD> VLD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000001;
const LD EPS = 10e-9;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define abs(a) ((a)<0 ? -(a) : (a))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

short setBit(int number, int pos, bool value)
{
	int mask = (value ? 1 : 0) << pos;
	int res = number&(~(1<<pos));
	return res|mask;
}

bool getBit(int number, int pos)
{
	int mask = 1<<pos;
	return number&mask;
}

int swapBits(int number, int pos1, int pos2)
{
	int res = number;
	res = setBit(number, pos1, getBit(number, pos2));
	res = setBit(res, pos2, getBit(number, pos1));
	
	return res;
}

int flipBits(int number, int startPos, int count)
{
	int endPos = startPos+count-1;
	int res = number;
	
	int s = startPos, e = endPos;
	while(s < e)
	{
		res = swapBits(res, s, e);
		s++;
		e--;
	}	
	
	FOR(i, startPos, endPos)
		res = res^(1<<i);
	
	return res;
}

int convertToInt(const string& s)
{
	int res = 0;
	REP(i, s.size())
	{
		if(s[i] == '+')
		{
			res |= 1;
		}
		
		if(i < s.size()-1)
		{
			res <<= 1;
		}
	}
	
	return res;
}

LL poww(LL x, int a)
{
	LL res = 1;
	while(a > 0)
	{
		if(a%2 == 1)
		{
			res *= x;	
		}
		
		x *= x;
		a /= 2;
	}
	
	return res;
}

vector<vector<int>> buildGraph(const string& s)
{
	int elems = 1<<(s.size());
	vector<vector<int>> res(elems);
	
	REP(i, elems)
	{
		FOR(j, 1, s.size())
		{
			res[i].push_back(flipBits(i, s.size()-j, j));
		}	
	}	
	
	return res;	
} 

const int MAX_V = 5000;

int T;
bool vis[MAX_V];
int dist[MAX_V];

int distance(const vector<vector<int>>& g, int start, int end)
{
	if(start == end)
	{
		return 0;
	}
	
	REP(i, g.size())
	{
		vis[i] = false;
	}
	
	queue<int> q;
	q.push(start);
	vis[start] = true;	
	dist[start] = 0;
	
	while(!q.empty())
	{
		int v = q.front();
		q.pop();
		
		FORE(it, g[v])
		{
			if(!vis[*it])
			{
				vis[*it] = true;
				dist[*it] = dist[v]+1;
				
				if(*it == end)
				{
					return dist[*it];
				}
				
				q.push(*it);
			}
		}
	}
	
	return dist[end];
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> T;
	FOR(t, 1, T)
	{
		string s;
		cin >> s;
		
		vector<vector<int>> g = buildGraph(s);
		
		/*REP(i, 1<<s.size())
		{
			cout << i << " => ";
			FORE(it, g[i])
			{
				cout << *it << " ";
			}
			cout << endl;
		}*/
		
		cout << "Case #" << t << ": " << distance(g, convertToInt(s), (1<<(s.size()))-1 ) << endl; 	
	}	
	
	return 0;
}


