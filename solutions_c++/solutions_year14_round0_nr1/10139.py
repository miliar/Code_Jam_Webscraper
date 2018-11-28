#include<iostream>
#include<fstream>
using namespace std;

ifstream in("input.txt",ios::in);
ofstream out("output.txt",ios::out);

void solve()
{
	int arr1[4][4], arr2[4][4];
	int rowA,rowB;
		in>>rowA;
		for(int j=0 ; j<4 ; j++)
			for(int k=0 ; k<4 ; k++)
				in>>arr1[j][k];
		in>>rowB;
		for(int j=0 ; j<4 ; j++)
			for(int k=0 ; k<4 ; k++)
				in>>arr2[j][k];
	int match;
	bool oneMatch=false;
	bool moreThanOne=false;
	for(int i=0 ; i<4 ; i++)
	{
		for(int j=0 ; j<4 ; j++)
		{
			if(arr1[rowA-1][i]==arr2[rowB-1][j])
			{
				if(!oneMatch)
				{
					oneMatch=true;
					match=arr1[rowA-1][i];
				}
				else
				{
					moreThanOne=true;
				}
			}
		}
	}
	if(!oneMatch)
	{
		out<<"Volunteer cheated!\n";
	}
	else if(moreThanOne)
	{
		out<<"Bad magician!\n";
	}
	else
	{
		out<<match<<endl;
	}
}

void main()
{
	int total;
	in>>total;
	for(int i=0 ; i<total ; i++)
	{
		out<<"Case #"<<i+1<<": ";
		solve();
	}
}