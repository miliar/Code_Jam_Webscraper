#include<stdio.h>
#include<iostream>

using namespace std;
int arr[5];
int arr2[5];

int main()
{
	freopen("a-small-attempt0.in", "rt", stdin);
	freopen("a-small.out", "wt", stdout);

	int inp;
	int i, j, a1, a2, kase, tmp;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d", &a1);
		for(i = 1; i <=4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				scanf("%d", &tmp);
				if(i == a1)
					arr[j] = tmp;
			}
		}
		scanf("%d", &a2);
		for(i = 1; i <=4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				scanf("%d", &tmp);
				if(i == a2)
					arr2[j] = tmp;
			}
		}
		int fa = -1;
		int cnt = 0;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				if(arr[i] == arr2[j])
				{
					fa = arr[i];
					cnt++;
				}
			}
		}
		printf("Case #%d: ", kase);
		if(cnt == 0)
		{
			printf("Volunteer cheated!\n");
		}
		else if(cnt > 1)
		{
			printf("Bad magician!\n");
		}
		else
		{
			printf("%d\n", fa);
		}
	}
	return 0;
}