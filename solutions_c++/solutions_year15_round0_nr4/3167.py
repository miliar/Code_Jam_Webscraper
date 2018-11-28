#include <stdio.h>
int main(int argc, char const *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int totalCases, x, r, c, limit;	scanf("%d", &totalCases);
	for (int caseNo = 1; caseNo <= totalCases; ++caseNo)
	{
		scanf("%d %d %d", &x, &r, &c);
		limit = (x+1)/2;
		if(x>=4)
			limit++;
		if (x<7 && (r>=limit && c>=limit) && (r>=x || c>=x) && (r*c%x==0))
			printf("Case #%d: GABRIEL\n", caseNo);
		else
			printf("Case #%d: RICHARD\n", caseNo);
	}
	return 0;
}