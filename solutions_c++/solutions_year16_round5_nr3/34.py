#include <stdio.h>
#include <math.h>

double max(double aa ,double bb)
{
	if (aa>bb)
	{
		return aa;	
	}
	return bb;
}
double min(double aa ,double bb)
{
	if (aa<bb)
	{
		return aa;	
	}
	return bb;
}
double x[1010] ,y[1010] ,z[1010];
double vx[1010] ,vy[1010] ,vz[1010];
double dis[1010];
int vis[1010];
int main(void)
{
	int tt ,ii;
	int n ,s ,i;
	double ans;
	double LAR=1000000000;
	double tempd;
	int tempp;
	int p;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&n ,&s);
		for (i=1 ; i<=n ; i++)
		{
			scanf("%lf %lf %lf %lf %lf %lf" ,&x[i] ,&y[i] ,&z[i] ,&vx[i] ,&vy[i] ,&vz[i]);
		}
		for (i=1 ; i<=n ; i++)
		{
			vis[i]=1;
			dis[i]=LAR;
		}
		ans=0;
		p=1;
		while (p!=2)
		{
			vis[p]=0;
			for (i=1 ; i<=n ; i++)
			{
				dis[i]=min(dis[i],sqrt((x[p]-x[i])*(x[p]-x[i])+(y[p]-y[i])*(y[p]-y[i])+(z[p]-z[i])*(z[p]-z[i])));
			}
			tempd=LAR;
			for (i=1 ; i<=n ; i++)
			{
				if (vis[i])
				{
					if (dis[i]<tempd)
					{
						tempd=dis[i];
						tempp=i;
					}
				}
			}			
			p=tempp;
			ans=max(ans,tempd);
		}
		printf("Case #%d: %.7f\n" ,ii ,ans);
	}
	
	return 0;
}
