#include<cstdio>
double c,x,f;
double ab(double a)
{
	return (a<0)?-a:a;
}
int search(int l,int h)
{
	int m = (l+h)/2,p;
	double lhs,rhs,m1;
	if (h < l)
		return -1;
	m1 = m;
	lhs = f*x;
	rhs = (m1*f+2.0)*c;
	if (ab(rhs-lhs)<=0.000001 || lhs < rhs)
	{
		p = search(l,m-1);
		if (p==-1)
			return m;
		else
			return p;
	}
	else
		return search(m+1,h);
}
int main()
{
	double ans,cur;
	int t,ca=0,k,lim,i;
	scanf("%d",&t);
	while(t--)
	{
		ca++;
		scanf("%lf%lf%lf",&c,&f,&x);
		lim = x+1;
		k = search(0,lim)-1;
		cur = 2.0;
		ans = 0;
		for (i=1;i<=k;i++)
		{
			ans = ans + c/cur;
			cur = cur + f;
		}
		ans = ans + x/cur;
		printf("Case #%d: %.7lf\n",ca,ans);
	}
	return 0;
}
