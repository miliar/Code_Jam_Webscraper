#include<stdio.h>

#define swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
int cc;

int A[1000], B[1000], C[1000], N;
int Ret;
int Cnt;
int T;

void Sort1(int l1, int l2)
{
	int l3, l4;
	for(l3 = l1; l3+1 <= l2; l3++)
	{
		for(l4 = l1; l4+1 <= l2; l4++)
		{
			if(A[l4] > A[l4+1]){ swap(A[l4], A[l4+1]); Cnt++; }
		}
	}
}

void Sort2(int l1, int l2)
{
	int l3, l4;
	for(l3 = l1; l3+1 <= l2; l3++)
	{
		for(l4 = l1; l4+1 <= l2; l4++)
		{
			if(A[l4] < A[l4+1]){ swap(A[l4], A[l4+1]); Cnt++; }
		}
	}
}

int main(void)
{
	int l0, l1, l2, left, right;
	scanf("%d", &T);

	for(l0 = 1; l0 <= T; l0++)
	{
		fprintf(stderr, "%d\n", l0);
		scanf("%d", &N);
		for(l1 = 0; l1 < N; l1++) scanf("%d", &A[l1]);
		for(l1 = 0; l1 < N; l1++) B[l1] = A[l1];

		for(l1 = 0; l1 < N; l1++) C[l1] = 0;

		Ret = 1000000000;

		Ret = 0;
		for(l1 = 0; l1 < N; l1++)
		{
			int idx = -1;

			for(l2 = 0; l2 < N; l2++)
			{
				if(C[l2]) continue;
				if(idx == -1) idx = l2;
				else if(A[l2] < A[idx]) idx = l2;
			}

			left = 0; right = 0;
			for(l2 = 0; l2 < N; l2++) B[l2] = A[l2];
			l2 = idx;
			while(1)
			{
				if(l2 == 0) break;
				if(l2 > 0 && B[l2] > B[l2-1]) break;
				swap(B[l2], B[l2-1]);
				l2--;
				left++;
			}
			for(l2 = 0; l2 < N; l2++) B[l2] = A[l2];
			l2 = idx;
			while(1)
			{
				if(l2 == N-1) break;
				if(l2+1 < N && B[l2] > B[l2+1]) break;
				swap(B[l2], B[l2+1]);
				l2++;
				right++;
			}
//			fprintf(stderr, "[%d] %d %d\n", A[idx], left, right);

			if(left < right)
			{
				l2 = idx;
				while(1)
				{
					if(l2 == 0) break;
					if(l2 > 0 && A[l2] > A[l2-1]) break;
					swap(A[l2], A[l2-1]);
					swap(C[l2], C[l2-1]);
					l2--;
					Ret++;
				}
				C[l2] = 1;
			}
			else
			{
				l2 = idx;
				while(1)
				{
					if(l2 == N-1) break;
					if(l2+1 < N && A[l2] > A[l2+1]) break;
					swap(A[l2], A[l2+1]);
					swap(C[l2], C[l2+1]);
					l2++;
					Ret++;
				}
				C[l2] = 1;
			}

		}

/*		
		Cnt = 0;
		for(l1 = 0; l1 < N; l1++) A[l1] = B[l1];
		Sort1(0, N-1);
		if(Cnt < Ret) Ret = Cnt;

		Cnt = 0;
		for(l1 = 0; l1 < N; l1++) A[l1] = B[l1];
		Sort2(0, N-1);
		if(Cnt < Ret) Ret = Cnt;

		for(l1 = 0; l1+1 < N; l1++)
		{
			Cnt = 0;
			for(l2 = 0; l2 < N; l2++) A[l2] = B[l2];
			Sort1(0, l1);
			Sort2(l1+1, N-1);
			if(Cnt < Ret) Ret = Cnt;
		}
*/
		
		printf("Case #%d: %d\n", l0, Ret);

	}
}
