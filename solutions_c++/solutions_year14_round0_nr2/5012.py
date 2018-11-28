#include<stdio.h>
int main()
{
    //freopen("fun.in", "r", stdin);
    //freopen("fun.out", "w", stdout);
	int T,i;
	double c,f,x,minn,n;
    double a[100000];
	scanf("%d",&T);
	for (int j = 1; j <=T; ++j)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		//printf("%lf %lf %lf\n",c,f,x);
		n=2.0;
		minn=x/n;
		a[0]=0;
        for (int i=1; ; i++)
        {
		    //printf("%.7f\n",minn);
            a[i]= c/n+a[i-1];
            n+=f;
            if (minn<(x/n+a[i]))
                break;
            else
                minn = x/n+a[i];
		}
		printf("Case #%d: %.7f\n",j,minn);
	}

	return 0;
}
