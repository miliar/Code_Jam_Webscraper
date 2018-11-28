#include<iostream>
#include "conio.h"
#include<fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

void calc(char *arr,int Smax,int cse)
{
	int need=0,temp=0;
	if(Smax==0)
		need=0;
	else
	{
		int count=(arr[0]-48);
		for(int i=1;i<=Smax;i++)
		{
			if(arr[i]!='0')
			{
				if(count>=i)
					temp=0;
				else
				{
					temp=(i-count);
					need=need+temp;
				}
				count=count+temp+(((int)arr[i])-48);
			}
		}

	}
	fout<<"Case #"<<cse<<": "<<need<<endl;

}

int main()
{
	int total,Smax;
	char arr[1003];
	fin>>total;
	for(int i=0;i<total;i++)
	{
		fin>>Smax;
		for(int j=0;j<=Smax;j++)
			fin>>arr[j];
		calc(arr,Smax,i+1);
		
	}
	_getch();
	return 0;
}