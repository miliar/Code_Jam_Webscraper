#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

int tt( string s )
{
	stringstream ss;
	int y;
	ss << s;
	ss >> y;
	return y;
}

string tt1(int w)
{
	stringstream ss;
	string u;
	ss << w;
	ss >> u;
	ss.clear();
	return u;
}

int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++ )
	{
		int num;
		cin >> num;
		int orinum = num;
		set< int > cc;
		if (num == 0)
		{
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;

		}
		else
		{
			string v;
			int rr = 1;
			while (cc.size() < 10)
			{
				num = orinum * rr;
				v = tt1( num );
				for (int j = 0; j < v.size(); j++)
				{
					int ww = v[j] - 0x30;
					cc.insert(ww);
				}
				rr++;
			}

			cout << "Case #" << i + 1 << ": " << num << endl;
		}
	}
    return 0;
}
