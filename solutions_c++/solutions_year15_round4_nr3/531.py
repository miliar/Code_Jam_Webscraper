#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 4010, maxm = 201, maxs = 20010;
int t, n, m, equ[maxn], ans;
long long e[maxn >> 2], f[maxn >> 2], h[maxm][maxn / maxm], que[maxn];
char str[maxs];
int main()
{
	scanf("%d", &t);
	for(int Case = 1; Case <= t; ++Case)
	{
		n = 0;
		ans = 0x3f3f3f3f;
		scanf("%d\n", &m);
		m -= 2;
		gets(str);
		e[0] = 0;
		for(int i = 0, j; str[i]; )
		{
			for( ; str[i] == ' '; ++i);
			for(j = i; str[j] != ' ' && str[j] != '\0'; ++j);
			long long tmp = 0;
			for( ; i < j; ++i)
				tmp = tmp * 27 + str[i] - 'a' + 1;
			e[++e[0]] = tmp;
			que[n++] = tmp;
		}
		gets(str);
		f[0] = 0;
		for(int i = 0, j; str[i]; )
		{
			for( ; str[i] == ' '; ++i);
			for(j = i; str[j] != ' ' && str[j] != '\0'; ++j);
			long long tmp = 0;
			for( ; i < j; ++i)
				tmp = tmp * 27 + str[i] - 'a' + 1;
			f[++f[0]] = tmp;
			que[n++] = tmp;
		}
		for(int k = 0; k < m; ++k)
		{
			gets(str);
			h[k][0] = 0;
			for(int i = 0, j; str[i]; )
			{
				for( ; str[i] == ' '; ++i);
				for(j = i; str[j] != ' ' && str[j] != '\0'; ++j);
				long long tmp = 0;
				for( ; i < j; ++i)
					tmp = tmp * 27 + str[i] - 'a' + 1;
				h[k][++h[k][0]] = tmp;
				que[n++] = tmp;
			}
		}
		sort(que, que + n);
		n = unique(que, que + n) - que;
		for(int i = 1; i <= e[0]; ++i)
			e[i] = lower_bound(que, que + n, e[i]) - que;
		for(int i = 1; i <= f[0]; ++i)
			f[i] = lower_bound(que, que + n, f[i]) - que;
		for(int k = 0; k < m; ++k)
			for(int i = 1; i <= h[k][0]; ++i)
				h[k][i] = lower_bound(que, que + n, h[k][i]) - que;
		for(int s = 0; s < 1 << m; ++s)
		{
			int cnt = 0;
			memset(equ, 0, sizeof equ);
			for(int i = 1; i <= e[0]; ++i)
				equ[e[i]] |= 1;
			for(int i = 1; i <= f[0]; ++i)
				equ[f[i]] |= 2;
			for(int k = 0; k < m; ++k)
				for(int i = 1; i <= h[k][0]; ++i)
					equ[h[k][i]] |= 1 << ((s >> k) & 1);
			for(int i = 0; i < n; ++i)
				if(equ[i] == 3)
					++cnt;
			if(ans > cnt)
				ans = cnt;
		}
		printf("Case #%d: %d\n", Case, ans);
	}
	return 0;
}
