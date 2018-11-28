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

int n;
double a[1024], b[1024];

void init()
{
    cin >> n;

    f(i,1,n)
    {
        cin >> a[i-1];
    }
    f(i,1,n)
    {
        cin >> b[i-1];
    }

    sort(a,a+n);
    sort(b,b+n);

//    f(i,0,n-1)
//        cout << a[i] << " ";
//    cout << endl;
//    f(i,0,n-1)
//        cout << b[i] << " ";
//    cout << endl;
}

void solve(int testIndex)
{
    cout << "Case #" << testIndex << ": ";

    // War
    int cnt1 = 0;
    int p1 = n-1, p2 = n-1;

    while (p1 >= 0)
    {
        if (a[p1] < b[p2])
        {
            p1--;
            p2--;
        }
        else
        {
            cnt1++;
            p1--;
        }
    }

    // Deceitful war

    int cnt2 = 0;
    p1=0, p2=0;

    while (p1 < n)
    {
        if (a[p1] > b[p2])
        {
            p1++;
            p2++;
            cnt2++;
        }
        else
        {
            p1++;
        }
    }

    cout << cnt2 << " " << cnt1 << endl;
}

int main()
{
//	input("test.txt");
    input("D-large.in");
    output("D-large.out");

	int numberOfTests = 1;
	cin >> numberOfTests;

	f(i,1,numberOfTests)
	{
		init();
		solve(i);
	}

	return 0;
}
