#include<iostream>
#include<cstdio>

void test(int);

int main()
{
	int t,i=1;
	scanf("%d",&t);
	while(t--)
	{
		test(i);
		i++;
	}
	return 0;
}

void test(int num)
{
	int arr1[4][4],arr2[4][4],magic[4],ctr=0,pos;
	int c1,c2,i,j;
	scanf("%d",&c1);
	for(i=0 ; i<4 ; i++)
	{
		for(j=0 ; j<4 ; j++)
		{
			scanf("%d",&arr1[i][j]);
			if(i==c1-1)
				magic[j]=arr1[i][j];
		}

	}
	scanf("%d",&c2);
	for(i=0 ; i<4 ; i++)
	{
		for(j=0 ; j<4 ; j++)
			scanf("%d",&arr2[i][j]);
	}
	for(i=0 ; i<4 ; i++)
	{
		for(j=0 ; j<4 ; j++)
		{
			if(magic[i]==arr2[c2-1][j])
			{
				ctr++;
				pos=i;
			}
		}
	}
	if(ctr==1)
		printf("Case #%d: %d\n",num,magic[pos]);
	else if(ctr==0)
		printf("Case #%d: Volunteer cheated!\n",num);
	else
		printf("Case #%d: Bad magician!\n",num);
}