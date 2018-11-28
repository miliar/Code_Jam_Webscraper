#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;

int main()
{
	ifstream infile("sampleB.in");
	streambuf* inStream_buf(cin.rdbuf());
	cin.rdbuf(infile.rdbuf());
	ofstream outfile("sampleB.out");
	streambuf* outStream_buf(cout.rdbuf());
	cout.rdbuf(outfile.rdbuf());
	int n,i,row,column,a,b,flag;
	int rowSum[20],columnSum[20],map[20][20];
	cin >> n;
	for (i = 0;i < n;++i)
	{
		flag = 1;
		cin >> a >> b;
		for (row = 0;row < a;++row)
		{
			for (column = 0;column < b;++column)
			{
				map[row][column] = 0;
			}
		}
		for (row = 0;row < a;++row) rowSum[row] = 0;
		for (column = 0;column < b;++column) columnSum[column] = 0;
		for (row = 0;row < a;++row)
		{
			for (column = 0;column < b;++column)
			{
				cin >> map[row][column];
				if (map[row][column] == 1)
				{
					rowSum[row] += (1 << column);
					columnSum[column] += (1 << row);
				} 
			}
		}
		for (row = 0;row < a;++row)
		{
			for (column = 0;column < b;++column)
			{
				if (map[row][column] == 1)
				{
					if ((rowSum[row] != ((1 << b) - 1)) && (columnSum[column] != ((1 << a) - 1))) 
					{
						flag = 0;
						break;
					}
				}
				if (!flag) break;
			}
			if (!flag) break;
		}
		if (flag) cout << "Case #" << i+1 << ": YES" << endl;
		else cout << "Case #" << i+1 << ": NO" << endl;
	}
	cin.rdbuf(inStream_buf);
	cout.rdbuf(outStream_buf);
	return 0;
}
