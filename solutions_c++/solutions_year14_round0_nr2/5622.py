#include <ctime>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
using namespace std;


#define PB	push_back
#define MP  make_pair
#define ALL(a) 		(a).begin(), (a).end()
#define FILL(a,v) memset(a,v,sizeof(a))

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define SQR(x) (x)*(x)

const double PI = acos(-1.0);
const double EPS = 1e-7;

const int MOD = 1000000007;

typedef long long ll;


void solve()
{
	double c,f,x;
	cin >> c >> f >> x;
	int farmsCnt = 0;
	double speed = 2.0;
	double res = x / speed;
	double prevRes = res + 1000;
	double prevToFarm = 0;
	while(res < prevRes)
	{
		prevRes = res;
		++farmsCnt;
		res = prevToFarm;
		res += c / speed;
		speed += f;
		prevToFarm = res;
		res += x / speed;
	}
	printf("%.7f", prevRes);
}


int main()
{
	ios_base::sync_with_stdio(false);
	freopen( "input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cout << "Case #" << test << ": ";
		solve();
		cout << endl;
	}

	return 0;
} 
