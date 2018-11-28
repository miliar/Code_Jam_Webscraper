#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;
int main()
{

	int T;
	int arr[4][4];
	int R1=0;
	int R2=0;
	int arr1[4]={0};
	int sol = 0;
	int sol_found=0;
	int j,k;
	//stdbuf("input_file.txt","r");
	cin >> T;
	for(int i=0;i<T;i++)
	{
		sol=0;
		sol_found=0;
		cin >> R1;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin >> arr[j][k];
			}
		}
		for(int l=0; l<4;l++)
		{
			arr1[l]=arr[R1-1][l];
		}
		//scanf("%d",&R2);
		cin >> R2;
		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				//scanf("%d",&arr[m][n]);
				cin >> arr[m][n];
			}
		}

		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(arr1[j]==arr[R2-1][k])
				{
					if(sol_found==0)
					{
						sol=arr1[j];
						sol_found=1;
					}
					else 
						{
						sol_found =2;
						break;
					}
				}
				
			}
			if(sol_found==2)
					break;
		}
		if(sol_found==1)
			printf("Case #%d: %d\n",i+1,sol);
		else if(sol_found==0)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else
			printf("Case #%d: Bad magician!\n",i+1);
	}

	return 0;
}