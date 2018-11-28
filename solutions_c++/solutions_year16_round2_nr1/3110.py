#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

map<int, int> a;

void del(string p, int c)
{
	for (int i = 0; i < p.size(); i++)
		a[p[i]] -= c;
}

int main(int argc, char* argv[])
{
	freopen("io.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	vector<string> s;
	for (int i = 0; i < T; i++)
	{
		string tmp;
		cin >> tmp;
		s.push_back(tmp);
	}

	vector<int> h(10);

	for (int i = 'A'; i <= 'Z'; i++)
		a.insert(make_pair(i, 0));

	for (int i = 0; i < s.size(); i++)
	{
		for (int j = 0; j < s[i].size(); j++)
			a[s[i][j]]++;

		h[0] = a['Z'];
		del("ZERO", h[0]);

		h[2] = a['W'];
		del("TWO", h[2]);

		h[6] = a['X'];
		del("SIX", h[6]);

		h[7] = a['S'];
		del("SEVEN", h[7]);

		h[8] = a['G'];
		del("EIGHT", h[8]);

		h[5] = a['V'];
		del("FIVE", h[5]);

		h[4] = a['F'];
		del("FOUR", h[4]);

		h[3] = a['T'];
		del("THREE", h[3]);

		h[1] = a['O'];
		del("ONE", h[1]);

		h[9] = a['E'];
		del("NINE", h[9]);

		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < h.size(); j++)
			if (h[j] != 0)
			{
				for (int k = 0; k < h[j]; k++)
					cout << j;
				h[j] = 0;
			}

		cout << endl;
		for (int j = 'A'; j <= 'Z'; j++)
			a[j] = 0;
	}
	return 0;
}