#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <string.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

using namespace std;

typedef set<int> SetInt;

int main(int argc, char** argv) {
	int casen = 0;
	ifstream ifile;
	ofstream ofile;
	//ifile.open("sample.txt");
	ifile.open("B-large.in");
	//ifile.open("A-large.in");
	ofile.open("output.txt");
	ifile >> casen;
	for (int c=0; c<casen; c++)
	{
		SetInt hs;
		int n, m;
		ifile >> n;
		ifile >> m;
		int a[n][m];
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
			{
				int h;
				ifile >> a[i][j];
				hs.insert(a[i][j]);
				cout << int(a[i][j]);
			}
			cout << endl;
		}
		//sort(hs.begin(), hs.end(), hs);
		int invalid = 0;
		for (SetInt::iterator it=hs.begin();it!=hs.end();it++)
		{
			//cout << *it << ",";
			for (int i=0;i<n&&invalid==0;i++)
			{
				for (int j=0;j<m&&invalid==0;j++)
				{
					int invalid1 = 0;
					int invalid2 = 0;
					for (int k=0;k<m&&invalid==0;k++)
					{
						if (a[i][k]>a[i][j]) invalid1 = 1;
					}
					for (int k=0;k<n&&invalid==0;k++)
					{
						if (a[k][j]>a[i][j]) invalid2 = 1;
					}
					if (invalid1&&invalid2) invalid = 1;
				}
			}
		}
		//cout << invalid;
		//cout << endl;
		
		string msg = "YES";
		if (invalid) msg = "NO";
		cout << "Case #" << c+1 << ": " << msg << endl;
		ofile << "Case #" << c+1 << ": " << msg << endl;
	}
	ifile.close();
	ofile.close();
	return 0;
}
