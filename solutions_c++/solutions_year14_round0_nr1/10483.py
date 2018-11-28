// magic_trick.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("a.out");
int magic_trick(int[4][4],int[4][4],int ,int);
int main()
{
	int i,j;
	int count=0;
	int count1=0;
	int a[4][4];
	int b[4][4];
	int k=0;
	int noOfCases;
	int firstans;
	int secondans;
	fin>>noOfCases;
	
	while(k<noOfCases)
	{
	fin>>firstans;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			fin>>a[i][j];
			//cout<<a[i][j];
		}
	}
	fin>>secondans;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			fin>>b[i][j];
			//cout<<b[i][j];
		}
	}
	fout<<"Case #";
	fout<<k+1;
	fout<<": ";
	k++;
	int result=magic_trick(a,b,firstans,secondans);
	//cout<<result;
	if(result==-1)
		fout<<"Bad magician!"<<endl;
	 else if(result==0)
			fout<<"Volunteer cheated!"<<endl;
	else
			fout<<result<<endl;	 
	}
	return 0;
}
int magic_trick(int a[4][4],int b[4][4],int first,int second)
{
	int i,j,count=0;
	int c;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(a[first-1][i]==b[second-1][j])
			{
				
				c=a[first-1][i];
				count++;
				//cout<<count;
			}
			if(count>=2)
			{
				return -1;
				
			}
			
		}
	}
	if(count==0)
		return 0;
	else{
		//cout<<"ans"<<a[first-1][i];
		return c;
	}

}
	

