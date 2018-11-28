#include<iostream>
#include <fstream>
#include<string>

using namespace std;
int main()
{
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int c=0; c<t; c++)
	{
	string input;
	int max;
	int invite=0;
	fin >> max >> input;
	for(int i=1; i<max+1; i++)
	{
		int sum=0;
		for(int j=0; j<i; j++)
		{
			if(sum<i)
			{
				sum+=input[j]-'0';
			}
			else
				break;
		}
		if(sum < i)
		{
			input[0]+=i-sum;
			invite+=i-sum;
		}
	}
	fout<<"Case"<<" "<<'#'<<c+1<<':'<< " "<< invite << endl;
	}

}