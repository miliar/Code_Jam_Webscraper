#include <cstdio>
#include <algorithm>
#define abs(x) ((x)>0?(x):(-(x)))
#define eps 1e-12
int T,cas,n,i,z[111],f[111],ti[111],nf,nz,j;
double l,r,mi,td[111],sp,P[111],zc[111],fc[111],R[111],C[111],A,B,sz,sf,dlt;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
//		printf("cas %d\n", cas);
		scanf("%d%lf%lf", &n, &B, &A);
		nf = nz = 0;
		long double mxc = -1, mnc = 1e50;
		for (i=1; i<=n; ++i)
		{
			scanf("%lf%lf", &R[i], &C[i]);
			if (C[i] > mxc) mxc = C[i];
			if (C[i] < mnc) mnc = C[i];
			if (C[i] < A)
			{
				f[++nf] = i;
				fc[nf] = A-C[i];
			} else
			{
				z[++nz] = i;
				zc[nz] = C[i]-A;
			}
		}
		if (A > mxc+eps || A < mnc-eps)
		{
				printf("Case #%d: ", cas);
				printf("IMPOSSIBLE\n");
				continue;
		}
		sz = sf = 0;
		for (i=1; i<=nf; ++i) sf += R[f[i]]*fc[i];
		for (i=1; i<=nz; ++i) sz += R[z[i]]*zc[i];
		if (sf > sz)
		{
			memcpy(ti, f, sizeof(f));
			memcpy(f, z, sizeof(z));
			memcpy(z, ti, sizeof(ti));
			memcpy(td, fc, sizeof(fc));
			memcpy(fc, zc, sizeof(zc));
			memcpy(zc, td, sizeof(td));
			i=nf; nf=nz; nz=i;
		}
		for (i=1; i<nz; ++i)
		for (j=i+1; j<=nz; ++j)
		if (zc[i] < zc[j])
		{
			long double tmpd = zc[i];
			zc[i] = zc[j];
			zc[j] = tmpd;
			long double tmpi = z[i];
			z[i] = z[j];
			z[j] = tmpi;
		}
		
		l=0; r=1e8+10;
		while (r-l > 1e-8)
		{
	//		printf("l=%.10lf r=%.10lf\n", l, r);
			mi = (l+r)/2;
			sp = 0;
			for (i=1; i<=n; ++i)
			{
				P[i] = mi*R[i];
				sp += P[i];
			}
			dlt = 0;
			for (i=1; i<=nz; ++i) dlt += zc[i]*P[z[i]];
			for (i=1; i<=nf; ++i) dlt -= fc[i]*P[f[i]];
			if (abs(dlt) > eps)
			{
				for (i=1; i<=nz; ++i)
				{
					if (dlt-P[z[i]]*zc[i] > 0)
					{
						dlt -= P[z[i]]*zc[i];
						sp -= P[z[i]];
					} else
					{
						sp -= dlt/zc[i];
						break;
					}
					if (abs(dlt) < eps) break;
				}
			}
			if (sp > B) r = mi; else l = mi;
		}
		printf("Case #%d: ", cas);
		if (r > 1e8) printf("IMPOSSIBLE\n"); else printf("%.8lf\n", r);
	}
	return 0;
}
					
