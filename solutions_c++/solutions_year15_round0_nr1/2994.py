#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


ifstream lire("large.in", ios::in);
ofstream ecrire("out.txt", ios::out);

int main()
{
	int T;
	lire >> T;
	for (int t = 1; t <= T; t++)
	{
		int Smax;
		lire >> Smax;
		string S;
		lire >> S;
		int a = 0, s = 0;
		for (int k = 0; k <= Smax; k++)
		{
			if (k > a)
			{
				s++;
				a++;
			}
			a += S[k] - '0';
		}
		ecrire << "Case #" << t << ": " << s << endl;
	}
	return 0;
}
