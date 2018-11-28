#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int main()
{

	int t;
	
	int row1,row2;
	FILE* fin;
	fin= fopen("A-small-attempt2.in","r");
	FILE* fout;
	fout= fopen("output2.txt","w");
	vector <int> v1;
	vector <int> v2;
	int num1,num2,num3,num4;
	int inp,flag , temp;
	fscanf(fin,"%d",&t);

	for(int k=1; k<=t;k++)
	{
		flag=0;
		fscanf(fin,"%d",&row1);
		v1.clear();
		v2.clear();
		
		for(int i=0; i<4;i++)
		{
			fscanf(fin,"%d %d %d %d",&num1,&num2,&num3,&num4);
			if(i+1==row1)
			{
				v1.push_back(num1);
				v1.push_back(num2);
				v1.push_back(num3);
				v1.push_back(num4);
			}
		}

		// for(int m=0 ; m<v1.size();m++)
		// {
		// 	cout<<v1[m]<<" ";
		// }
		// cout<<"\n";

		fscanf(fin,"%d",&row2);

		for(int i=0; i<4;i++)
		{
			fscanf(fin,"%d %d %d %d",&num1,&num2,&num3,&num4);
			if(i+1==row2)
			{
				v2.push_back(num1);
				v2.push_back(num2);
				v2.push_back(num3);
				v2.push_back(num4);
			}
		}
		
		// for(int m=0 ; m<v2.size();m++)
		// {
		// 	cout<<v2[m]<<" ";
		// }
		// cout<<"\n";

		
		for(int i=0; i<4;i++)
		{	for(int j=0; j<4;j++)
			{
				if(v1[i]==v2[j])
				{
					if(flag==0)
					{
						flag=1;
						temp = v1[i];
					}

					else if(flag==1)
					{
						flag=2;
					}
				}
			}

		}

			if(flag==0)
			{
				fprintf(fout,"Case #%d: %s\n",k,"Volunteer cheated!");
			}
			if(flag==1)
			{
				fprintf(fout,"Case #%d: %d\n",k,temp);
			}
			if(flag==2)
			{
				fprintf(fout,"Case #%d: %s\n",k,"Bad magician!");
			}

	}

	return 0;
}