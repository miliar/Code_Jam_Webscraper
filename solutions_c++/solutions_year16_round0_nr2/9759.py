#include <cstdio>
#include <cstring>

const int MAXN = 1000;

char pancakes[MAXN+5];
int N;

void doTest(int caseNumber)
{
	scanf("%s", pancakes);
	N = strlen(pancakes);
	
	bool sign=(pancakes[0] == '+');
	int answer=0;
	for(int i=1; i<N; i++) if(pancakes[i] != pancakes[i-1]) { sign=!sign; answer++; }
	if(!sign) answer++;
	
	printf("Case #%d: %d\n", caseNumber, answer);
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int i=1; i<=T; i++) doTest(i);
	
	
	return 0;
	
}
