#include<cstdio>
int main()
{
	freopen("F:\\B-large.in","r",stdin);
	freopen("F:\\B-large.out","w",stdout);
	int T(0);
	double C(0),F(0),X(0);
	int n(0);
	double res(0);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		res=0;
		n=(int)(X/C-2/F);
		if(n<0)
			n=0;
		for(int i=0;i<n;i++)
			res+=C/(2+F*i);
		res+=X/(2+F*n);
		printf("Case #%d: %.7f\n",t,res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
