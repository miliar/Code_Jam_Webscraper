#include<iostream>
#include<fstream>
#include<stdlib.h>

using namespace std;
int main()
{	int file;
	//file input
	ifstream ifile;
	ifile.open("A-small-attempt1.in");
	ifile>>file;
	//initialization
	int test;
	int i,j,k,x;
	//cin>>test;
	test=file;
	
	int *flag;
	flag=new int[test];
	int *op;
	op=new int[test];
	int **result;
	result=new int*[test];
	for(i=0;i<test;i++)
	{
		result[i]=new int[2];
	}
	
	
	int set[2][4][4];
	for(i=0;i<test;i++)
	{
		//input
		for(x=0;x<2;x++)		
		{	ifile>>file;
			result[i][x]=file;
			//cout<<result[i][x];
			for(j=0;j<4;j++)
			{
				for(k=0;k<4;k++)
				{
					ifile>>file;
					set[x][j][k]=file;
				}
			}	
		}
		
		//processing
		int temp1[4],temp2[4];
		for(k=0;k<4;k++)
		{
			temp1[k]=set[0][(result[i][0]-1)][k];
			//cout<<temp1[k]<<"\t"; 
			temp2[k]=set[1][(result[i][1]-1)][k];
			//cout<<temp2[k]<<"\t";
		}
		flag[i]=0;
		op[i]=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(temp1[j]==temp2[k])
				{
					flag[i]++;
					op[i]=temp1[j];
				}	
			}
		}
		
	}
	ofstream ofile;
	ofile.open("magician.output");
	for(i=0;i<test;i++)
	{
		ofile<<"Case #"<<(i+1)<<": ";
		switch(flag[i])
		{
			case 0: ofile<<"Volunteer cheated!";
				break;
			case 1 : ofile<<op[i];
					break;
			default: ofile<<"Bad magician!";
		}
		ofile<<"\n";
	}	
	
	ofile.close();
	ifile.close();		
	
	return 0;
}
