#include <iostream> 
#include <fstream> 
#include <string>
#include <unordered_map>
using namespace std;

// Problem C. Dijkstra

char mul(char a, char b, int& sign)
{
	if (a == b)
	{
		sign ^= 0x01;
		return '1';
	}
	if (a == '1')
		return b;
	if (b == '1')
		return a;
	switch (a)
	{
	case 'i':
		if (b == 'j')
			return 'k';
		else// 'k':
		{
			sign ^= 0x01;
			return 'j';
		}
	case 'j':
		if (b == 'i')
		{
			sign ^= 0x01;
			return 'k';
		}
		else // 'k'
			return 'i';
	case 'k':
		if (b == 'i')
			return 'j';
		else // 'j'
		{
			sign ^= 0x01;
			return 'i';
		}
	}
}

int main(int argc, char* argv[])
{
	ifstream in("C-small.in");
	ofstream out("C-small.out");
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		int L, X;
		in >> L >> X;
		string s;
		in >> s;
		char* target = "ijk1";
		char cur = '1';
		int sign = 0;
		while (X-- > 0)
		{
			for (int i = 0; i < s.length(); ++i)
			{
				cur = mul(cur, s[i], sign);
				if (cur == *target && sign == 0 && *target != '1')
				{
					cur = '1';
					++target;
				}
			}
		}
		string res = (*target == '1' && cur == '1' && sign == 0) ? "YES" : "NO";
		out << "Case #" << t << ": " <<  res << endl;
	}
	return 0;
}
