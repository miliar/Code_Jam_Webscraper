#include <cmath>
#include <stdio.h>
#include <cstring>

bool yes[1005], vis[1005];
int num[1005];
bool is_pa(int x)
{
	char str[100] = {0};
	sprintf(str, "%d", x);
	int len = strlen(str);
	for(int i=0; i<len/2 +1; i++)
		if(str[i] != str[len-i-1])
			return 0;
	return 1;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int cas, st,ed, i;
	memset(yes, 0, sizeof(yes));
	memset(vis, 0, sizeof(vis));
	for(i=1; i<=1000; i++)
		vis[i] = is_pa(i);
	for(i=1; i<=1000; i++)
	{
		double tmp = sqrt(i);
		if(vis[i] && tmp == (int)tmp && vis[(int)tmp])
			yes[i] = 1;
	}
    num[0] = 0;
	for(i=1; i<=1000; i++)
		num[i] = num[i-1] + yes[i];
	scanf("%d", &cas);
	for(int z=1; z<=cas; z++)
	{
		scanf("%d %d", &st, &ed);
		printf("Case #%d: %d\n", z, num[ed] - num[st-1]);
	}
 	return 0; 

}