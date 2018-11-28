#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int i,j,k,T,A,B,K,count=0;
	ifstream fin("B-small-attempt0.IN");
	ofstream fout("output.txt");
	fin >> T;
	for (i = 0; i < T; i++)
	{
		fin >> A;
		fin >> B;
		fin >> K;
		for (j = 0; j < A; j++)
		{
			for (k = 0; k < B; k++)
			{
				if ((j&k) < K)
					++count;
			}
		}
		fout << "Case #" << i + 1 << ": "<<count<<endl;
		count = 0;
	}
	return 0;
}