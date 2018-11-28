#include <fstream>
#include <iostream>
#include <array>

using namespace std;

FILE *fin, *fout;
int t;
//zero - z two - w four - u six - x eight - g 
//five - f seven - v three - h one - o nine - i

int letters[100];

int a[100];

int main()
{
	fopen_s(&fin, "input.txt", "r");
	fopen_s(&fout, "output.txt", "w");
	fscanf_s(fin, "%d", &t);

	char s[2001];

	for (int k = 1; k <= t; k++) {
		for (int i = 0; i < 40; i++) {
			letters[i] = 0;
			a[i] = 0;
		}

		fscanf_s(fin, "%s", &s, _countof(s));

		for (int i = 0; i < strlen(s); i++) {
			letters[s[i] - 'A']++;
		}

		a[0] = letters['Z' - 'A'];
		letters['E' - 'A'] -= a[0];
		letters['R' - 'A'] -= a[0];
		letters['O' - 'A'] -= a[0];
		letters['Z' - 'A'] = 0;

		a[2] = letters['W' - 'A'];
		letters['T' - 'A'] -= a[2];
		letters['O' - 'A'] -= a[2];
		letters['W' - 'A'] -= 0;

		a[4] = letters['U' - 'A'];
		letters['F' - 'A'] -= a[4];
		letters['O' - 'A'] -= a[4];
		letters['U' - 'A'] -= a[4];
		letters['R' - 'A'] -= a[4];

		a[6] = letters['X' - 'A'];
		letters['S' - 'A'] -= a[6];
		letters['I' - 'A'] -= a[6];
		letters['X' - 'A'] -= a[6];

		a[8] = letters['G' - 'A'];
		letters['E' - 'A'] -= a[8];
		letters['I' - 'A'] -= a[8];
		letters['G' - 'A'] -= a[8];
		letters['H' - 'A'] -= a[8];
		letters['T' - 'A'] -= a[8];

		a[5] = letters['F' - 'A'];
		letters['F' - 'A'] -= a[5];
		letters['I' - 'A'] -= a[5];
		letters['V' - 'A'] -= a[5];
		letters['E' - 'A'] -= a[5];

		a[7] = letters['V' - 'A'];
		letters['S' - 'A'] -= a[7];
		letters['E' - 'A'] -= a[7];
		letters['V' - 'A'] -= a[7];
		letters['E' - 'A'] -= a[7];
		letters['N' - 'A'] -= a[7];

		a[3] = letters['H' - 'A'];
		letters['T' - 'A'] -= a[3];
		letters['H' - 'A'] -= a[3];
		letters['R' - 'A'] -= a[3];
		letters['E' - 'A'] -= a[3];
		letters['E' - 'A'] -= a[3];

		a[1] = letters['O' - 'A'];
		letters['O' - 'A'] -= a[1];
		letters['N' - 'A'] -= a[1];
		letters['E' - 'A'] -= a[1];

		a[9] = letters['I' - 'A'];
		fprintf_s(fout, "Case #%d: ", k); 

		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < a[i]; j++) {
				fprintf_s(fout, "%d", i);
			}
		}

		fprintf(fout, "\n");
	}

	return 0;
}