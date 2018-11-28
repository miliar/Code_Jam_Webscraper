#include <cstdio>
#include <cstring>
int mark[17];
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++) {
		memset(mark, 0, sizeof(mark));
		int a1,a2;
		scanf("%d",&a1);
		for(int j = 1; j <=4; j++) {
			for(int k = 1; k <= 4; k++) {
				int temp;
				scanf("%d",&temp);
				if(j == a1)
				{
					mark[temp]++;
				}
			}
		}
		scanf("%d",&a2);
		for(int j = 1; j <=4; j++) {
			for(int k = 1; k <= 4; k++) {
				int temp;
				scanf("%d",&temp);
				if(j == a2)
				{
					mark[temp]++;
				}
			}
		}
		int sum = 0;
		int number = 0;
		for(int j = 1; j <= 16; j++) {
			if(mark[j] == 2) {
				sum++;
				number = j;
			}
		}
		printf("Case #%d: ",i);
		if(sum == 1)
			printf("%d\n",number);
		else if(sum > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}