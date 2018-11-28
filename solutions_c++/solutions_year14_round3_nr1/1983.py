#include <iostream>
#include <fstream>
#include <math.h> 
using namespace std;
void sort(char ** arr,int size)
{
	char x[1000];
	int i=0;
	for (i=0;i<size-1;i++)
	{
		for(int j=i;j<size;j++)
			if(strlen (arr[i])>strlen(arr[j]))
			{
				strcpy(x,arr[i]);
				strcpy(arr[i],arr[j]);
				strcpy(arr[j],x);
			}
	}
}

int main()
{
	int size,N;
	int flips;
	int index1,index2;
	double x,y,z;
	char input1;
	int x1;
	double check;
	int answer;
	bool flag;
	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin>>size;
	fin.get(input1);
	for(int i=0;i<size;i++)
	{	
		flag=true;
		x=0;
		x1=0;
		answer=-1;
		
		fin.get(input1);
		while(input1!='/')
		{
			x=x*10;
			input1=input1-'0';
			x=x+input1;
			fin.get(input1);
		}
		fin.get(input1);
		while(input1!=10&&!fin.eof())
		{
			x1=x1*10;
			input1=input1-'0';
			x1=x1+input1;
			fin.get(input1);
		}
		x=x/x1;

		check= x*(pow(2.0,40));
		check=fmod(check ,1);

		if(check!=0)
		{
			flag=false;
		}
		
		if(flag)
		{
			for(int j=0;j<40;j++)
			{
				if(x*(pow(2.0,j))-1>=0)
				{
					answer=j;
					break;
				}
			}
		}

		if (flag)
			fout<<"Case #"<<i+1<<": "<<answer<<endl;
		else
			fout<<"Case #"<<i+1<<": impossible"<<endl;
		
	
	}
	fin.close();
	fout.close();
	return 0;
	
}