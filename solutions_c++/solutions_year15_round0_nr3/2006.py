#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("output.txt");

// #define fin cin
// #define fout cout

int mTable[4][4] = 
{
	{1, 2, 3, 4},
	{2, -1, 4, -3},
	{3, -4, -1, 2},
	{4, 3, -2, -1}
};

struct Quaternion
{
	int val;
	bool neg;

	Quaternion() : val(1), neg(false) {}
};

inline Quaternion Multiply(const Quaternion& a, const Quaternion& b)
{
	Quaternion res;
	res.neg = (a.neg != b.neg);
	res.val = mTable[a.val - 1][b.val - 1];
	if(res.val < 0)
	{
		res.val *= -1;
		res.neg = !res.neg;
	}
	return res;
}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	fin>>t;
	int u = 0;
	while(u++ < t)
	{
		int l, x;
		fin>>l>>x;
		vector<Quaternion> vec(x * l), suffix(x * l);
		for (int i = 0; i < l; ++i)
		{
			char a;
			fin>>a;
			vec[i].val = (int)(a - 'i' + 2);
		}
		for (int i = 1; i < x; ++i)
		{
			for (int j = 0; j < l; ++j)
			{
				vec[j + i * l] = vec[j];
			}
		}
		for (int i = 0; i < x * l; ++i)
		{
			Quaternion one;
			for (int j = i; j < x * l; ++j)
			{
				one = Multiply(one, vec[j]);
			}
			suffix[i] = one;
		}
		bool possible = false;
		Quaternion one;
		for (int i = 0; i < x * l; ++i)
		{
			one = Multiply(one, vec[i]);
			if(one.val == 2 && !one.neg)
			{
				Quaternion two;
				for (int j = i + 1; j < x * l; ++j)
				{
					two = Multiply(two, vec[j]);
					if(two.val == 3 && !two.neg)
					{
						if(suffix[j + 1].val == 4 && !suffix[j + 1].neg)
						{
							possible = true;
							goto end;
						}
					}
				}
			}
		}
		end:;
		fout<<"Case #"<<u<<": ";
		possible ? fout<<"YES\n" : fout<<"NO\n";
	}
	return 0;
}