#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <functional>

#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(i,v) for(__typeof(v.begin()) i=v.begin();i!=v.end();++i)
#define ass(v) (v)||++*(int*)0;

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<double> VD;
typedef long long LL;

double data[20][1 << 20];
void solve(int N)
{
	double *ans = data[N - 1];
	ans[(1 << N) - 1] = 0.0;
	for (int s = (1 << N) - 2; s >= 0; --s)
	{
		double sum = 0.0;
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{
				int k = (i + j) % N;
				if ((s & (1 << k)) == 0)
				{
					sum += (N - j) + ans[s | (1 << k)];
					break;
				}
			}
		}
		ans[s] = sum / N;
	}
}

int main()
{
	for (int N = 1; N <= 20; ++N) solve(N);
//	for (int i = 0; i < 8; ++i)
//	{
//		printf("%d: %f\n", i, data[2][i]);
//	}
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		char str[1024];
		scanf("%s", str);
		int N = strlen(str);
		int S = 0;
		for (int i = 0; i < N; ++i)
		{
			if (str[i] == 'X') S |= (1 << i);
		}
		printf("Case #%d: %.15f\n", cs, data[N - 1][S]);
	}
	return 0;
}
