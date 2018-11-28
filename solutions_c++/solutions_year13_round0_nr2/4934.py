#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main(void)
{
	ifstream ifs;
	ifs.open("B-large.in",ios_base::in);
	ofstream ofs;
	ofs.open("B-large.out",ios_base::trunc);
	int T;
	ifs>>T;

	for(int caseNo=1;caseNo<=T;caseNo++)
	{
		int M,N;
		ifs>>N>>M;
		int*rowOffset=new int[N];
		int*columnOffset=new int[M];
		int*elements=new int[M*N];
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				ifs>>elements[i*M+j];
		for(int i=0;i<M;i++)
			columnOffset[i]=0;
		for(int i=0;i<N;i++)
			rowOffset[i]=0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				if(elements[i*M+j]>rowOffset[i])
					rowOffset[i]=elements[i*M+j];
				if(elements[i*M+j]>columnOffset[j])
					columnOffset[j]=elements[i*M+j];
			}
		}
		bool possible=true;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				if(elements[i*M+j]!=min(rowOffset[i],columnOffset[j]))
				{
					possible=false;
					break;
				}
			}
			if(!possible)
				break;
		}
		if(possible)
			ofs<<"Case #"<<caseNo<<": YES"<<endl;
		else
			ofs<<"Case #"<<caseNo<<": NO"<<endl;
	}
}