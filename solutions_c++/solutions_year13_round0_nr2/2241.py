#include <iostream>
#include <fstream>
using namespace std;
int Matrix[200][200];
int M,N;
unsigned int Test_Cases;


void read_test_cases(void);

void Check(unsigned int);


main()
{
	read_test_cases();
	return 0;
}

void read_test_cases(void)
{
	ifstream fin("A.in");
	fin >> Test_Cases ;
	unsigned int Number_of_iterations;
	int i,j;
	for(Number_of_iterations=0;Number_of_iterations<Test_Cases;Number_of_iterations++)
	{
		fin>>M;
		fin>>N;
		for(i=0;i<M;i++)
		{
			for(j=0;j<N;j++)
			{
				fin >>Matrix[i][j];
			}
		}
		Check(Number_of_iterations+1);
	}
}

void Check(unsigned int Case)
{
		
		int Row_NO,Col_NO;
		int i,j,k;
		int current;
		for(i=0;i<M;i++)
		{
			for(j=0;j<N;j++)
			{
				current=Matrix[i][j];
				Row_NO=1;
				Col_NO=1;
				for(k=0;k<M;k++)
				{
					if(current<Matrix[k][j]) 
					{
						k=M+2;
						Row_NO=0;				
					}	
				}
				if(Row_NO==0)
				{
					for(k=0;k<N;k++)
					{
						if(current<Matrix[i][k]) 
						{
							k=N+2;
							Col_NO=0;				
						}	
					}	
				}
				if(Col_NO==0)
				{
					cout<<"Case #"<<Case<<": NO\n";					
					return;
				}
				
			}
		}

		cout<<"Case #"<<Case<<": YES\n";
		return;

}		
