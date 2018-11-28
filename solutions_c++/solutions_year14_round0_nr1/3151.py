#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>

int main()
{
	int t =0 , flag = 0,row1, row2, arr1[4][4], arr2[4][4],number=0;
	ifstream inf("input.txt");
	inf >> t;
	ofstream outf("output.txt");
for(int count = 0; count< t ; count++)
{
	flag=0;
	inf>>row1;
	//input for 1st array
	for (int i = 0; i<4; i++)
	{
		for(int j = 0 ; j<4 ; j++)
		{
			inf>>arr1[i][j];
			//cout<<arr1[i][j];
		}
	}
	inf>>row2;
	//input for 2nd array
	for (int i = 0; i<4; i++)
	{
		for(int j = 0 ; j<4 ; j++)
		{
			inf>>arr2[i][j];
		}
	}
	//magic check
	for (int i = 0; i<4; i++)
	{
		for(int j = 0 ; j<4 ; j++)
		{
			if(arr1[row1-1][i]==arr2[row2-1][j])
			{
				flag++;
				number = arr1[row1-1][i];
			}
		}
	}
	if(flag==1)
	  	outf<<"Case #"<<(count+1)<<": "<<number<<"\n";
	else if(flag >1)
		outf<<"Case #"<<(count+1)<<": Bad magician!\n";
	else if(flag==0)
		outf<<"Case #"<<(count+1)<<": Volunteer cheated!\n";
}
	return 0;
}