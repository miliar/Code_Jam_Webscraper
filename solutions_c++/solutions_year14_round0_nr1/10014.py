#include <iostream>
#include <sstream>
using namespace std;

int main ()
{
	int T, c = 0;
	cin >> T;

	string tmp;
	getline (cin, tmp);

	T++;
	while (--T)
	{
		int r1 [4], r2 [4];
		int fc = 0, sc = 0;

		c++;
		cin >> fc, getline (cin, tmp);
		string t [4];

		for (int i = 0; i < 4; i++)
			getline (cin, t [i]);

		istringstream instream;
		instream.clear ();
		instream.str (t [fc - 1]);

		for (int i = 0; i < 4; i++)
			instream >> r1 [i];

		cin >> sc, getline (cin, tmp);

		for (int i = 0; i < 4; i++)
			getline (cin, t [i]);

		instream.clear ();
		instream.str (t [sc - 1]);

		for (int i = 0; i < 4; i++)
			instream >> r2 [i];

		int e = 0, ind = 0;

		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (r1 [i] == r2 [j])
				{
					ind = i;
					e++;
				}

		cout << "Case #" << c << ": ";
		if (e < 1)
			cout << "Volunteer cheated!" << endl;

		if (e > 1)
			cout << "Bad magician!" << endl;

		if (e == 1)
			cout << r1 [ind] << endl;
	}

	return 0;
}