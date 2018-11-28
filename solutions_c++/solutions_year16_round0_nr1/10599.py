#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;

bool check(bool arr[])
{
	for(int x=0;x<10;x++)
	{
		if(arr[x]==false)
			return false;
	}
	return true;
}

int main()
{
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	bool numbers[10]={false};
	int T;
	long long int N;
	fin>>T;
	for(int y=1 ; y<=T; y++)		//Test Cases
	{
		fin>>N;
		if(N==0)
		{
			fout<<"Case #"<<y<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		for(int i=1; ;i++)
		{
			long long int temp=i*N;
			while(temp!=0)
			{
				int digit=temp%10;
				numbers[digit]=true;
				temp/=10;
				//printf("%d ",digit);
			}
			if(check(numbers))
			{
				fout<<"Case #"<<y<<": "<<i*N<<endl;
				break;
			}
		}
		for(int x=0;x<10;x++)
			numbers[x]=false;
		
	}
	return 0;
}