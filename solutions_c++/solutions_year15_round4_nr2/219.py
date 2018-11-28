#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXN 200

int N,T;
struct water
{
	double r,c;
	water(double r = 0, double c = 0)
	{
		this->r = r;
		this->c = c;
	}
	bool operator < (const water &a) const
	{
		return c < a.c;
	}
}W[MAXN],F;

water mix(const water &a, const water &b)
{
	water ret;
	ret.r = a.r + b.r;
	ret.c = (a.r*a.c + b.r*b.c) / (a.r + b.r);
	return ret;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		scanf("%d%lf%lf",&N,&F.r,&F.c);
		for (int i=0;i<N;i++)
		{
			scanf("%lf%lf",&W[i].r,&W[i].c);
		}
		sort(W,W+N);
		double l = 0, r = 0, sr = 0;
		r = max(F.r / W[N-1].r, F.r / W[0].r);
		for (int i=0;i<N;++i)
		{
			
			sr += W[i].r;
		}
		l = F.r / sr;
		if (F.c < W[0].c || F.c > W[N-1].c)
		{
			l = -2;
			goto PRINT;
		}
		while (r - l > 5e-9)
		{
			double m = (l+r) / 2;
			water wlow, whigh;
			wlow.r = 0;
			whigh.r = 0;
			
			for (int i=0;i<N;++i)
			{
				if (wlow.r + m * W[i].r >= F.r)
				{
					wlow = mix(wlow, water(F.r - wlow.r, W[i].c));
					break;
				}
				wlow = mix(wlow, water(m * W[i].r, W[i].c));
			}
			
			
			for (int i=N-1;i>=0;i--)
			{
				if (whigh.r + m * W[i].r >= F.r)
				{
					whigh = mix(whigh, water(F.r - whigh.r, W[i].c));
					break;
				}
				whigh = mix(whigh, water(m * W[i].r, W[i].c));
			}
			
			if (F.c >= wlow.c && F.c <= whigh.c)
			{
				r = m;
			}
			else
			{
				l = m;
			}
			
		}
	PRINT:
		printf("Case #%d: ", cases);
		if (l < -1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%.8f\n", l);
		}
		fflush(stdout);
	}
    return 0;
}
