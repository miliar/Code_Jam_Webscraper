#include<stdio.h>

#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
char cc;

char A[1111];
int N, T, Ret;

void Flip(int x)
{
	int l1, l2;

	Ret++;

	l1 = 0;
	l2 = x-1;
	while(l1 < l2)
	{
		Swap(A[l1], A[l2]);
		l1++;
		l2--;
	}
	for(l1 = 0; l1 < x; l1++)
	{
		if(A[l1] == '+') A[l1] = '-';
		else if(A[l1] == '-') A[l1] = '+';
	}
}

int main(void)
{
	int l0, l1;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%s", A);
		for(N = 0; A[N]; N++);

		Ret = 0;
		while(1)
		{
			for(l1 = 0; l1 < N; l1++) if(A[l1] == '-') break;
			if(l1 == N) break;

			for(l1 = 0; A[l1] == '+'; l1++);
			if(l1 > 0) Flip(l1);

			for(l1 = N-1; l1 >= 0; l1--) if(A[l1] == '-') break;
			Flip(l1+1);
		}

		printf("Case #%d: %d\n", l0, Ret);
	}

	return 0;
}
