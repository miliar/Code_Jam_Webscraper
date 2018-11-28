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

inline ll gcd (ll a, ll b){ return (!b ? a : gcd (b, a % b)); }

int main()
{
	int notc;
	long double C,F,X;
	scanf("%d", &notc);
	FOR(tc, 1, notc)
	{
		scanf("%Lf %Lf %Lf", &C, &F, &X);
		long double time=0, normalTime, takeTime, cc=0, cr=2;
		
		while(true)
		{
			normalTime=(X-cc)/cr;
			takeTime=(C-cc)/cr + X/(cr+F);
			if (normalTime<=takeTime)
			{
				time+=normalTime;
				break;
			}
			else
			{
				time+=(C-cc)/cr;
				cr+=F;
				cc=0;
			}
		}
		printf("Case #%d: %.7Lf\n", tc, time);
				
	}	
	return 0;
}
