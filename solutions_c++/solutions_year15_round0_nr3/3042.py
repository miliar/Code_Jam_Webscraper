#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int sum[11000];
int sum_rev[11000];
char st[11000];
int a[11000];
int mat[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int L, T, X;

int getToken(char ch)
{
	if (ch == '1')
		return 1;
	if (ch == 'i')
		return 2;
	if (ch == 'j')
		return 3;
	if (ch == 'k')
		return 4;
	return 0;
}

int Abs(int x)
{
	if (x < 0) return -x;
	return x;
}

int multi(int x, int y)
{
	int xx = Abs(x);
	int yy = Abs(y);
	int res = mat[xx][yy];
	int sign1 = xx / x;
	int sign2 = yy / y;
	res *= sign1 * sign2;
	return res;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);

	scanf("%d\n", &T);
	for (int ii=1;ii<=T;++ii)
	{
		printf("Case #%d: ", ii);
		scanf("%d %d\n", &L, &X);
		scanf("%s", st);
		for (int i=0;i<L*X;++i)
			a[i] = getToken(st[i % L]);
		sum[0] = a[0];
		for (int i=1;i<L*X;++i)
			sum[i] = multi(sum[i-1], a[i]);
		sum_rev[L*X-1] = a[L*X-1];
		for (int i=L*X-2;i>=0;--i)
			sum_rev[i] = multi(a[i], sum_rev[i+1]);
		bool flag = false;
		bool find = false;
		if (sum[0] == 2) flag = true;
		for (int i=1;i<=L*X-2;++i)
		{
			if (flag && sum[i] == 4 && sum_rev[i+1] == 4)
			{
				find = true;
				break;
			}
			if (sum[i] == 2) flag = true;
		}
		if (find)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}

	return 0;
}