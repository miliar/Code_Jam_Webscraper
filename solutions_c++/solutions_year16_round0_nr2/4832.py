#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <ctime>
using namespace std;
#include <conio.h>


ifstream infile;
string STRING;
ofstream offile;
string pattern;

int arr [100];

void gethappycount(string pattern,int &count);
void flip(int index);

long  main()
{
	infile.open ("c:\\temp\\in.txt");
	offile.open("c:\\temp\\out3.txt");

	int testcases;
	infile >> testcases;
	

	for(int i=1;i<=testcases;i++)
	{
		//Init arry
		for(int ii=0;ii<=99;ii++)
			arr[ii]=-1;
		int count=0;
		infile >> pattern;
		gethappycount(pattern,count);
		
		cout<<"Case #"<<i<<": "<<count<<endl;
		offile << "Case #"<<i<<": "<<count<<"\n";	
				
	}
	
	getch();
	infile.close(); 
	offile.close();
	return 0;
}

void gethappycount(string pattern,int & count)
{
	int len = pattern.length();
	for(int i=1;i<=len;i++)
	{
		char check = pattern.at(i-1);
		if(check == '-')
			arr[i-1]=0;
		else
			arr[i-1]=1;
	}
	for(int j=0;j<len;j++)
	{
		if( (arr[j] == 0 && arr[j+1] ==1) || (arr[j] == 1 && arr[j+1] ==0) )
		{
			count++;
			flip(j);
		}
		else if((j+1) == len && arr[0] == 0)
		{
			count++;
			flip(j+1);
		}

	}	

}

void flip(int index)
{
	for(int k=0;k<=index;k++)
	{
		if(arr[k] == 0)
			arr[k]=1;
		else if(arr[k]== 1)
			arr[k]=0;
	}

}