#include <iostream>

using namespace std;

int main()
{
	int t, i, j, k, l, m, n, x;
	int hash[26];
	int num[10];
	char str[5000];
	cin >> t;

	for (x = 1; x <= t; ++x) {
		for (i = 0; i < 26; ++i) {
			hash[i] = 0;
		}
		for (i = 0; i < 10; ++i) {
			num[i] = 0;
		}
		cin >> str;
		for (i = 0; str[i] != '\0'; ++i) {
			hash[str[i] - 'A']++;
		}
		num[0] = hash['Z'-'A'];
		num[1] = hash['O'-'A'] - hash['Z'-'A'] - hash['W'-'A'] - hash['U'-'A'];
		num[2] = hash['W'-'A'];
		num[3] = hash['H'-'A'] - hash['G'-'A'];
		num[4] = hash['U'-'A'];
		num[5] = hash['F'-'A'] - hash['U'-'A'];
		num[6] = hash['X'-'A'];
		num[7] = hash['S'-'A'] - hash['X'-'A'];
		num[8] = hash['G'-'A'];
		num[9] = hash['I'-'A'] - hash['F'-'A']  + hash['U'-'A'] - hash['X'-'A'] - hash['G'-'A'];
	
		cout << "Case #" << x << ": ";
		for (i = 0; i < 10; ++i) {
			while (num[i] > 0) {
				cout << i;
				num[i]--;
			}
		}
		cout << endl;
	}

	return 0;
}
