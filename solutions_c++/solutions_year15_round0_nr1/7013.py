#include <iostream>
#include <vector>
#include <assert.h>
#include <fstream>

using namespace std;

ifstream in("A.in");
ofstream out("A.out");

void read_line(int& Smax, vector<char>& Ss)
{
	in >> Smax;
	in.ignore(1);
	Ss.resize(Smax + 1);
	for (int i = 0; i < Smax + 1; ++i)
		Ss[i] = in.get() - '0';
}

int main()
{
	
	int T;
	in >> T;

	for (int i = 0; i < T; ++i)
	{
		int Smax;
		vector<char> Ss;
		read_line(Smax, Ss);

		int acc = Ss.front();
		int needed = 0;
		for (int s = 1; s < Smax + 1; ++s)
		{
			if (Ss[s] > 0 && s > acc)
			{
				needed += s - acc;
				acc += s - acc;
			}
			acc += Ss[s];
		}
		
		out << "Case #" << i + 1 << ": " << needed << endl;
	}

	return 0;
}