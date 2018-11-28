#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <list>
#include <map>
#include <assert.h>
using namespace std;

void Remove(vector<int>& freq, string num, int cnt)
{
	for (auto c : num)
	{
		freq[c - 'A'] -= cnt;
		assert(freq[c - 'A'] >= 0);
	}
}


int main()
{
	int num_of_testcases;
	cin >> num_of_testcases;
	for (int t = 1; t <= num_of_testcases; ++t){
		string s;
		cin >> s;

		vector<int> freq(27);
		for (int i = 0; i < s.length(); ++i) {
			freq[s[i] - 'A']++;
		}
		
		vector<int> n(10);

		n[0] = freq['Z' - 'A'];
		if (n[0] > 0)
			Remove(freq, "ZERO", n[0]);
		n[2] = freq['W' - 'A'];
		if (n[2] > 0)
			Remove(freq, "TWO", n[2]);
		n[6] = freq['X' - 'A'];
		if (n[6] > 0)
			Remove(freq, "SIX", n[6]);
		n[8] = freq['G' - 'A'];
		if (n[8] > 0)
			Remove(freq, "EIGHT", n[8]);
		n[3] = freq['H' - 'A'];
		if (n[3] > 0)
			Remove(freq, "THREE", n[3]);
		n[4] = freq['U' - 'A'];
		if (n[4] > 0)
			Remove(freq, "FOUR", n[4]);
		n[5] = freq['F' - 'A'];
		if (n[5] > 0)
			Remove(freq, "FIVE", n[5]);
		n[1] = freq['O' - 'A'];
		if (n[1] > 0)
			Remove(freq, "ONE", n[1]);
		n[7] = freq['V' - 'A'];
		if (n[7] > 0)
			Remove(freq, "SEVEN", n[7]);
		n[9] = freq['I' - 'A'];
		if (n[9] > 0)
			Remove(freq, "NINE", n[9]);

		string out = "";

		for (int i = 0; i < n.size(); ++i)
		{
			for (int j = 0; j < n[i]; ++j)
				out += (i+'0');
		}
		cout << "Case #" << t << ": " <<  out << "\n";
	}

    return 0;
}

