#include<iostream>
#include<cstdio>
#include<cmath>
#include<math.h>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
using namespace std;

void init()
{
#ifdef MY_TEST_VAR
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
}

unsigned char_stats[50];
char line[3000];
unsigned line_len;

unsigned count_letter(char letter) {
	return char_stats[letter - 'A'];
}

void substract_word(const string &str, unsigned num) {
	for (unsigned i = 0; i < str.size(); ++i) {
		char_stats[str[i] - 'A'] -= num;
	}
}

unsigned count_and_sub(char letter, const string &str) {
	const unsigned n = count_letter(letter);
	substract_word(str, n);
	return n;
}

void debug_stats() {
	for (char i = 'A'; i <= 'Z'; ++i) {
		printf("%c=%u ", i, char_stats[i - 'A']);
	}
	printf("\n");
}


void solve()
{
	unsigned n = 0;
	scanf("%u", &n);
	unsigned num_stats[20];
	for (unsigned T = 0; T < n; ++T) {
		for (char i = 'A'; i <= 'Z'; ++i) {
			char_stats[i - 'A'] = 0;
		}
		scanf("%2500s", line);
		line_len = strlen(line);
		for (unsigned i = 0; i < line_len; i++) {
			++char_stats[line[i] - 'A'];
		}
		printf("Case #%u: ", T + 1);
		/*
		"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
		*/
		num_stats[0] = count_and_sub('Z', "ZERO");
		num_stats[2] = count_and_sub('W', "TWO");
		num_stats[8] = count_and_sub('G', "EIGHT");
		num_stats[6] = count_and_sub('X', "SIX");
		num_stats[7] = count_and_sub('S', "SEVEN");
		num_stats[5] = count_and_sub('V', "FIVE");
		num_stats[4] = count_and_sub('F', "FOUR");
		num_stats[1] = count_and_sub('O', "ONE");
		num_stats[9] = count_and_sub('I', "NINE");
		num_stats[3] = count_and_sub('T', "THREE");
		for (unsigned num = 0; num < 10; ++num) {
			// printf("%u ", num_stats[num]);
			for (unsigned i = 0; i < num_stats[num]; ++i) {
				printf("%c", ('0' + num));
			}
		}
		printf("\n");
	}
}

int main()
{
	init();
	solve();
	return 0;
}