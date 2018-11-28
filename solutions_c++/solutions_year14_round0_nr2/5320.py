#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <ctime>
#include <sstream>
#include <fstream>
#include <bitset>
#include <iomanip>
#include <cassert>

using namespace std;

typedef long long int64;

#define mp make_pair
#define PII pair<int, int>
#define pb push_back
#define sz(X) ((int)((X).size()))

#define x first
#define y second

const double eps = 1e-8;

double C, F, X;

bool check(double mid)
{
    double time = mid, per = 2;
    while (time * per + eps < X)
    {
        time -= C / per;
        per += F;
        if (time - eps < 0) return false;
    }
    return true;
}

void work()
{
    cin >> C >> F >> X;
    double l = 0, r = X / 2;
    while (abs(l - r) > eps)
    {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    printf("%.7f\n", l);
}

int main()
{
	#ifdef LOCAL_TEST
		freopen("c.in","r",stdin);
		freopen("c.out","w",stdout);
	#endif
	int task;
	cin >> task;
	for (int i = 1; i <= task; ++i)
	{
	    cout << "Case #" << i << ": ";
	    work();
	}
	return 0;
}
