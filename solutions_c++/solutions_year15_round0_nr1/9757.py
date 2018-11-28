#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void main()
{
	int T, max, count, k, f;
	string s;

	ifstream in;
	ofstream out;
	in.open("A-small-attempt4.in");
	out.open("A-small4.out");

	in >> T;

	for (int i = 0; i < T; i++)
	{
		count = 0, f = 0;
		in >> max >> s;
		for (int j = 0; j <= max; j++)
		{
			k = s[j] - '0';
			
			if ((j > count) && (k!=0))
			{
				f += j - count;
				count += f;
			}
			count += k;
		}
		out << "Case #" << i + 1 << ": " << f << endl;
	}

	in.close();
	out.close();
}