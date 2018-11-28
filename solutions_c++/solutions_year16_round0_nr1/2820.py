#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int N, M;
vector<int> t;

int main()
{
	int c;
	cin >> c;
	for (int cc = 1; cc <= c; cc++) {
		cin >> N;
		t.clear();
		t.resize(10);
		for (int j = 0; j < 10; j++)
			t[j] = 0;
		int i;
		for (i = 1; i <= 100; i++)
		{
			M = N * i;
			ostringstream ost;
			ost << M;
			string s = ost.str();
			for (int j = 0; j < s.length(); j++)
				t[s[j] - '0'] = 1;
			int a = 0;
			for (int j = 0; j < 10; j++)
				a += t[j];
			if (a == 10)
				break;
		}
		if (i == 101)
			cout << "Case #" << cc << ": INSOMNIA" << endl;
		else
			cout << "Case #" << cc << ": " << M << endl;
	}
}