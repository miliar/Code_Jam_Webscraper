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

int T, n;
LL res;

bool areAllDigits(bool* tab)
{
	REP(i, 10)
	{
		if(!tab[i])	
		{
			return false;
		}
	}
	
	return true;	
}

void insertDigits(bool* tab, int nr)
{
	while(nr > 0)
	{
		tab[nr%10] = true;
		nr /= 10;
	}
}

int main()
{
	scanf("%d", &T);
	FOR(t, 1, T)
	{
		scanf("%d", &n);
		
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		
		res = n;
		bool digits[10] = {0};	
		
		while(1)
		{
			insertDigits(digits, res);
			
			if(areAllDigits(digits))
			{
				printf("Case #%d: %lld\n", t, res);
				break;	
			}	
			
			res += n;
		}
	}
	return 0;
}


