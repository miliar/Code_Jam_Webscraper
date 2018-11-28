#pragma comment(linker, "/STACK:36777216")
#include <bits/stdc++.h>
using namespace std;
#define fori(i, n) for (int i = 0; i < (int)(n); i++)
//----------------------------
//FILE *in = fopen("input.txt", "r");
//FILE *in = fopen("A-small-attempt0.in", "r");
ifstream in;
FILE *out = fopen("output.txt", "w");
//----------------------------
void solve() {
	char ch;
	int a[26];
	memset(a, 0, sizeof(a));
	/*while (fscanf(in, "%c", &ch)==1 && ch>='A' && ch<='Z') {
		a[ch - 'A']++;
	}*/
	string str;
	in>>str;
	for (int i = 0; i < str.size(); i++) {
		a[str[i] - 'A']++;	
	}
	int num[10];
	memset(num, 0, sizeof(num));
	if (a['Z' - 'A'] > 0) {
		num[0] = a['Z' - 'A'];
		a['Z' - 'A'] -= num[0];
		a['E' - 'A'] -= num[0];
		a['R' - 'A'] -= num[0];
		a['O' - 'A'] -= num[0];
	}
	if (a['U' - 'A'] > 0) {
		num[4] = a['U' - 'A'];
		a['F' - 'A'] -= num[4];
		a['O' - 'A'] -= num[4];
		a['U' - 'A'] -= num[4];
		a['R' - 'A'] -= num[4];
	}
	if (a['W' - 'A'] > 0) {
		num[2] = a['W' - 'A'];
		a['T' - 'A'] -= num[2];
		a['W' - 'A'] -= num[2];
		a['O' - 'A'] -= num[2];
	}
	if (a['G' - 'A'] > 0) {
		num[8] = a['G' - 'A'];
		a['E' - 'A'] -= num[8];
		a['I' - 'A'] -= num[8];
		a['G' - 'A'] -= num[8];
		a['H' - 'A'] -= num[8];
		a['T' - 'A'] -= num[8];
	}
	if (a['O' - 'A'] > 0) {
		num[1] = a['O' - 'A'];
		a['O' - 'A'] -= num[1];
		a['N' - 'A'] -= num[1];
		a['E' - 'A'] -= num[1];
	}
	if (a['H' - 'A'] > 0) {
		num[3] = a['H' - 'A'];
		a['T' - 'A'] -= num[3];
		a['H' - 'A'] -= num[3];
		a['R' - 'A'] -= num[3];
		a['E' - 'A'] -= num[3];
		a['E' - 'A'] -= num[3];
	}
	if (a['F' - 'A'] > 0) {
		num[5] = a['F' - 'A'];
		a['F' - 'A'] -= num[5];
		a['I' - 'A'] -= num[5];
		a['V' - 'A'] -= num[5];
		a['E' - 'A'] -= num[5];
	}
	if (a['X' - 'A'] > 0) {
		num[6] = a['X' - 'A'];
		a['S' - 'A'] -= num[6];
		a['I' - 'A'] -= num[6];
		a['X' - 'A'] -= num[6];
	}	
	if (a['S' - 'A'] > 0) {
		num[7] = a['S' - 'A'];
		a['S' - 'A'] -= num[7];
		a['E' - 'A'] -= num[7];
		a['V' - 'A'] -= num[7];
		a['E' - 'A'] -= num[7];
		a['N' - 'A'] -= num[7];
	}
	if (a['I' - 'A'] > 0) {
		num[9] = a['I' - 'A'];
		a['N' - 'A'] -= num[9];
		a['I' - 'A'] -= num[9];
		a['N' - 'A'] -= num[9];
		a['E' - 'A'] -= num[9];
	}
	string res;
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < num[i]; j++) {
			res += char(i + '0');
		}
	}
	res += '\n';
	fprintf(out, res.c_str());
}
//----------------------------
int main()
{
	int tn;
	in.open("A-large.in");
  	//fscanf(in, "%d\n", &tn);
  	in>>tn;
  	fori(t, tn) {
	  	fprintf(out, "Case #%d: ", t + 1);
    	solve();
  	}
  	//fclose(in);
  	in.close();
    fclose(out);
  	return 0;
}
