#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>
using namespace std;

#ifdef _LOCAL_
#define LLD "%lld"
#else
#define LLD "%lld"
#endif

#define prev pppppppprev
#define next nnnnnnnnext

#ifdef _LOCAL_
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define DB1(x) cerr<<#x<<" = "<<(x)<<"\n"
#define DB2(x, y) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<"\n"
#define DB3(x, y, z) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<", "<<#z<<" = "<<(z)<<"\n"
#define DB4(x, y, z, w) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<", "<<#z<<" = "<<(z)<<", "<<#w<<" = "<<(w)<<"\n"
#define DB5(x, y, z, w, t) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<", "<<#z<<" = "<<(z)<<", "<<#w<<" = "<<(w)<<", "<<#t<<" = "<<(t)<<"\n"
#define DB6(x0, x1, x2, x3, x4, x5) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<"\n"
#define DB7(x0, x1, x2, x3, x4, x5, x6) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<", "<<#x6<<" = "<<(x6)<<"\n"
#define DB8(x0, x1, x2, x3, x4, x5, x6, x7) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<", "<<#x6<<" = "<<(x6)<<", "<<#x7<<" = "<<(x7)<<"\n"
#define DB9(x0, x1, x2, x3, x4, x5, x6, x7, x8) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<", "<<#x6<<" = "<<(x6)<<", "<<#x7<<" = "<<(x7)<<", "<<#x8<<" = "<<(x8)<<"\n"
#else
#define eprintf(...) static_cast<void>(0)
#define DB1(x) static_cast<void>(0)
#define DB2(x, y) static_cast<void>(0)
#define DB3(x, y, z) static_cast<void>(0)
#define DB4(x, y, z, w) static_cast<void>(0)
#define DB5(x, y, z, w, t) static_cast<void>(0)
#define DB6(x0, x1, x2, x3, x4, x5) static_cast<void>(0)
#define DB7(x0, x1, x2, x3, x4, x5, x6) static_cast<void>(0)
#define DB8(x0, x1, x2, x3, x4, x5, x6, x7) static_cast<void>(0)
#define DB9(x0, x1, x2, x3, x4, x5, x6, x7, x8) static_cast<void>(0)
#endif

#define rep(x,y,z) for (int x = (y), e##x = (z);x < e##x; x++)
typedef long long ll;
typedef pair<int,int> pii;

const int MAXD = 1000;
int P[MAXD];

void test(int tnum)
{
	int d, i;
	int ord, spec, tmp, ans = 1000;
	scanf("%d", &d);
	for(i = 0; i < d; ++i)
		scanf("%d", P + i);
	for(ord = 1; ord < ans; ++ord)
	{
		for(spec = i = 0; i < d; ++i)
			spec += (P[i] - 1)  / ord;
		tmp = ord + spec;
		if(tmp < ans)
			ans = tmp;
	}
	printf("Case #%d: %d\n", tnum, ans);
}

void run()
{
	int T;
	scanf("%d", &T);
	for(int tnum = 1; tnum <= T; ++tnum)
		test(tnum);
}

//#define file_name "barduck"

int main()
{
//#ifdef _LOCAL_
    if(freopen("input.txt", "r", stdin) == NULL)
    {
        printf("Can't open input.txt\n");
        return 0;
    }
    if(freopen("output.txt", "w", stdout) == NULL)
    {
        printf("Can't open output.txt\n");
        return 0;
    }
//#else
#ifdef file_name
    freopen(file_name".in", "r", stdin);
    freopen(file_name".out", "w", stdout);
#endif
//#endif
    run();
//#ifdef _LOCAL_
    //puts("================");
//#endif

    return 0;
}
