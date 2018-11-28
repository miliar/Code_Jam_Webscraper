#include<cstdio>

int main()
{
//	freopen("E:/in.txt","r",stdin);
//	freopen("E:/out.txt","w",stdout);
	int T,t,i;
	double s,c,f,x,tl,t0,t1;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		s=2.0;
		t0=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		tl=x/s;
		for(i=1;;i++)
		{
			t0+=c/s;
			s+=f;
			t1=x/s;
			if(t0+t1<tl)
				tl=t0+t1;
			else
				break;
		}
		printf("Case #%d: %.10f\n",t,tl);
	}
	return 0;
}
