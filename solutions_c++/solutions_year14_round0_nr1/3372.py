#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include<cstdlib>
using namespace std;
#define eps 1e-10
#define maxn 100010
#define pi acos(-1.0)
int g[4][4];
int g2[4][4];
int a[20];
int main(){
	int t;
	freopen("A-small-attempt8.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	int kase = 0;
	while (t--){
		memset(a, 0, sizeof(a));
		int p;
		scanf("%d", &p);
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &g[i][j]);
		for (int j = 0; j < 4; j++)a[g[p - 1][j]]++;
		scanf("%d", &p);
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &g[i][j]);
		for (int j = 0; j < 4; j++)a[g[p - 1][j]]++;
		int cnt = 0;
		int pos = -1;
		for (int i = 1; i <= 16; i++)
		if (a[i] == 2){
			pos = i; cnt++;
		}
		printf("Case #%d: ", ++kase);
		if (cnt == 0)printf("Volunteer cheated!\n");
		if (cnt >= 2)printf("Bad magician!\n");
		if (cnt == 1)printf("%d\n", pos);

	}
	return 0;
}