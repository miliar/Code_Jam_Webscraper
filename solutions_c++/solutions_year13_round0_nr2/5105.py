#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin>>T;
	for (int i=1;i<=T;++i)
	{
		int n,m;
		fin>>n;
		fin>>m;
		int arr[100][100] = {0};
		int rMax[100] = {0};
		int cMax[100] = {0};
		for(int j=0;j<n;++j)
			for(int k=0;k<m;++k)
				fin>>arr[j][k];
		bool result = true;
		for(int j=0;j<n;++j)
		{
			for(int k=0;k<m;++k)
			{
				if(rMax[j] < arr[j][k])
					rMax[j] = arr[j][k];
			}
		}

		for(int j=0;j<m;++j)
		{
			for(int k=0;k<n;++k)
			{
				if(cMax[j] < arr[k][j])
					cMax[j] = arr[k][j];
			}
		}

		for(int j=0;j<n;++j)
			for(int k=0;k<m;++k)
			{
				if(arr[j][k] < rMax[j] && arr[j][k] < cMax[k])
				{
					result = false;
					break;
				}
			}
		fout<<"Case #"<<i<<": "<<(result?"YES":"NO")<<endl;
	}
	fin.close();
	fout.close();
}
