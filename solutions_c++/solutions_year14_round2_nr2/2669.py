#include<iostream>
#include <fstream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	 int a=4,b=5,k=2;
	 ifstream fin("B-small-attempt0.in");
	 ofstream fout("B-small-attempt0.out");

	 int t=0;
	 fin>>t;
	 for (int l = 0; l < t; l++)
	 {
		 fin>>a>>b>>k;
		int count=0;
		 for (int i = 0; i < k; i++)
		 {
			 for (int q = 0; q < a; q++)
			 {
				 for (int w = 0; w < b; w++)
				 {
					 int z=q&w;
					 if( z==i )
					 {
						 count++;
					 }
				 }

			 }
		 }
		 fout<<"Case #"<<l+1<<": "<<count<<endl;
	 }


	/*

	ifstream fin("input.txt");
	int n;
	vector<string> strings;
	string temp;
	fin>>n;
	int n_string;
	for (int i=0;i<n;i++)
	{
	fin>>n_string;
	int k=n_string;
	while (k>0)
	{
	fin>>temp;
	strings.push_back(temp);
	k--;
	}

	for (int j=0;j<n_string;j++)
	{
	for (int k = 0; k < strings[j].length(); k++)
	{
	if (strings[j][k]==strings[j][k+1])
	{

	}
	}

	}
	}*/
}