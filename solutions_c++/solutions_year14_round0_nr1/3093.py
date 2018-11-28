#include<iostream>
#include<cstdio>
using namespace std;

int num,x,y,ca;
int a[10][10],b[10][10];
void init()
{
	scanf("%d",&num);
	while (num--)
	{
		scanf("%d",&x);
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++) scanf("%d",&a[i][j]);
		scanf("%d",&y);
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++) scanf("%d",&b[i][j]);

		int ans1=0, ans2=0;
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++)
				if (a[x][i]==b[y][j]) 
				{
					++ans1;
					ans2=a[x][i];
				}	
		printf("Case #%d: ",++ca);

		if (ans1==1) printf("%d\n",ans2); else 
		if (ans1>1) printf("Bad magician!\n"); else printf("Volunteer cheated!\n");

			
	}
}
int main()
{
	init();
	return 0;
}
