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

const int MAX_N = 1050;

set<double> s_ken;
int t, n, s, e, res_w, res_dw;
double nao[MAX_N], ken[MAX_N];

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> t;
	FOR(c, 1, t)
	{
		cin >> n;
		
		s = res_w = res_dw = 0;
		e = n-1;
		s_ken.clear();
		
		REP(i, n) cin >> nao[i];
		REP(i, n) 
		{
			cin >> ken[i];
			s_ken.insert(ken[i]);
		}
		
		sort(nao, nao+n);
		sort(ken, ken+n);
		
		REP(i, n)
		{
			if(nao[i] > ken[s])
			{
				res_dw++;
				s++;
			}	
			else
			{
				e--;
			}
			
			set<double>::iterator it = s_ken.upper_bound(nao[i]);
			if(it == s_ken.end())
			{
				s_ken.erase(s_ken.begin());
				res_w++;
			}
			else s_ken.erase(it);
		}
		
		cout << "Case #" << c << ": " << res_dw << ' ' << res_w << endl;
	}
	//system("pause");
	return 0;
}

