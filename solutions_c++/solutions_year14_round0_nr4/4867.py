#include <stdio.h>

struct Test 
{
	int blockNum;
	double N[10],K[10];
};
void quicksort(double a[],int left,int right)
{
	double temp;
	int i,j;
	i=left;
	j=right;
	temp=a[left];
	if(left>right)
		return;
	while(i!=j)
	{
		while(a[j]>=temp&&j>i)
			j--;
		if(j>i)
			a[i++]=a[j];
		while(a[i]<=temp&&j>i)
			i++;
		if(j>i)
			a[j--]=a[i];

	}
	a[i]=temp;
	quicksort(a,left,i-1);
	quicksort(a,i+1,right);
}
void moveList(double a[],int num)
{
	for (int i=num-1;i>0;i--)
	{
		a[i] = a[i-1];
	}
}
int main()
{
	int T;
	double C,F,X;
	scanf("%d",&T);
	Test test[50];
	int result[50][2]={0};
	int j=0,i=0,m=0,o=0;
	for(j=0;j<T;j++)
	{
		scanf("%d",&test[j].blockNum);
		for (i=0;i<test[j].blockNum;i++)
		{
			scanf("%lf",&test[j].N[i]);
		}
		for (i=0;i<test[j].blockNum;i++)
		{
			scanf("%lf",&test[j].K[i]);
		}
		quicksort(test[j].N,0,test[j].blockNum-1);
		quicksort(test[j].K,0,test[j].blockNum-1);
		int rek = 0, ren = 0;
		for (i=0,m=0;i<test[j].blockNum;i++)
		{
			for (;m<test[j].blockNum;m++)
			{
				if (test[j].N[i] < test[j].K[m])
				{
					rek++;
					m++;
					break;
				}
			}
			if (m >= test[j].blockNum)break;
		}
		result[j][1] = test[j].blockNum -rek;
		rek = 0;
		for (i=0;i<test[j].blockNum;i++)
		{
			if (test[j].N[i] < test[j].K[i])
			{
				rek++;
				moveList(test[j].K,test[j].blockNum);
			}else
			{
				ren++;
			}
		}
		result[j][0] = ren;
		
	}
	for(j=0;j<T;j++)
	{
		printf("Case #%d: %d %d\n",j+1,result[j][0],result[j][1]);
	}

	getchar();
	getchar();
	return 0;
}
