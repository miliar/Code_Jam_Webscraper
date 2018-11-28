#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;
struct node
{
	int val,key;
};
int compare(const void *a,const void *b)
{
	struct node *A=(struct node*)a;
	struct node *B=(struct node*)b;
	
	if(A->val<=B->val)return 1;
	else return -1;
}
int main()
{
	int n,i,t,test,in,count;
	scanf("%d",&test);
	
	for(t=1;t<=test;t++)
	{
		scanf("%d",&n);
		struct node arr[27];
		for(i=1;i<=26;i++)
		{
			arr[i].val=arr[i].key=0;
		}
		count=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&in);
			arr[i].val=in;
			count+=in;
			arr[i].key=i;
		}
		int num;
		int done;
		printf("Case #%d: ",t);
		while(count!=0)
		{
			qsort(arr+1,n,sizeof(struct node),compare);
			done=1;
			num=(count-2)/2;
			num++;
			if(done&&arr[1].val>=2)
			{	
				if(arr[2].val<num)
				{
					arr[1].val-=2;
					count-=2;
					done=0;
					printf("%c%c ",'A'+arr[1].key-1,'A'+arr[1].key-1);
				}
			}
			if(done)
			{
				if(n>2)
				{
					if(arr[3].val<num)
					{
						arr[1].val--;
						arr[2].val--;
						count-=2;
						done=0;
						printf("%c%c ",'A'+arr[1].key-1,'A'+arr[2].key-1);
					}
				}
				else if(n==2&&arr[1].val==arr[2].val)
				{
					arr[1].val--;
					arr[2].val--;
					count-=2;
					done=0;
					printf("%c%c ",'A'+arr[1].key-1,'A'+arr[2].key-1);
				}
			}
			
			if(done)
			{
				arr[1].val--;
				count--;
				printf("%c ",'A'+arr[1].key-1);
			}
		}
		printf("\n");
	}
	return 0;
}
