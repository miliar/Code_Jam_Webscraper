
#include <iostream>
#include <list>
#include <memory.h>

int arr[52][52];
int count[2504];
int lost[54];

int main(int argc, char** argv) {
	int i,j,k,max,min,temp;
	int test,T,N,cnt;
	freopen("C:\\Users\\raju\\Documents\\input.in","r",stdin);
	freopen("C:\\Users\\raju\\Documents\\out.txt","w+",stdout);
	scanf("%d\n",&T);
	for(test=1;test<=T;test++)
	{
		
		memset(arr,0x00,sizeof(arr) );
		memset(count,0x00,sizeof(count));
		memset(lost,0x00,sizeof(lost));
		max =0;
		min=2508;
		cnt =0;
		scanf("%d",&N);
		for(i=1;i<=2*N-1;i++)
		{
			for(j=1;j<=N;j++)
			{
				scanf("%d",&arr[i][j]);
				count[arr[i][j]]++;
				
				if(arr[i][j] < min)
				{
					min = arr[i][j];
				}
				if(arr[i][j] > max)
				{
					max=arr[i][j];
				}
			}
		}
		
		for(i=min;i<=max;i++)
		{
			if(count[i] % 2 != 0)
			{
			    lost[cnt]= i;
				cnt++;	
			}
		}
		
		for(i=0;i < cnt;i++)
		{
			for(j=0;j<cnt-1;j++)
			{
				if(lost[j] > lost[j+1])
				{
					temp = lost[j+1];
					lost[j+1]=lost[j];
					lost[j]=temp;
				}
			}
		}
		printf("Case #%d:",test);
		for(i=0;i < cnt;i++)
		{
			printf(" %d",lost[i]);	
		}
		printf("\n");
		
	}//test
	return 0;
}

	
