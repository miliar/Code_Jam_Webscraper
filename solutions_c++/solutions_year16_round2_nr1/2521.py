
#include <bits/stdc++.h>

using namespace std;

vector<string> ls({"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"});
string let;
map<char, int> mp;
vector<int> freq(10);

void sub(char c, int idx)
{
	int count = mp[c];
	for (char x: ls[idx])
		mp[x] -= count;
	freq[idx] = count;
}


int main()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t){
		cin >> let;
		mp.clear();
		for (char c: let)
			++mp[c];
		sub('G', 8);
		sub('X', 6);
		sub('Z', 0);
		sub('W', 2);
		sub('S', 7);
		sub('V', 5);

		sub('F', 4);
		sub('R', 3);
		sub('I', 9);
		sub('O', 1);

		cout << "Case #" << t + 1 << ": ";
		for (int i = 0; i < 10; ++i)
			for (int j = 0; j < freq[i]; ++j)
				cout << i;
		cout << endl;
	}

	return 0;
}
