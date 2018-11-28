#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>

using namespace std;

int T;
int N;
long double V, X;
long double ret;
long double A[111], B[111];
long double EPS = 1e-12;

int equal(long double v1, long double v2)
{
	long double diff = v1 - v2;

	if(-EPS < diff && diff < EPS)
	{
		return 1;
	}

	if(v1 < -EPS || v1 > EPS)
	{
		long double diff2 = diff / v1;
		if(-EPS < diff2 && diff2 < EPS) return 1;
	}
	if(v2 < -EPS || v2 > EPS)
	{
		long double diff2 = diff / v2;
		if(-EPS < diff2 && diff2 < EPS) return 1;
	}

	return 0;
}

int main(void)
{
	int l1, l2;
	int l0;

	cin >> T;
	for(l0 = 1; l0 <= T; l0++)
	{
		cin >> N >> V >> X;

		for(l1 = 0; l1 < N; l1++) cin >> A[l1] >> B[l1];

		ret = 1e100;

		for(l1 = 0; l1 < N; l1++)
		{
			if(equal(B[l1], X))
			{
				long double curr = V / A[l1];
				if(curr < ret) ret = curr;
			}
		}
		if(N == 2)
		{
			if(equal(B[0], X) && equal(B[1], X))
			{
				long double curr = V / (A[0] + A[1]);
				if(curr < ret) ret = curr;
			}

			else if(equal(B[0], X) == 0 && equal(B[1], X) == 0)
			{
				long double ratio = (X - B[0]) / (B[1] - X);
				if(0 < ratio)
				{
					long double up = 1;
					long double down = ratio * A[0] / A[1];
					long double div = A[0] * up + A[1] * down;
					long double curr = V / div;
					curr *= max(up, down);
					if(curr < ret) ret = curr;
				}
			}
		}

		if(ret > 1e99)
		{
			printf("Case #%d: IMPOSSIBLE\n", l0);
		}
		else
		{
			printf("Case #%d: %.12Lf\n", l0, ret);
		}
	}
}
