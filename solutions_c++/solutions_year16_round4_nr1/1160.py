#include <cstdio>
#include <string>
using namespace std;

void work()
{
	int n, r, s, p;
	string ans = "", PS, RS, PR;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	char win[150];
	string str[15][150];
	str[0]['R'] = "R";
	str[0]['P'] = "P";
	str[0]['S'] = "S";
	win['R'] = 'S';
	win['P'] = 'R';
	win['S'] = 'P';
	for (int i = 1; i <= 12; i++) {
		for (int j = 'P'; j <= 'S'; j++) {
			if (win[j]) {
				char k = win[j];
				if (str[i - 1][k] < str[i - 1][j]) {
					str[i][j] = str[i - 1][k] + str[i - 1][j];
				} else {
					str[i][j] = str[i - 1][j] + str[i - 1][k];
				}
			}
		}
	}
	// count R
	int rrcount = 0;
	int rpcount = 0;
	int rscount = 0;
	int prcount = 0;
	int ppcount = 0;
	int pscount = 0;
	int srcount = 0;
	int spcount = 0;
	int sscount = 0;
	for (int i = 0; i < str[n]['R'].length(); i++) {
		if (str[n]['R'][i] == 'R') {
			rrcount ++;
		} else if (str[n]['R'][i] == 'P') {
			rpcount ++;
		} else {
			rscount ++;
		}
	}
	for (int i = 0; i < str[n]['P'].length(); i++) {
		if (str[n]['P'][i] == 'R') {
			prcount ++;
		} else if (str[n]['P'][i] == 'P') {
			ppcount ++;
		} else {
			pscount ++;
		}
	}
	for (int i = 0; i < str[n]['S'].length(); i++) {
		if (str[n]['S'][i] == 'R') {
			srcount ++;
		} else if (str[n]['S'][i] == 'P') {
			spcount ++;
		} else {
			sscount ++;
		}
	}
	if (rrcount == r && rpcount == p && rscount == s) {
		puts(str[n]['R'].c_str());
	} else if (prcount == r && ppcount == p && pscount == s) {
		puts(str[n]['P'].c_str());
	} else if (srcount == r && spcount == p && sscount == s) {
		puts(str[n]['S'].c_str());
	} else {
		puts("IMPOSSIBLE");
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		work();
	}
}