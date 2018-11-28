#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("OUT.out");
	int T;
	in >> T;
	string S;
	for (int i = 0; i < T; ++i)
	{
		int q = 0;
		in >> S;
		string copy("");
		while (true)
		{
			while (S.size() > 0 && S.back() == '+')
			{
				S.pop_back();
			}
			if (S.size() == 0)
				break;
			if (S[0] == '+')
				reverse(S.begin(), S.end());
			/*if (S.size() == 2 && S[0] == '+' && S[1] == '-')
			{
				q += 2;
				break;
			}*/
			if (copy == S)
			{
				if (S.back() == '+')
					q += S.size() - 2;
				else
					q += S.size() - 1;
				break;
			}
			copy = S;
			reverse(S.begin(), S.end());
			++q;
			for (int j = 0; j < S.size(); ++j)
			{
				if (S[j] == '-')
					S[j] = '+';
				else
					S[j] = '-';
			}
		}
		out << "Case #" << i + 1 << ": " << q << endl;
	}
}