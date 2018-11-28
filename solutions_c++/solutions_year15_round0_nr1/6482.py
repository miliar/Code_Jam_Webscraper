#define IOSTREAM_TO_FSTREAM

#include<iostream>
#ifdef IOSTREAM_TO_FSTREAM
#include<fstream>
#endif

using namespace std;

int main()
{
#ifdef IOSTREAM_TO_FSTREAM
	ifstream fin;
	fin.open("A-large.in");
	cin.rdbuf(fin.rdbuf());
	ofstream fout;
	fout.open("A-large.out");
	cout.rdbuf(fout.rdbuf());
#endif
	int n0;
	cin >> n0;
	int max, r;
	char s[1010];
	int sn[1010];
	for (int i0 = 1 ; i0 <= n0 ; i0++) {
		cin >> max;
		for (int i = 0 ; i < 1010 ; i++) {
			s[i] = 0;
		}
		int now = 0;
		r = 0;
		for (int i = 0 ; i <= max ; i++) {
			cin >> s[i];
			sn[i] = s[i] - '0';
			if (i <= now) {
				now += sn[i];
			} else {
				r += i - now;
				now = i + sn[i];
			}
		}
		cout << "Case #" << i0 << ": " << r << endl;
	}
	return 0;
}
