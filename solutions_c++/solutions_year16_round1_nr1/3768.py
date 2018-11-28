#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<numeric>
#include<queue>
#include<functional>
#include<set>
#include<unordered_map>
#include<deque>
using namespace std;

class Solution
{
public:
	string lastWord(istream& in)
	{
		string s;
		in >> s;
		string res;
		res.resize(2 * s.size());
		res[s.size()] = s[0];
		int start = s.size();
		int last = s.size();
		for (int idx = 1; idx < s.size(); ++idx)
		{
			if (s[idx] >= res[start])
			{
				--start;
				res[start] = s[idx];
			}
			else
			{
				++last;
				res[last] = s[idx];
			}
		}
		return res.substr(start, s.size());
	}
};

int main()
{
	//ifstream in("input.txt");
	//ofstream out("output.txt");
	istream& in = cin;
	ostream& out = cout;
	int T;
	in >> T;
	Solution A;
	for (int i = 1; i <= T; ++i)
	{
		out << "Case #" << i << ": ";
		out << A.lastWord(in) << endl;
	}
	return 0;
}