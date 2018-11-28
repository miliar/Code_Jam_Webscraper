#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
int caseNum, totalCaseNum;

int main()
{
	int cnt[26], r[10];
	int i, j, t;
	char s[2001];

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &totalCaseNum);
	for(caseNum=1; caseNum<=totalCaseNum; caseNum++)
	{
		for(i=0; i<26; i++) cnt[i] = 0;
		for(i=0; i<10; i++) r[i] = 0;
		scanf("%s", s);
		for(i=strlen(s)-1; i>=0; i--) cnt[s[i]-'A']++;

		// 8
		t = cnt['G'-'A'];
		r[8] += t;
		cnt['E'-'A'] -= t;
		cnt['I'-'A'] -= t;
		cnt['G'-'A'] -= t;
		cnt['H'-'A'] -= t;
		cnt['T'-'A'] -= t;

		// 0
		t = cnt['Z'-'A'];
		r[0] += t;
		cnt['Z'-'A'] -= t;
		cnt['E'-'A'] -= t;
		cnt['R'-'A'] -= t;
		cnt['O'-'A'] -= t;

		// 6
		t = cnt['X'-'A'];
		r[6] += t;
		cnt['S'-'A'] -= t;
		cnt['I'-'A'] -= t;
		cnt['X'-'A'] -= t;

		// 2
		t = cnt['W'-'A'];
		r[2] += t;
		cnt['T'-'A'] -= t;
		cnt['W'-'A'] -= t;
		cnt['O'-'A'] -= t;

		// 4
		t = cnt['U'-'A'];
		r[4] += t;
		cnt['F'-'A'] -= t;
		cnt['O'-'A'] -= t;
		cnt['U'-'A'] -= t;
		cnt['R'-'A'] -= t;

		// 3
		t = cnt['H'-'A'];
		r[3] += t;
		cnt['T'-'A'] -= t;
		cnt['H'-'A'] -= t;
		cnt['R'-'A'] -= t;
		cnt['E'-'A'] -= t;
		cnt['E'-'A'] -= t;

		// 1
		t = cnt['O'-'A'];
		r[1] += t;
		cnt['O'-'A'] -= t;
		cnt['N'-'A'] -= t;
		cnt['E'-'A'] -= t;

		// 7
		t = cnt['S'-'A'];
		r[7] += t;
		cnt['S'-'A'] -= t;
		cnt['E'-'A'] -= t;
		cnt['V'-'A'] -= t;
		cnt['E'-'A'] -= t;
		cnt['N'-'A'] -= t;

		// 5
		t = cnt['V'-'A'];
		r[5] += t;
		cnt['F'-'A'] -= t;
		cnt['I'-'A'] -= t;
		cnt['V'-'A'] -= t;
		cnt['E'-'A'] -= t;

		// 9
		t = cnt['I'-'A'];
		r[9] += t;
		cnt['N'-'A'] -= t;
		cnt['I'-'A'] -= t;
		cnt['N'-'A'] -= t;
		cnt['E'-'A'] -= t;

		printf("Case #%d: ", caseNum);
		for(i=0; i<10; i++)
		{
			for(j=0; j<r[i]; j++) printf("%d", i);
		}
		printf("\n");
	}

	return 0;
}