#include <bits/stdc++.h>

using namespace std;

ifstream fin("A.in");
ofstream fout("output.out");

// #define fin cin
// #define fout cout

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	fin >> t;
	int u = 0;
	while (u++ < t)
	{
		string s;
		fin >> s;
		vector<int> vec(10), nums(10);
		int count = 0;
		for (int i = 0; i < s.size(); ++i)
		{
			count++;
			switch(s[i])
			{
				case 'Z':
					vec[0]++;
					break;
				case 'O':
					vec[1]++;
					break;
				case 'W':
					vec[2]++;
					break;
				case 'R':
					vec[3]++;
					break;
				case 'U':
					vec[4]++;
					break;
				case 'F':
					vec[5]++;
					break;
				case 'X':
					vec[6]++;
					break;
				case 'S':
					vec[7]++;
					break;
				case 'H':
					vec[8]++;
					break;
				case 'I':
					vec[9]++;
					break;
				default:
					count--;
					break;
			}
		}
		nums[0] += vec[0];
		vec[1] -= vec[0];
		vec[3] -= vec[0];
		nums[2] += vec[2];
		vec[1] -= vec[2];
		nums[6] += vec[6];
		vec[9] -= vec[6];
		vec[7] -= vec[6];
		nums[4] += vec[4];
		vec[5] -= vec[4];
		vec[1] -= vec[4];
		vec[3] -= vec[4];
		nums[1] += vec[1];
		nums[3] += vec[3];
		vec[8] -= vec[3];
		nums[8] += vec[8];
		vec[9] -= vec[8];
		nums[5] += vec[5];
		vec[9] -= vec[5];
		nums[7] += vec[7];
		nums[9] += vec[9];
		fout << "Case #" << u << ": ";
		for (int i = 0; i < nums.size(); ++i)
		{
			for (int j = 0; j < nums[i]; ++j)
			{
				fout << i;
			}
		}
		fout << endl;
	}	
	return 0;
}