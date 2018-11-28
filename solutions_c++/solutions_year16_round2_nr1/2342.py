#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");

	int T, t, i, alph[26], temp, a[10];
	string S;

	in >> T;

	t = 1;
	while (t <= T)
	{
		out << "Case #" << t << ": ";

		for (i = 0; i < 26; i++)
			alph[i] = 0;

		in >> S;

		for (i = 0; i < S.size(); i++)
			alph[S[i] - int('A')]++;

		a[0] = alph[int('Z') - int ('A')];
		a[2] = alph[int('W') - int ('A')];
		a[4] = alph[int('U') - int ('A')];
		a[6] = alph[int('X') - int ('A')];
		a[8] = alph[int('G') - int ('A')];

		a[1] = alph[int('O') - int ('A')] - a[0] - a[2] - a[4];
		a[3] = alph[int('H') - int ('A')] - a[8];
		a[5] = alph[int('F') - int ('A')] - a[4];
		a[7] = alph[int('S') - int ('A')] - a[6];
		a[9] = alph[int('I') - int ('A')] - a[5] - a[6] - a[8];
	
		for (i = 0; i <= 9; i++)
			while (a[i]--)
				out << i;
		
		out << endl;

		t++;
	}

	in.close();
	out.close();

	return 0;
}