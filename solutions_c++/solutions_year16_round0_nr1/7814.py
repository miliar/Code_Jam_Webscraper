#include<stdio.h>

#define SIZE 201

int N;
int Case;
int Ans;
int Used[10];
int Count;

void initUsed()
{
	int i;
	for (i=0; i<10; i++)
		Used[i] = 0;
}

void solve(int n)
{
	int r;
	long t = n;
	t *= N;
	while (t) {
		r = t%10;
		t /= 10;
		if (!Used[r]) {
			Used[r] = 1;
			Count++;
		}
	}
}

void readCase()
{
	scanf("%d", &N);
}

void solveCase()
{
	int i;
	initUsed();
	Count = 0;
	for (i=1; i<=100; i++) {
		solve(i);
		if (Count == 10)
			break;
	}
	Ans = i*N;
}

void printCase()
{
	printf("Case #%d: ", Case);
	if (Count < 10)
		printf("INSOMNIA\n");
	else
		printf("%d\n", Ans);
}

int main()
{
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (Case=1; Case<=T; Case++) {
		readCase();
		solveCase();
		printCase();
	}
	return 0;
}
