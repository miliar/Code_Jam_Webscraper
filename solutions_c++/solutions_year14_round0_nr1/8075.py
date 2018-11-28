#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("A-small-attempt4.in");

	ofstream f;
	f.open("n.txt");

	int x;
	infile >> x;

	for(int t = 0; t < x ; t++)
	{
		f << "Case #" << t + 1 << ": ";
	int r, r2;
	
	infile >> r;
	r--;

	vector<vector<int>> v;
	int n1, n2, n3, n4;

	v.resize(4);
	v[0].resize(4);
	v[1].resize(4);
	v[2].resize(4);
	v[3].resize(4);


	for(int y = 0; y < 4; y++)
	{
		infile >> n1 >> n2 >> n3 >> n4;
		v[0][y] = n1;
		v[1][y] = n2;
		v[2][y] = n3;
		v[3][y] = n4;
	}

	infile >> r2;
	r2--;

	vector<vector<int>> v2;

	v2.resize(4);
	v2[0].resize(4);
	v2[1].resize(4);
	v2[2].resize(4);
	v2[3].resize(4);

	for(int y = 0; y < 4; y++)
	{
		infile >> n1 >> n2 >> n3 >> n4;
		v2[0][y] = n1;
		v2[1][y] = n2;
		v2[2][y] = n3;
		v2[3][y] = n4;
	}

	int c = 0;
	int num = 0;

	for(int y = 0; y < 4; y++)
	{
		for(int n = 0; n < 4; n++)
	{
		if(v2[y][r2] == v[n][r])
		{
			num = v[n][r];
			c++;
		}
	}
	}

	if(c == 1)
	{
		f << num << endl;
	}
	else if(c > 1)
	{
		f << "Bad magician!" << endl;
	}
	else
	{
		f << "Volunteer cheated!" << endl;
	}
	

	}
	infile.close();
	f.close();
	

}

