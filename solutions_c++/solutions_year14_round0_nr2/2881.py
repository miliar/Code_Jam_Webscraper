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

int t, j;
double x, c, f, res, res_last, sum; 

int main()
{
	ios_base::sync_with_stdio(0);
	cout.precision(7);
	cin >> t;
	FOR(i, 1, t)
	{
		cin >> c >> f >> x;
		
		sum = j = 0;
		res_last = x/2;
		REP(j, x+10)
		{
			//cout << "sum: " << sum << ", res_last: " << res_last << ", x/2:" << x/2 << endl;
			sum += c/(2+j*f);
			//cout << "sum: " << sum << endl;
			res = sum + x/(2+(j+1)*f);
			
			//cout << fixed << res << endl;
			
			if(res > res_last) break;
			res_last = res;
		}
		
		cout << "Case #" << i << ": " << fixed << res_last << endl;
	}
	//system("pause");
	return 0;
}

