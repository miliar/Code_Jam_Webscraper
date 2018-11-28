#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main()
{
	ifstream in("A-large.in");
	ofstream out("1.txt");
	unsigned int T;
	unsigned int i, j;
	in >> T;
	string s, sol, tmp;
	for (i = 0; i < T; i++)
	{
		in >> s;
		sol = "";
		sol += s[0];
		for (j = 1; j < s.length(); j++)
		{
			if (s[j] > sol[0] || s[j] == sol[0])
			{
				tmp = s[j] + sol;
				sol = tmp;
			}
			else
				sol = sol + s[j];
		}
		out << "Case #"<< i + 1 <<": ";
		out << sol << endl;
	}
}