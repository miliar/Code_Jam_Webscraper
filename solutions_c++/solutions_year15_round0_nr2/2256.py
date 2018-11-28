#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define N 1010
using namespace std;

int d[N];
int t, n, ys = 0;
bool cmp(const int& a, const int& b) { return a > b; }

bool check(int time, int special)
{
	int eat = time - special;
	for (int i=0;i<n;++i)
	{
		if (d[i] > eat)
		{
			int use = (d[i] + eat - 1) / eat - 1;
			special -= use;
			if (special < 0) return false;
		}
		else
			break;
	}

	return true;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("dataB-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			scanf("%d",&d[i]);
		sort(d,d+n,cmp);

		int ans = N;
		bool flag = false;
		for (int i=1;i<=d[0]&&!flag;++i)
		{
			for (int j=0;j<i&&!flag;++j)
				if (check(i, j))
				{
					ans = i;
					flag = true;
				}
		}

		printf("Case #%d: %d\n", ++ys, ans);
	}

	return 0;
}

