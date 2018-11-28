#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char map[101];
int pancake[101];
int d[101][101][2];
int len;
const int inf = 1e9;

int f(int left, int right, int upanddown, int *arr, int cnting)
{
	int panarr[101] = {};
	int panarr2[101] = {};
	memcpy(panarr, arr, sizeof(arr)* 101);
	memcpy(panarr2, arr, sizeof(arr)* 101);
	int cnt = 0;
	for (int i = 0; i < len; i++)
	{
		if (upanddown && panarr2[i] == 1) cnt++;
		if (!upanddown && panarr[i] == 1) cnt++;
	}
	if (cnt == len) return cnting;

	int &ret = d[left][right][upanddown];
	if (ret != -1) return ret;
	int p;
	for (p = left; p<len-1; p++)
	{
		if (panarr[p] != panarr[p+1]) break;
	}
	for (int i = left; i <= p; i++)
	{
		panarr[i] = 1 - panarr[i];
	}
	ret = f(left, p, 0, panarr, cnting +1);
	reverse(panarr2, panarr2 + len);
	ret = min(ret, f(left, len - 1, 1, panarr2 + len, cnting + 1));
	return ret;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("ouput.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		memset(map, 0, sizeof(map));
		memset(pancake, 0, sizeof(pancake));
		scanf("%s", map);
		len = strlen(map);
		for (int i = 0; i < len; i++)
		{
			if (map[i] == '+') pancake[i] = 1;
			else pancake[i] = 0;
		}
		memset(d, -1, sizeof(d));
		int res = f(0, 0, 0, pancake, 0);
		printf("Case #%d: ", T);
		printf("%d\n", res);
	}
}