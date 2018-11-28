#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <memory.h>
#include <map>
#define _USE_MATH_DEFINES
#include <cmath>
#include <list>
#include <fstream>
#include <time.h>
#include <iomanip>
#include <queue>
#include <stack>
#include <complex>
#include <assert.h>

using namespace std;

#define For(i,a,b,d) for (int i = (a); i != (b); i += d)
#define FORD(i,a,b) for (int i = (a); i >= b; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define REPD(i,n) for (int i = (n - 1); i >= 0; i--)
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(a) (a).begin(), (a).end()
#define CLR(a,x) memset(a,x,sizeof(a))
#define min(a,b) (((a) < (b)) ? (a) : (b))
#define max(a,b) (((a) > (b)) ? (a) : (b))
#define debug(x) cout << #x << "=" << x << endl;
#define Abs(a) (((a) < 0) ? (-(a)) : (a))
#define sqr(a) ((a)*(a))
#define pb push_back
#define mp make_pair
#define gc getchar_unlocked

typedef double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

const int Inf = 1000000000;
const int Mi = 1000000009;
const ld eps = 10e-8;
const ld PI = 2 * acos(0.0);
const ll InfLL = ll(Inf) * ll(Inf);

int main()
{
	int notc;
	scanf("%d", &notc);
	FOR(tc, 1, notc)
	{
		int a, b, count=0, ans1,ans2, finalans;
		vector<bool> c(17, false);
		scanf("%d", &ans1);
		REP(i, 4)
		{
			if (i==ans1-1)	{ REP(j,4) {	scanf("%d", &a); c[a]=true; } 	}
			else	{ REP(j,4)	scanf("%*d");	}
		}	
		scanf("%d", &ans2);
		REP(i, 4)
		{
			if (i==ans2-1)	{ REP(j,4) {	scanf("%d", &b); if (c[b]) {++count; finalans=b;} }	}
			else	{ REP(j,4)	scanf("%*d");	}
		}		
		
		if (count==1)
			printf("Case #%d: %d\n", tc, finalans);
		else if (count==0)
			printf("Case #%d: Volunteer cheated!\n", tc);
		else
			printf("Case #%d: Bad magician!\n", tc);
		
		
	}	
	return 0;
}
