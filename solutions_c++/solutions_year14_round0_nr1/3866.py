#include <iostream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>

using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
typedef pair<int,ll> pil;

void test(int TC)
{
	printf("Case #%d: ", TC);

	vector<int> good;

	rep(i, 0, 2)
	{
		int cgr;
		scanf("%d", &cgr);
		cgr--;

		rep(i, 0, 4)
		{
			rep(j, 0, 4)
			{
				int cc;
				scanf("%d", &cc);
				if (i == cgr)
				{
					good.push_back(cc);
				}
			}
		}
	}

	sort(all(good));

	int gn = -1;

	rep(i, 0, good.size() - 1)
	{
		if (good[i] == good[i+1])
		{
			if (gn != -1)
				gn = -2;
			else
				gn = good[i];
		}
	}

	if (gn >= 0)
	{
		printf("%d\n", gn);
	}
	else if (gn == -1)
	{
		printf("Volunteer cheated!\n");
	}
	else
	{
		printf("Bad magician!\n");
	}
}

void run()
{
	int tc;
	scanf("%d", &tc);

	rep(i, 1, tc + 1)
	{
		test(i);
	}
}

//#define prob "fence"

int main()
{
#ifdef LOCAL_DEBUG
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    time_t st=clock();
#else 
#ifdef prob
    freopen(prob".in","r",stdin);
    freopen(prob".out","w",stdout);
#endif
#endif

    run();

#ifdef LOCAL_DEBUG
    fprintf(stderr, "\n=============\n");
    fprintf(stderr, "Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif
    
    return 0;
}