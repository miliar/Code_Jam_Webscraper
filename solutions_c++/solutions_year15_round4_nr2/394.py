#include<cstdio>
#include<algorithm>

double v[111];
double t[111];

std::pair<double,int> d[111];
int dn;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int tc,tcn;
    scanf("%d",&tcn);
    for(tc=1;tc<=tcn;tc++)
	{
		bool p,m;
		double tot;
		double V,T,R,TT;
        int i,n;
        scanf("%d%lf%lf",&n,&V,&T);
        p=m=false;
        tot=0.0;
        for(i=0;i<n;i++)
		{
			scanf("%lf%lf",&v[i],&t[i]);
			tot+=v[i]*(t[i]-T);
			if(t[i]>=T-0.00005)p=true;
			if(t[i]<=T+0.00005)m=true;
		}
		if(!p||!m)
		{
			printf("Case #%d: IMPOSSIBLE\n",tc);
			continue;
		}
		R=TT=0.0;
		dn=0;
		if(tot<0)
		{
			for(i=0;i<n;i++)
			{
				if(t[i]>=T-0.00005)
				{
					TT+=(t[i]-T)*v[i];
					R+=v[i];
				}
                else
				{
					d[dn].first=t[i]-T;
                    d[dn].second=i;
                    dn++;
				}
			}
			std::sort(d,d+dn);
            for(i=dn-1;i>=0;i--)
			{
				if(TT+d[i].first*v[d[i].second]>0)
				{
					TT+=d[i].first*v[d[i].second];
                    R+=v[d[i].second];
				}
                else
                {
                	R-=TT/d[i].first;
                	break;
                }
			}
		}
		else
		{
			for(i=0;i<n;i++)
			{
				if(t[i]<=T+0.00005)
				{
					TT+=(t[i]-T)*v[i];
					R+=v[i];
				}
                else
				{
					d[dn].first=t[i]-T;
                    d[dn].second=i;
                    dn++;
				}
			}
			std::sort(d,d+dn);
            for(i=dn-1;i>=0;i--)
			{
				if(TT+d[i].first*v[d[i].second]<0)
				{
					TT+=d[i].first*v[d[i].second];
                    R+=v[d[i].second];
				}
                else
                {
                	R-=TT/d[i].first;
                	break;
                }
			}
		}
		printf("Case #%d: %.12lf\n",tc,V/R);
	}
}
