#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("A-small-attempt5.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	string s;
	int num, x, r, c;
	cin >> num;

	for (int i = 0; i<num; i++)
	{
		r = 0;
		c = 0;
		cin >> x;
		cin >> s;

		for (int j = 0; j<x + 1; j++)
		{
			if (c >= j)
			{
				c += (s[j] - '0');
				//	cout<<c<<endl;
			}
			else
			{

				r += (j - c);
				c += (s[j] - '0') + 1;
			}

		}

		cout << "Case #" << i + 1 << ": " << r << endl;
	}

	return 0;
}