#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;

const int N = 200;

int f[N][2];//0:+
char st[N];
int T, n;

inline bool check(int t){
	return (st[t] == '+');
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
	{
		scanf("%s", st);
		n = strlen(st);
		//initialize
		f[0][0] = 1 - check(0);
		f[0][1] = 1 - f[0][0];
		//dp
		for (int i = 1; i < n; i ++)
		{
			if (check(i)){
				f[i][0] = f[i-1][0];
				f[i][1] = f[i-1][0] + 1;
			} else {
				f[i][1] = f[i-1][1];
				f[i][0] = f[i-1][1] + 1;
			}
		//	printf("%d,%d\n",f[i][0], f[i][1]);
		}
		printf("Case #%d: %d\n", t, f[n-1][0]);
	}
	return 0;
}
