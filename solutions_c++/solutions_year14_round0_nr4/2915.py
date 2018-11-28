#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <iomanip>
using namespace std;


int main( int argc, char* argv[] ){

	ifstream is;
	is.open(argv[1],std::ifstream::in);

	ofstream os;
	os.open(argv[2],std::ofstream::out);

	int case_total;
	is>>case_total;
	int block_num;
	float min=LLONG_MAX;
	int del=0;
	int count=0;
	int count1=0;
	for(int i=0;i<case_total;i++)
	{	
		is>>block_num;
		count=0;
		count1=0;
		float *A = new float[block_num];
		float *B = new float[block_num];
		float *C = new float[block_num];
		float *D = new float[block_num];
		for(int j=0;j<block_num;j++)
			is>> A[j];
		for(int j=0;j<block_num;j++)
			is>> B[j];
		for(int j=0;j<block_num;j++)
			C[j]=A[j];
		for(int j=0;j<block_num;j++)
			D[j]=B[j];

		for(int j=0;j<block_num;j++)
		{
			min=LLONG_MAX;
			del=0;
			for(int k=0;k<block_num;k++)
			{
				if((C[k]-D[j])>0 && (C[k]-D[j])<min && C[k]!=-1)
				{
					min=C[k]-D[j];
					del=k;
				}
			}
			if(min!=LLONG_MAX)
				{
					C[del]=-1;
				}
		}	
		for(int j=0;j<block_num;j++)
		{
			if(C[j]==-1)
				count1++;
		}

		for(int j=0;j<block_num;j++)
		{
			min=LLONG_MAX;
			del=0;
			for(int k=0;k<block_num;k++)
			{
				if((B[k]-A[j])>0 && (B[k]-A[j])<min && B[k]!=-1)
				{
					min=B[k]-A[j];
					del=k;
				}
			}
			if(min!=LLONG_MAX)
				{
					B[del]=-1;
				}
		}	
		for(int j=0;j<block_num;j++)
		{
			if(B[j]!=-1)
				count++;
		}

		os<<"Case #"<< i+1 <<": "<<count1<<" "<<count<<endl;
		delete []A;
		delete []B;
		delete []C;
		delete []D;

	}
		
	is.close();
	os.close();


return 0;
}
