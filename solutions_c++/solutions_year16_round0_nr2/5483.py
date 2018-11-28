#include <fstream>
#include <string>

using namespace std;

bool allPluses(string s)
{
	for (int i = 0; i < s.length(); i++)
		if (s[i] != '+') return false;
	return true;
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int numberOfTests;
	in >> numberOfTests;

	for (int t = 1; t <= numberOfTests; t++)
	{
		string s;
		in >> s;

		int result = 0;
		
		int curSymbol = 0;

		while (!allPluses(s))
		{
			curSymbol = 0;
			char buf = s[curSymbol];
			while ((s[curSymbol] == buf)&&(curSymbol < s.length()))
			{
				if (s[curSymbol] == '+') s[curSymbol++] = '-';
				else if (s[curSymbol] == '-') s[curSymbol++] = '+';
			}
			result++;
		}
		out << "Case #" << t << ": ";
		out << result << endl;
	}

	return 0;
}
