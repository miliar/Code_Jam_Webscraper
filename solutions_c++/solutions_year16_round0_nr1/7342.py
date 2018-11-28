#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int a;
	fin>>a;
	for(int i=0;i<a;i++)
	{
		int b;
		int j=1;
		int array[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
		fin>>b;
		int d;
		while(true)
		{
		int num=j*b;
		 d=num;
		 j++;
		if(num==0)
		{
			fout<<"case #"<<i+1<<": INSOMNIA\n";
			break;
		}	
		while(num!=0)
		{
			int c=num%10;
			num/=10;
			if(array[c]!=c)
			array[c]=c;		
		}
		int h=0;
		for(int z=0;z<10;z++)
		{
			if(array[z]!=-1)
			h++;
		}
		if(h==10)
		{
			fout<<"case #"<<i+1<<": "<<d<<"\n";
			break;
		}
		
		}
		
	}
	
}
