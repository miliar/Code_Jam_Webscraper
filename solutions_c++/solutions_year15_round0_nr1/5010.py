# include <iostream>
# include <string>
# include <fstream>

using namespace std;

int standingOvation (const string &S)
{
	int sum = 0, count = 0;
	for (int i = 0; i < S.length (); i++)
	{
		if (sum < i)
		{
			count++;
			sum++;
		}
		sum += S [i]-48;
	}
	return count;
}

int main ()
{
	int num, testCases;
	string s;
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");
	in >> testCases;
	for (int i = 0; i < testCases; i++)
	{
		in >> num >> s;
		out << "Case #" << i+1 << ": " << standingOvation (s) << endl;
	}
	in.close ();
	out.close ();

	return 0;
}