#include <cstdio>
#include <cstring>
int c1[4], c2[4];
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("PA.out", "w", stdout);
	int TN, i, j, x=1, y, r1, r2;
	scanf("%d", &TN);
	while(TN--){
		scanf("%d", &r1);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				if(r1==i+1)scanf("%d", &c1[j]);
				else scanf("%*d");

			}
		scanf("%d", &r2);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				if(r2==i+1)scanf("%d", &c2[j]);
				else scanf("%*d");

			}
		y=-1;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(c1[i]==c2[j]){
					if(y==-1)y=c1[i];
					else y=0;
				}

			}
		}
		printf("Case #%d: ", x++);
		if(y==-1)puts("Volunteer cheated!");
		else if(y==0)puts("Bad magician!");
		else printf("%d\n", y);


	}
	return 0;
}