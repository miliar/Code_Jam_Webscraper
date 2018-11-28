#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;
int T,x,y,ans;
int f[20];
int a[10][10],b[10][10];
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1 ;t <= T; ++ t)
	{
		memset(f,0,sizeof(f));
		scanf("%d",&x);
		for(int i = 1; i <= 4; ++ i)
		for(int j = 1; j <= 4; ++ j)
		scanf("%d",&a[i][j]);
		for(int i = 1; i <= 4; ++ i)
			++f[a[x][i]];
		scanf("%d",&y);
		for(int i = 1; i <= 4; ++ i)
		for(int j = 1; j <= 4; ++ j)
		scanf("%d",&b[i][j]);
		for(int i = 1; i <= 4; ++ i)
			++f[b[y][i]];
		ans = 0;
		for(int i = 1; i <= 16; ++ i)
		if (f[i] == 2) ++ ans;
		printf("Case #%d: ",t);
		if (ans == 0)
			puts("Volunteer cheated!");
		if (ans > 1)
			puts("Bad magician!");
		if (ans == 1)
		{
			for(int i = 1; i <= 16; ++ i)
			if (f[i] == 2)
				printf("%d\n",i);
		}
	}
}
