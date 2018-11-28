#include<cstdio>
#include<iostream>
using namespace std;

#define fin(a) fscanf(input,"%d",&a)

int main()
{
	FILE *input,*output;
	input = fopen("A-small.in","r");
	output = fopen("output.txt","w");
	int t,z;
	fin(t);
	for (z=0;z<t;z++)
	{
		int ans1,ans2,arr1[4],arr2[4],garb,count=0,out=0,k;
		fin(ans1);
		int i,j;
		for (i=0;i<4;i++)
		{
			for (j=0;j<4;j++)
			{
				if (i!=ans1-1)
				{
					fin(garb);
				}
				else
				{
					fin(arr1[j]);
				}
			}
		}
		fin(ans2);
		for (i=0;i<4;i++)
		{
			for (j=0;j<4;j++)
			{
				if (i!=ans2-1)
				{
					fin(garb);
				}
				else
				{
					fin(arr2[j]);
					for (k=0;k<4;k++)
					{
						if ((arr2[j])==(arr1[k]))
						{
							count++;
							out=k;
						}
					}
				}
			}
		}
		if (count==0)
			fprintf(output,"Case #%d: Volunteer Cheated!\n",z+1);
		else if (count==1)
			fprintf(output,"Case #%d: %d\n",z+1,arr1[out]);
		else
			fprintf(output,"Case #%d: Bad Magician!\n",z+1);
	}
	return 0;
}
