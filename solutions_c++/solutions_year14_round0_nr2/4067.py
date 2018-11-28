#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <limits>
#include <string>
#include <vector>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

#define stop exit(0)
#define nc -1
#define eps 1e-10
#define inf 1000000000
#define mod 1000000007
#define mp make_pair

#define fill(array,value) memset(array,value,sizeof(array))
#define f(i,beg,end) for(int i=beg; i<=end; i++)
#define F(i,beg,end) for(int i=beg; i>=end; i--)
#define Max(a,b) ( (a>b)?a:b )
#define Min(a,b) ( (a<b)?a:b )
#define pi 3.1415926535897932384626433832
#define iread(var) scanf("%d",&var)
#define dread(var) scanf("%f",&var)
#define lread(var) scanf("%lld",&var)
#define input(name) freopen(name,"r",stdin)
#define output(name) freopen(name,"w",stdout)
typedef unsigned long long ull;
typedef unsigned int ui;
typedef long double ld;
typedef long long ll;

using namespace std;

double c, ff, x;

void init()
{
    cin >> c >> ff >> x;
}

void solve(int testIndex)
{
    double f0 = x / 2.0;
    double ans = f0;

    for(int n=0; ;n++)
    {
        double fn = f0 + (c-x)/(2+n*ff) + x/(2+n*ff+ff);
//        cout << n << " : " << fn << endl;
        if (fn - f0 > 0.0)
        {
            ans = f0;
            break;
        }
        f0 = fn;
    }

    printf("Case #%d: %.10f\n",testIndex,ans);
}

int main()
{
//	input("test.txt");
    input("B-large.in");
    output("B-large.out");

	int numberOfTests = 1;
	cin >> numberOfTests;

	f(i,1,numberOfTests)
	{
		init();
		solve(i);
	}

	return 0;
}
