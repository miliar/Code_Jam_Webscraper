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

int t;
int smax;
string shyness;

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> t;
	for(int _t = 1; _t <= t; _t++)
	{
		cin >> smax >> shyness;
		
		int result = 0, sum = 0;
		for(int i = 0; i <= smax; i++)
		{
			int actValue = (shyness[i]-'0');
			if(actValue > 0 && sum < i)
			{
				int toAdd = i-sum;
				result += toAdd;
				sum += toAdd;
			}
			
			sum += actValue;
		}
		
		cout << "Case #" << _t << ": " << result << endl;	
	}
	return 0;
}


