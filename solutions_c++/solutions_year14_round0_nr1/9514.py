#include<iostream>
#include<string>
#include<fstream>

using namespace std;

void main()
{
	int num;
	int test;
	int res;
	int first;
	int second;
	int arr[4];
	int arr1[4];
	int arr2[4];

	ofstream write("output.txt");
	ifstream read("A-small-attempt0.in");
	read>>test;
	for(int q=0;q<test;q++)
{	num=0;
	read>>first;
	for(int i=1;i<=4;i++)//iteration
	{
		if(i==first){
		for(int k=0;k<4;k++)
			{
				read>>arr[k];
			}}
		else
			{for(int l=0;l<4;l++)
			{
				read>>arr2[l];
			}}

	}
	read>>second;
	for(int i=1;i<=4;i++)//iteration
	{
		if(i==second){
		for(int k=0;k<4;k++)
		{
				read>>arr1[k];
		}}
		else
			{for(int l=0;l<4;l++)
			{
				read>>arr2[l];
			}}
	}
	
	for(int z=0;z<4;z++)
		{
			for(int a=0;a<4;a++)
				{
					if(arr[z]==arr1[a])
						{
							res=arr1[a];
							num++;
						}
				}
		}
		if(num==0)
			write<<"Case #"<<q+1<<": Volunteer cheated!\n";
		else if(num==1)
			write<<"Case #"<<q+1<<": "<<res<<"\n";
		else if(num>1)
			write<<"Case #"<<q+1<<": Bad magician!\n";
	}
	read.close();
	write.close();
}