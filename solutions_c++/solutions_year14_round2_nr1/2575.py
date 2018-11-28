#define IOSTREAM_TO_FSTREAM

#include<iostream>
#include<string.h>
#ifdef IOSTREAM_TO_FSTREAM
#include<fstream>
#endif

using namespace std;

int main()
{
#ifdef IOSTREAM_TO_FSTREAM
	ifstream fin;
	fin.open("A-small-attempt0.in");
	cin.rdbuf(fin.rdbuf());
	ofstream fout;
	fout.open("A-small-attempt0.out");
	cout.rdbuf(fout.rdbuf());
#endif
	int m, n;
	char s[110][110];
	char ss[110][110];
	int sn[110][110];
	char rb;
	cin >> n;
	for (int i = 1 ; i <= n ; i++) {
		for (int j = 0 ; j < 110 ; j++) {
			for (int k = 0 ; k < 110 ; k++) {
				s[j][k] = 0;
				ss[j][k] = 0;
				sn[j][k] = 0;
			}
		}
		bool flag = false;
		cin >> m;
		cin.get(rb);
		for (int j = 0 ; j < m ; j++) {
			cin.getline(s[j], 110);
		}
		for (int j = 0 ; j < m ; j++) {
			char t = s[j][0];
			int tn = 1;
			int tk = 0;
			for (int k = 1 ; k < strlen(s[j]) ; k++) {
				if (s[j][k] != t) {
					ss[j][tk] = t;
					sn[j][tk] = tn;
					tk++;
					t = s[j][k];
					tn = 1;
				} else {
					tn++;
				}
			}
			ss[j][tk] = t;
			sn[j][tk] = tn;
			/*for (int k = 0 ; k < strlen(ss[j]) ; k++) {
				cout << ss[j][k] << ": " << sn[j][k] << endl;
			}
			cout << endl;*/
		}
		int t = strlen(ss[0]);
		for (int j = 0 ; j < m ; j++) {
			if (t != strlen(ss[j])) {
				flag = true;
				break;
			}
		}
		if (!flag) {
			for (int k = 0 ; k < t ; k++) {
				char ts = ss[0][k];
				int tn = sn[0][k];
				for (int j = 0 ; j < m ; j++) {
					if (ts != ss[j][k]) {
						flag = true;
						break;
					}
				}
			}
		}
		if (flag == true) {
			cout << "Case #" << i << ": Fegla Won" << endl;
			continue;
		}
		int sum = 0;
		for (int k = 0 ; k < t ; k++) {
			int tn = 0;
			for (int j = 0 ; j < m ; j++) {
				tn += sn[j][k];
			}
			int tm = (int)((double)tn / m + 0.500001);
			for (int j = 0 ; j < m ; j++) {
				sum += abs(sn[j][k] - tm);
			}
		}
		cout << "Case #" << i << ": " << sum << endl;
	}
	return 0;
}
