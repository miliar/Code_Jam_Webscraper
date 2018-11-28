//---------------------------------------------------------------------
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

int const MAX_CH = 100100;

char DGS[10][100] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char st[MAX_CH];

int t;

int cnt[10],all_cnt[10000];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	sscanf(st,"%d",&t);
	for (int q=0; q<t; q++) {
		gets(st);
		printf("Case #%d: ",q+1);

		int i = 0;
		int len = (int) strlen(st);

		for (int i=0; i<10; i++) cnt[i] = 0;
		
		for (int i=0; st[i]; i++) {
			cnt[0] += st[i] == 'Z';
			cnt[2] += st[i] == 'W';
			cnt[6] += st[i] == 'X';
			cnt[8] += st[i] == 'G';
		}

		for (int i=0; i<26; i++) all_cnt[i] = 0;
		for (int i=0; st[i]; i++)
			all_cnt[st[i]-'A']++;

		int chh = 0;
		for (int i=0; i<10; i++)
			if (i==0 || i == 2 || i == 6 || i == 8)
				for (int k=0; k<cnt[i]; k++)
					for (int j=0; DGS[i][j]; j++) {
						all_cnt[DGS[i][j]-'A']--;
						chh++;
					}

		int LNN = ((int) strlen(st)) - chh;
		int max_cnt = (LNN+2)/3;

		int FND = 0;

		for (int one = 0; one <= max_cnt && !FND; one++) {
			int one_Ok = 1;
			for (int j=0; DGS[1][j]; j++)
				all_cnt[DGS[1][j]-'A'] -= one;

			for (int j=0; j<26; j++)
				if (all_cnt[j] < 0)
					one_Ok = 0;

			if (!one_Ok) {
				for (int j=0; DGS[1][j]; j++)
					all_cnt[DGS[1][j]-'A'] += one;
				continue;
			}

			for (int thr = 0; thr+one <= max_cnt && !FND; thr++) {
				int thr_Ok = 1;
				for (int j=0; DGS[3][j]; j++)
					all_cnt[DGS[3][j]-'A'] -= thr;

				for (int j=0; j<26; j++)
					if (all_cnt[j] < 0)
						thr_Ok = 0;

				if (!thr_Ok) {
					for (int j=0; DGS[3][j]; j++)
						all_cnt[DGS[3][j]-'A'] += thr;
					continue;
				}

				int four = all_cnt['R'-'A'];

				int four_Ok = 1;
				for (int j=0; DGS[4][j]; j++)
					all_cnt[DGS[4][j]-'A'] -= four;

				for (int j=0; j<26; j++)
					if (all_cnt[j] < 0)
						four_Ok = 0;

				if (!four_Ok) {
					for (int j=0; DGS[3][j]; j++)
						all_cnt[DGS[3][j]-'A'] += thr;
					for (int j=0; DGS[4][j]; j++)
						all_cnt[DGS[4][j]-'A'] += four;
					continue;
				}

				for (int fiv = 0; fiv+one+thr+four <= max_cnt; fiv++) {
					int fiv_Ok = 1;
					for (int j=0; DGS[5][j]; j++)
						all_cnt[DGS[5][j]-'A'] -= fiv;

					for (int j=0; j<26; j++)
						if (all_cnt[j] < 0)
							fiv_Ok = 0;

					if (!fiv_Ok) {
						for (int j=0; DGS[5][j]; j++)
							all_cnt[DGS[5][j]-'A'] += fiv;
						continue;
					}

					int sev = all_cnt['V'-'A'];

					int sev_Ok = 1;
					for (int j=0; DGS[7][j]; j++)
						all_cnt[DGS[7][j]-'A'] -= sev;

					for (int j=0; j<26; j++)
						if (all_cnt[j] < 0)
							sev_Ok = 0;

					if (!sev_Ok) {
						for (int j=0; DGS[5][j]; j++)
							all_cnt[DGS[5][j]-'A'] += fiv;
						for (int j=0; DGS[7][j]; j++)
							all_cnt[DGS[7][j]-'A'] += sev;
						continue;
					}

					int nine = all_cnt['E'-'A'];

					int nine_Ok = 1;
					for (int j=0; DGS[9][j]; j++)
						all_cnt[DGS[9][j]-'A'] -= nine;

					for (int j=0; j<26; j++)
						if (all_cnt[j] < 0)
							nine_Ok = 0;

					if (!nine_Ok) {
						for (int j=0; DGS[5][j]; j++)
							all_cnt[DGS[5][j]-'A'] += fiv;
						for (int j=0; DGS[7][j]; j++)
							all_cnt[DGS[7][j]-'A'] += sev;
						for (int j=0; DGS[9][j]; j++)
							all_cnt[DGS[9][j]-'A'] += nine;
						continue;
					}

					int is_good = 1;
					for (int ee=0; ee<26; ee++)
						if (all_cnt[ee] != 0) {is_good = 0; break;}

					if (is_good)
					{
						FND = 1;
						cnt[1] = one;
						cnt[3] = thr;
						cnt[4] = four;
						cnt[5] = fiv;
						cnt[7] = sev;
						cnt[9] = nine;
						break;
					}

					for (int j=0; DGS[9][j]; j++)
							all_cnt[DGS[9][j]-'A'] += nine;

					for (int j=0; DGS[7][j]; j++)
							all_cnt[DGS[7][j]-'A'] += sev;

					for (int j=0; DGS[5][j]; j++)
						all_cnt[DGS[5][j]-'A'] += fiv;
				}

				for (int j=0; DGS[3][j]; j++)
					all_cnt[DGS[3][j]-'A'] += thr;

				for (int j=0; DGS[4][j]; j++)
					all_cnt[DGS[4][j]-'A'] += four;
			}

			for (int j=0; DGS[1][j]; j++)
				all_cnt[DGS[1][j]-'A'] += one;
		}

		for (int i=0; i<10; i++)
			for (int j=0; j<cnt[i]; j++)
				printf("%d",i);
		printf("\n");
	}
	return 0;
}