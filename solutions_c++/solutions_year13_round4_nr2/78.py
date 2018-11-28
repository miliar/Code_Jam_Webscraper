#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
#define LL long long

int K;
LL P,N;

void run()
{
	scanf("%d %I64d", &K, &P); --P;
	N = 1ll << K;
	
	LL lo, hi, mid;
	
	// must win --> exist one case > P
	// keep most A
	lo = 0, hi = N;
	while(lo + 1 < hi)
	{
		mid = lo + hi >> 1;
		LL m = mid;
		LL A = m, B = N - m - 1;
		bool lose = false;
		for(int k=0;k<K;++k)
		{
			int t = !!(P & 1ll <<K-1- k);
			if(t == 0) 
			{
				if(A > 0) // lose
				{
					lose = true;
					break;
				} // no A, only win
				-- B;
				B >>= 1;
			} else // only lose
			{// keep most A
				if(A == 0) break; // cannot lose
				-- A;
				if(A & 1) {
					A = A-1 >> 1;
					B = B + 1 >> 1;
				} else{
					A >>= 1;
					B >>= 1;
				}
			}
		}
		if(lose) hi = mid;
		else lo = mid;
	}
	
	printf("%I64d ", lo);
	
	//exist one case <= P
	lo = 0, hi = N;
	while(lo + 1 < hi)
	{
		mid = lo + hi >> 1;
		LL m = mid;
		LL A = m, B = N - m - 1;
		bool win = true;
		for(int k=0;k<K;++k)
		{
			int t = !!(P & 1ll << K-1-k);
			if(t == 1)
			{
				if(B > 0) {win=true; break;}
				-- A;
				A >>= 1;
			} else
			{// must win
				if(B == 0){win=false; break;}// cannot win
				-- B;
				if(A & 1) {
					A = A + 1 >> 1;
					B = B - 1 >> 1;
				} else{
					A>>=1;B>>=1;
				}
			}
		}
		if(win) lo = mid;
		else hi = mid;
	}
	printf("%I64d\n", lo);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int test;
	scanf("%d", &test);
	for(int no=1;no<=test;++no) {
		printf("Case #%d: ", no);
		run();
	}
}
