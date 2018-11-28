#include <stdio.h>
#include <iostream>
using namespace std;

int arr[4][4];
int brr[4][4];
int main(void)
{

	int test;
	int i, j, k;
	scanf("%d", &test);

	for(k=1; k<=test; k++)
	{
		int first, second;
		int much=0;
		int result;
		scanf("%d", &first);

		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				scanf("%d", &arr[i][j]);
			}
		}
		
		scanf("%d", &second);

		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
				scanf("%d", &brr[i][j]);
		}
		//input end

		for(i=0; i<4; i++)
		{
			int num=arr[first-1][i];
			for(j=0; j<4; j++)
			{
				if(brr[second-1][j]==num)
				{
					much++;
					result=num;
					break;
				}
			}
		}

		if(much==1)
			cout<<"Case #"<<k<<": "<<result<<endl;
		else if(much==0)
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<k<<": Bad magician!"<<endl;


	}
	return 0;
}