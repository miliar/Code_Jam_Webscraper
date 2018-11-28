#include<iostream>
#include<string>
#include<fstream>
#include<conio.h>
using namespace std;
int main()
{
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
	int cases;
	fin>>cases;
	int i=0;
	int max;
	string str;
	int *arr;
	
	while(i<cases)
	{
		int ppl=0;
		fin>>max;
		fin>>str;
		arr = new int[max+1];
		for(int i=0;i<=max;i++)
		{
			arr[i]=str[i]-'0';
		}
		int sum=0;
		for(int i=0;i<=max;i++)
		{
			sum = sum + arr[i];
			while(sum-1<i)
			{
				sum++;
				ppl++;
			}
		}
		delete [] arr;
		fout<<"Case #"<<i+1<<": "<<ppl<<endl;
		i++;
	}
	system("pause");
	return 0;
}