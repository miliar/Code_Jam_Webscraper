#include<cstdio>
#include<iostream>

int main()
{
//	freopen("a.in", "r", stdin);
//	freopen("a.out", "w", stdout);
	int round;
	int s[10] = {1, 4, 9, 121, 484};
	int haha[1005];
	memset(haha, 0, sizeof(haha));
	int start = 0;
	for(int i = 0;i < 5;i++){
		for(int j = s[i]+1; j < 1005;j++)
		haha[j]++;
	}
	scanf("%d", &round);
	for(int i = 1;i <= round; i++){
		int low, high;
		scanf("%d", &low);
		scanf("%d", &high);
		printf("Case #%d: %d\n", i, haha[high+1]- haha[low]);
	}
	return 0;
}
