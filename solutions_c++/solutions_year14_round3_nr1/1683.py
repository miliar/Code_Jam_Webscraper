#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
int P, Q;
void parseStr(char *str)
{
	char str2[256];
	strcpy(str2, str);
	char *QStr = strchr(str2, '/');
	*QStr = 0;
	QStr++;
	char *PStr = str2;
	P = atoi(PStr);
	Q = atoi(QStr);
}
void solve(int caseNo)
{
	char str[256];
	scanf("%s", str);
	parseStr(str);

	if (Q & (Q-1)){
		if (caseNo != 1)
			printf("\n");
		printf("Case #%d: impossible", caseNo);
		return;
	}
	int count = 0;
	while (P < Q){
		P = P * 2;
		count++;
	}
	if (caseNo != 1)
		printf("\n");
	printf("Case #%d: %d", caseNo, count);
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
