#include<iostream>
#include<string>
using namespace std;



int main() {
	FILE *fpi, *fpo;
	fpi = fopen("A-large.in", "r");
	fpo = fopen("largeA.out", "w");
	int re;
	fscanf(fpi, "%d", &re);
	for (int co = 1; co <= re; co++) {
		char r[3000];
		fscanf(fpi, "%s", r);
		string str = r;
		int count[26];
		for (int i = 0; i < 26; i++)
			count[i] = 0;
		for (int i = 0; i < str.length(); i++) {
			count[str[i] - 'A']++;
		}
		int result[10];
		for (int i = 0; i < 10; i++) {
			result[i] = 0;
		}
		result[6] = count['X' - 'A'];
		count['I' - 'A'] -= result[6];
		count['S' - 'A'] -= result[6];
		result[7] = count['S' - 'A'];
		count['E' - 'A'] -= 2 * result[7];
		count['N' - 'A'] -= result[7];
		result[8] = count['G' - 'A'];
		count['H' - 'A'] -= result[8];
		count['I' - 'A'] -= result[8];
		result[2] = count['W' - 'A'];
		count['O' - 'A'] -= result[2];
		result[0] = count['Z' - 'A'];
		count['O' - 'A'] -= result[0];
		count['R' - 'A'] -= result[0];
		result[3] = count['H' - 'A'];
		count['R' - 'A'] -= result[3];
		result[4] = count['R' - 'A'];
		count['F' - 'A'] -= result[4];
		count['O' - 'A'] -= result[4];
		result[5] = count['F' - 'A'];
		count['I' - 'A'] -= result[5];
		result[1] = count['O' - 'A'];
		result[9] = count['I' - 'A'];
		fprintf(fpo, "Case #%d: ", co);
		int t = 0;
		while (t<10) {
			if (result[t]  != 0) {
				fprintf(fpo, "%d", t);
				result[t]--;
			}
			else {
				t++;
			}
		}
		fprintf(fpo, "\n");

	}
	fclose(fpi);
	fclose(fpo);
}