#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int num[30];
int ch[30];

int main() {
	int n;
	fin>>n;
	for (int i = 0; i < n; i++) {
		string s;
		fin>>s;
		for (int j = 0; j < 30; j++) {
			num[j]=0;
			ch[j]=0;
		}
		for (int j = 0; j < s.length(); j++)
			ch[s[j]-'A']++;

		num[0] = ch['Z'-'A'];
		ch['E'-'A'] -= num[0];
		ch['R'-'A'] -= num[0];
		ch['O'-'A'] -= num[0];

		num[2] = ch['W'-'A'];
		ch['T'-'A'] -= num[2];
		ch['O'-'A'] -= num[2];

		num[6] = ch['X'-'A'];
		ch['S'-'A'] -= num[6];
		ch['I'-'A'] -= num[6];

		num[8] = ch['G'-'A'];
		ch['E'-'A'] -= num[8];
		ch['I'-'A'] -= num[8];
		ch['H'-'A'] -= num[8];
		ch['T'-'A'] -= num[8];

		num[4] = ch['U'-'A'];
		ch['F'-'A'] -= num[4];
		ch['R'-'A'] -= num[4];
		ch['O'-'A'] -= num[4];

		num[5] = ch['F'-'A'];
		ch['I'-'A'] -= num[5];
		ch['V'-'A'] -= num[5];
		ch['E'-'A'] -= num[5];

		num[7] = ch['V'-'A'];
		ch['E'-'A'] -= 2*num[7];
		ch['S'-'A'] -= num[7];
		ch['N'-'A'] -= num[7];

		num[3] = ch['R'-'A'];
		ch['E'-'A'] -= 2*num[3];
		ch['T'-'A'] -= num[3];
		ch['H'-'A'] -= num[3];

		num[1] = ch['O'-'A'];
		ch['E'-'A'] -= num[1];
		ch['N'-'A'] -= num[1];

		num[9] = ch['I'-'A'];
		ch['N'-'A'] -= 2*num[9];
		ch['E'-'A'] -= num[9];

		string output="";
		for (int j = 0; j < 10; j++)
			for (int k = 0; k < num[j]; k++)
				output+=(char)('0'+j);
		fout<<"Case #"<<i+1<<": "<<output<<endl;
	}
}