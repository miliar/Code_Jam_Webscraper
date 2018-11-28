#include <iostream>
#include <stdio.h>
using namespace std;
bool IsNotPossible=false;
int main()
{
	FILE* fin = fopen("B-large.in","r");
	FILE* fout = fopen("output.txt","w+");
	int number_of_cases=0;
	fscanf(fin,"%d",&number_of_cases);
	int N =0;
	int M =0;
	for(int ncase=0;ncase<number_of_cases;ncase++)
	{
		fscanf(fin,"%d",&M);
		fscanf(fin,"%d",&N);
		int* pattern = new int[N*M];
		for(int i =0;i<N*M;i++)
		{
			fscanf(fin,"%d",&pattern[i]);
		}
		IsNotPossible=false;
		for(int i =0;i<M;i++)
		{
			for(int j =0;j<N;j++)
			{
				//row wise check for pattern(i,j)
				bool higherR = true;
				for(int col = 0; col<N;col++)
				{
					if(pattern[i*N+col]>pattern[i*N+j])
					{
						higherR=false;
						break;
					}
				}

				//column wise check for pattern(i,i)
				bool higherC = true;
				for(int row = 0; row<M;row++)
				{
					if(pattern[row*N+j]>pattern[i*N+j])
					{
						higherC=false;
						break;
					}
				}
				if(higherC||higherR)			
				{
				}
				else
				{
					IsNotPossible=true;
				}

			}
			if(IsNotPossible==true)
			{
				fprintf(fout,"Case #%d: NO\n",ncase+1);
				break;
			}
		}	
		if(IsNotPossible==false)
		{
			fprintf(fout,"Case #%d: YES\n",ncase+1);
		}
	}

	return 0;
}