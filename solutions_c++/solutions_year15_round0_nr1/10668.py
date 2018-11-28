
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <conio.h>

#include <iostream>
#include <vector>
using namespace std;



#define MAX 100

int calc_ovation(char *s, int smax)
{
	int sum_running = s[0]-48;
	int ppl_nd = 0;

	for(int idx=1; idx < smax+1; ++idx)
	{
		if(s[idx]-48 > 0  && sum_running < idx) {
			ppl_nd += (idx) - sum_running;
			sum_running += ppl_nd;
		}

		sum_running += s[idx]-48;

		}

	return ppl_nd;
}

int main()
{
	FILE *fp, *fout;
	if (fopen_s(&fp, "C:\\Users\\flodhi\\Dropbox\\MiscWork\\CodeJam\\A-small-attempt0.in", "r") != 0)
		printf("error opening read file\n");
	if (fopen_s(&fout, "C:\\Users\\flodhi\\Dropbox\\MiscWork\\CodeJam\\A-small-attempt0.out", "w") != 0)
		printf("error opening write file\n");

	int case_num=0;
	int total_cases;

	fscanf_s(fp, "%d\n", &total_cases);
	cout << total_cases << endl;

	//total_cases = 1;
	for (; case_num < total_cases; ++case_num)
	{

		char str[MAX];
		fgets(str, MAX, fp);

		// extract Smax and pass only remaining string for calculation
		int smax = str[0]-48;
		printf("string is %s", str);
		int ppl_needed = calc_ovation(&str[2], smax);
		
		printf("ppl needed are %d\n", ppl_needed);

		fprintf(fout, "Case #%d: %d\n", case_num + 1, ppl_needed);

		//	fprintf(fout, " Bad magician!\n");
		//else
		//	fprintf(fout, " Volunteer cheated!\n");
	}

	fclose(fp);
	fclose(fout);

	_getche();
	return 0;
}
