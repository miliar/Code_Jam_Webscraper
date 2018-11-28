#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out2.txt");
	int T;
	cin >> T;
	for (int TT = 0; TT < T; TT++)
	{
		int SM;
		string S;
		cin >> SM >> S;

		int Sum = 0;
		int Needed = 0;
		for (int i = 0; i <= SM; i++)
		{
			if (i > Sum)
			{
				Needed++;
				Sum++;
				i--;
			}
			else
			{
				Sum += S[i] - '0';
			}
		}
		cout << "Case #" << TT + 1 << ": " << Needed << endl;
	}

	return 0;
}