#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int solve(const int &Smax, const string &S)
{
	int y = 0;
	int cp = 0;
	cp += S.at(0) - '0';

	for (int i = 1; i <= Smax; i++)
	{
		if (S.at(i) == '0')
		{
			continue;
		}
		if (cp < i)
		{
			y += i - cp;
			cp += i - cp;
		}
		cp += S.at(i) - '0';
	}

	return y;
}

int main()
{
	ifstream in("A-large.in", ios::in);
	ofstream out("A-large.out", ios::out);

	int T;
	in >> T;

	for (int i = 1; i <= T; i++)
	{
		int Smax;
		string S;
		in >> Smax >> S;

		int y = solve(Smax, S);

		out << "Case #" << i << ": " << y << endl;
	}

	in.close();
	out.close();

	return 0;
}