
#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<vector>

using namespace std;


int table[5][5] = {
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}
};


int getcal(int x, int y);
void makeStream(vector<int>& vec, string str, int L, int X);
bool check_ijk(vector<int>& vec);


int main(int agrc, char* agrv[])
{

	ifstream in("C-small-attempt3.in");
	ofstream out("C-small-attempt3.out");

	int testCase;
	in >> testCase;
	for (int t = 0; t < testCase; ++t)
	{
		int L, X;
		string str;
		vector<int> vec;
		in >> L >> X;
		in >> str;

		if (L*X < 3)
		{
			out << "Case #" << t + 1 << ": " << "NO" << endl;
			continue;
		}

		makeStream(vec, str, L, X);
		
		if (check_ijk(vec))
		{
			out << "Case #" << t + 1 << ": " << "YES" << endl;
		}
		else
		{
			out << "Case #" << t + 1 << ": " << "NO" << endl;
		}
		

	}

	in.close();
	out.close();

	return 0;
}

int getcal(int x, int y)
{
	int temp = 1;
	if (x < 0)
	{
		x = -x;
		temp *= -1;
	}
	if (y < 0)
	{
		y = -y;
		temp *= -1;
	}

	return temp * table[x][y];

}

void makeStream(vector<int>& vec, string str, int L, int X)
{
	for (int i = 0; i < X; ++i)
	{
		for (int k = 0; k < L; ++k)
		{
			if (strcmp(str.substr(k, 1).c_str(), "i") == 0)
			{
				vec.push_back(2);
			}
			else if (strcmp(str.substr(k, 1).c_str(), "j") == 0)
			{
				vec.push_back(3);
			}
			else if (strcmp(str.substr(k, 1).c_str(), "k") == 0)
			{
				vec.push_back(4);
			}
		}
	}
}

bool check_ijk(vector<int>& vec)
{
	int temp = 1;
	int temp2 = 1;
	bool b_i = false;
	bool b_j = false;
	bool b_k = false;

	for (int i = 0; i < vec.size(); ++i)
	{
		temp = getcal(temp, vec[i]);
		temp2 = getcal(temp2, vec[i]);
		if (!b_i && temp == 2)
		{
			temp = 1;
			b_i = true;
			continue;
		}
		if (!b_j && b_i && temp == 3)
		{
			temp = 1;
			b_j = true;
			continue;
		}

		if (i == vec.size() - 1 && b_j && temp == 4)
		{
			temp = 1;
			b_k = true;
			continue;
		}
	}

	if (b_k)
	{
		return true;
	}
	else
	{
		return false;
	}
}
