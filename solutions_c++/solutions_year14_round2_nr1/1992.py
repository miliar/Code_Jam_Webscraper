#include <iostream>
#include <string>

using namespace std;

unsigned nrInstances(string s, unsigned start, char c)
{
	unsigned i = start;
	while(s[i] == c && i < s.length())
	{
		i++;
	}
	
	return i - start;
}

int main(int argc, char *argv[])
{
	unsigned nrTCS = 0;
	cin >> nrTCS;

	for(unsigned i = 0; i < nrTCS; i++)
	{
		unsigned nr;
		cin >> nr;
		string s1, s2;
		cin >> s1 >> s2;

		unsigned answer = 0;
		bool Fegla = false;
		unsigned p1 = 0, p2 = 0;
		while(p1 < s1.length() && p2 < s2.length())
		{
			unsigned nr1 = nrInstances(s1, p1, s1[p1]);
			unsigned nr2 = nrInstances(s2, p2, s1[p1]);

			if (nr1 == 0 || nr2 == 0)
			{
				Fegla = true;
				break;
			}

			if (nr2 > nr1)
			{
				answer += nr2-nr1;
			} else
			{
				answer += nr1-nr2;
			}

			p1 += nr1;
			p2 += nr2;
		}

		if (p1 != s1.length() || p2 != s2.length())
		{
			Fegla = true;
		}

		cout << "Case #" << (i + 1) << ": ";
		if (!Fegla)
		{
			cout << answer << "\n";
		} else 
		{
			cout << "Fegla Won\n";
		}
	}

	return 0;
}