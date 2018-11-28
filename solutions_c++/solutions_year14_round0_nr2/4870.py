#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef long long ll;  
#define FOR(i,n) for (int i = 0; i < n; i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define split(str) {vs.clear();istringstream ss(str);while(ss>>(str))vs.push_back(str);}
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	FOR(case1, t)
	{
		double C, F, X;
		cin >> C >> F >> X;

		double ans = 1000000000.0;
		double timeval = 0;
		double rate = 2.0;
		FOR(i, 2*X)
		{
			double local = timeval + X/rate;
			if(ans > local)
				ans = local;
			timeval += C/rate;
			rate += F;
		}
		cout << "Case #" << (case1 + 1) << ": ";
		printf("%.7lf\n", ans);
	}
}