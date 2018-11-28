#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in ("B-large.in");
	ofstream out ("B-large.out");

	int T, i, j, count;
	string S;

	in >> T;
	
	i = 1;
	while (i <= T)
	{
		out << "Case #" << i << ": ";

		in >> S;

		count = 0;
		j = 1;
		while (j < S.size())
		{
			if (S[j] != S[j - 1])
				count++;

			j++;
		}

		if (S[S.size() - 1] == '-')
			out << count + 1 << endl;
		else
			out << count << endl;

		i++;
	}

	in.close();
	out.close();

	return 0;
}