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

int t, q1, q2, a, c, r;
vector<int> line;

int main()
{
	scanf("%d", &t);
	FOR(k, 1, t)
	{
		c = 0;
		line.clear();
		
		scanf("%d", &q1);
		FOR(i, 1, 4)
		{
			FOR(j, 1, 4)
			{
				scanf("%d", &a);
				if(i == q1) line.push_back(a);
			}
		}
		sort(line.begin(), line.end());
		
		scanf("%d", &q2);
		FOR(i, 1, 4)
		{
			FOR(j, 1, 4)
			{
				scanf("%d", &a);
				if(i == q2 && binary_search(line.begin(), line.end(), a)) 
				{
					r = a;
					c++; 
				}
			}
		}
		
		if(!c) printf("Case #%d: Volunteer cheated!\n", k);
		else if(c == 1)	printf("Case #%d: %d\n", k, r);
		else printf("Case #%d: Bad magician!\n", k); 
	}
	//system("pause");
	return 0;
}

