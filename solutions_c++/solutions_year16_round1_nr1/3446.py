#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//don't worry - be happy :)

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");


	int nTests;
	in >> nTests;
	for (int t = 1; t <= nTests; t++)
	{
		string s,sres;
		char temp;

		in >> s;

		sres = s[0];

		for (int i = 1; i < s.length(); i++)
		{
			if (s[i] >= sres[0])
				sres = s[i] + sres;
			else
				sres = sres + s[i];
		}
		out << "Case #" << t << ": " << sres << endl;

	}
	





	return 0;
}