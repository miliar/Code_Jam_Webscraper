#include <iostream>
#include <algorithm>
#define max(a,b) (a>b) ? a:b

using namespace std;

int pi[1000] = { 0, };
int result=0,d;

int calcurateEatTime(int pi, int share)
{
	return pi / (share + 1) + (pi % (share + 1));
}
void SearchTime(int eat, int share, int idx){
	
	if (idx == d || eat>=pi[idx]){
		if (result > eat + share)
			result = eat + share;
		return;
	}

	int st = 0;

	while (1)
	{

		SearchTime(max(eat, calcurateEatTime(pi[idx], st)), share + st, idx + 1);
		if (calcurateEatTime(pi[idx], st) < calcurateEatTime(pi[idx], st + 1) + 1)
			break;
		st++;
	}
}
void main()
{
	FILE *fs = fopen("input.txt", "r");
	FILE *fp = fopen("output.txt", "w");

	int testcase;
	fscanf(fs, "%d", &testcase);

	for (int t = 0; t < testcase; t++)
	{
		fscanf(fs, "%d", &d);

		for (int j = 0; j < d; j++)
			fscanf(fs, "%d", &pi[j]);
		std::sort(pi, pi + d);
		std::reverse(pi, pi + d);
		result = pi[0];

		SearchTime(0, 0, 0);
		fprintf(fp, "Case #%d: %d\n", t + 1,result);
	}
	fclose(fs);
	fclose(fp);
}