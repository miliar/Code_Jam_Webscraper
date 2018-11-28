#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <cstring>
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

const int MAX_N = 1005;

int tc;
int res, min_res, n, max_pos, A[MAX_N], B[MAX_N], maxx, nextl, nextr;
map<int, int> pos;

/*void move_max(int pos)
{
	if(max_pos == pos) return;
	
	if(max_pos < pos)
	{
		int i = max_pos;
		while(i < pos) 
		{
			//cout << "1swap" << endl;
			swap(A[i], A[i+1]);
			i++;
			res++;
		}
	}
	else
	{
		int i = max_pos;
		while(i > pos) 
		{
			//cout << "swap" << endl;
			swap(A[i], A[i-1]);
			i--;
			res++;
		}	
	}
}

void sort_up(int end)
{
	if(end <= 0) return;
	
	for(int j = end; j > 0; j--)
	{
		bool p = 1;
	    for(int i = 0; i < j; i++)
	    {
	    	if(A[i] > A[i + 1])
	      	{
	        	swap(A[i], A[i + 1]);
	        	res++;
	        	p = 0;
	      	}
		}
		if(p) break;
	} 	
}

void sort_down(int start)
{
	if(start >= n-1) return;
	
	for(int j = n-1; j > start; j--)
	{
		bool p = 1;
		//cout << "j: " << j << endl;
	    for(int i = start; i < j; i++)
	    {
	    	//cout << A[i] << ' ' << A[i+1] << endl;
	    	if(A[i] < A[i + 1])
	      	{
	        	swap(A[i], A[i + 1]);
	        	res++;
	        	p = 0;
	      	}
		}
		if(p) break;
	} 	
}*/

void move(int from, int to)
{
	if(from == to) return;
	
	if(from < to)
	{
		int i = from;
		while(i < to)
		{
			swap(A[i], A[i+1]);
			pos[A[i]] = i;
			pos[A[i+1]] = i+1;
			res++;
			
			i++;
		}
	}
	else
	{
		int i = from;
		while(i > to)
		{
			swap(A[i], A[i-1]);
			pos[A[i]] = i;
			pos[A[i-1]] = i-1;
			res++;
			
			i--;
		}	
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> tc;
	FOR(t, 1, tc)
	{
		res = max_pos = maxx = 0;
		min_res = INF;
		
		cin >> n;
		nextl = 0; nextr = n-1;
		REP(i, n)
		{
			cin >> A[i];
			B[i] = A[i];
			pos[A[i]] = i;
			
			if(A[i] > maxx)
			{
				maxx = A[i];
				max_pos = i;
			}
		}
		
		sort(B, B+n);
		
		REP(i, n)
		{
			//cout << "B[i]: " << B[i] << ", pos: " << pos[B[i]] << ", koszt na lewo: " << abs(pos[B[i]] - nextl) << ", na prawo: " << abs(pos[B[i]] - nextr) << ", nextl: " << nextl << ", nextr: " << nextr << endl;
			if(abs(pos[B[i]] - nextl) <= abs(pos[B[i]] - nextr))	
			{
				move(pos[B[i]], nextl);
				nextl++;	
				//cout << "na lewo, res: " << res << endl;
			}
			else
			{
				move(pos[B[i]], nextr);
				nextr--;	
				//cout << "B[i]: " << B[i] << ", na prawo, res: " << res << endl;
			}
		}
		
		/*REP(i, n)
		{
			move_max(i);
			sort_up(i-1);
			sort_down(i+1);
			
			//cout << "i: " << i << endl;
			if(res < min_res)
			{
				//cout << "new min res: " << res << endl;
				min_res = res;
			}
			
			REP(j, n) A[j] = B[j];
			res = 0;
		}*/
		
		//cout << "max_pos: " << max_pos << endl;
		//REP(i, n) cout << A[i] << ' ';
		//cout << endl;
		
		cout << "Case #" << t << ": " << res << endl;
	}
	//system("pause");
	return 0;
}

