#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int lawn[100][100];
int maxH[100];
int maxV[100];

bool check(int n, int m)
{
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		{
			if(lawn[i][j] < maxH[i] && lawn[i][j] < maxV[j])
			{
				//cerr << i << " " << j << " " << lawn[i][j] << " " << maxV[i] << " " << maxH[j] << endl;
				return false;
			}
		}
		
	return true;
}

int main()
{
	ifstream fin("b-l.in");
	//ifstream fin("in.txt");
	ofstream fout("b-l.out");
	
	int t;
	fin >> t;
	
	for(int s = 0; s < t; s++)
	{
		for(int i = 0; i < 100; i++)
		{
			maxV[i] = 0;
			maxH[i] = 0;
		}
		
		int n, m;
		fin >> n >> m;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
			{
				int num;
				fin >> num;
				lawn[i][j] = num;
				maxH[i] = max(maxH[i], num);
				maxV[j] = max(maxV[j], num);
			}
		fout << "Case #" << s+1 << ": ";
		if(check(n, m))
			fout << "YES" << endl;
		else
			fout << "NO" << endl;
	}
	
	return 0;
	
}
