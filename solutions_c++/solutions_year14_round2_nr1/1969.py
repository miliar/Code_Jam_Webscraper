#include <assert.h>
#include <cstring>
#include <iostream>
using namespace std;

const int MXN = 105;

char str[MXN][MXN];
int rec[MXN][MXN];
int len[MXN];
int n;

void deal()
{
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> str[i];
		len[i] = 0;
		char last = -1;
		for (int j = 0; j < strlen(str[i]); ++j) {
			if (str[i][j] != last) {
				str[i][len[i]] = str[i][j];
				rec[i][len[i]] = 0;
				++len[i];
				last = str[i][j];
			}
			++rec[i][len[i]-1];
		}	
		cerr << i << ' ' << len[i] << endl;
	}
	for (int i = 0; i < n; ++i) {
		cerr << i << endl;
		for (int j = 0; j < len[i]; ++j) {
			cerr << str[i][j] << rec[i][j] << ' ';
		}
		cerr << endl;
	}
	int size = len[0];
	for (int i = 1; i < n; ++i) {
		if (len[i] != size) {
			cout << "Fegla Won" << endl;
			return ;
		}
	}
	int ans = 0;
	for (int t = 0; t < size; ++t) {
		int tot = 0;
		for (int i = 0; i < n; ++i) {
			tot += rec[i][t];
		}	
		int ex = tot / n + 0.5;
		cerr << "tot" << tot << "ex" << ex << endl;	
		for (int i = 0; i < n; ++i) {
			ans += rec[i][t] > ex ? rec[i][t] - ex : ex - rec[i][t];
		}
	}
	cout << ans << endl;
}


int main()
{
	int cases;
	ios::sync_with_stdio(false);
	cin >> cases;
	for (int t = 1; t <= cases; ++t) {
		cout << "Case #" << t << ": ";
		deal();
	}

	return 0;
}
