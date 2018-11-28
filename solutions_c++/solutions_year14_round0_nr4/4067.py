#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
	int t,T = 1;
	scanf("%d",&t);
	while(t--)
	{
		int N,i,j=0,war_d = 0, war = 0;
		double arr_1[1005], arr_2[1005];
		printf("Case #%d: ",T++);
		scanf("%d",&N);
		for(i=0;i<N;i++)
			scanf("%lf",&arr_1[i]);
		for(i=0;i<N;i++)
			scanf("%lf",&arr_2[i]);
		sort(arr_1,arr_1+N);
		sort(arr_2,arr_2+N);
		/*for(i=0; i < N;i++)
			printf("%0.3lf ",arr_1[i]);
		printf("\n");
		for(i=0; i < N;i++)
			printf("%0.3lf ",arr_2[i]);*/
		for(j=0,i=0; i < N && j < N; i++)
		{
			if(arr_1[i] > arr_2[j])
			{
				j++;
				war_d++;
			}
		}
		for(war=0,i=0,j=0; i < N && j < N;)
		{
			if((arr_1[i] < arr_2[j]))
			{
				war++;
				i++;
				j++;
			}
			else
			{
				j++;
			}
		}
		war = N - war;
		printf("%d %d\n",war_d,war);
	}
	return 0;
}
