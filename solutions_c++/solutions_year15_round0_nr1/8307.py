// QualificationA.cpp : Defines the entry point for the console application.
//

#include <stdio.h>

int main(int argc, const char* argv[])
{
	FILE *istream;
	FILE *ostream;

	freopen_s(&istream, "in", "r", stdin);
	freopen_s(&ostream, "out", "w", stdout);
	int totalCases;
	scanf_s("%d", &totalCases);
	for (int caseNr=1; caseNr<=totalCases; ++caseNr) {
		printf_s("Case #%d: ", caseNr);
		int s_max, ppl;
		int friends =0;
		int ova_lvl =0;
		scanf_s("%d", &s_max);
		for (int s_i = 0; s_i<=s_max; ++s_i) {
			scanf_s("%1d", &ppl);
			if (ppl>0) {
				if (s_i > ova_lvl) {
					int diff = s_i - ova_lvl;
					friends += diff;
					ova_lvl += diff;
				}
				ova_lvl += ppl;
			}
		}
		printf_s("%d\n", friends);
	}

	return 0;
}

