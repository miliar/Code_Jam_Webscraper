#include<cstdio>
#include<cstdlib>
#include<cmath>
int main()
{
	int T;
	scanf("%d",&T);
	for (int ri=0;ri<T;ri++)
	{
		double X,F,C,sum,now,t1,t2;
		int tp;
		scanf("%lf%lf%lf",&C,&F,&X);
	//	now=0;
		sum=0;
		tp=0;
		for (;1;)
		{
			t1=X/(tp*F+2)+sum;
			t2=X/((tp+1)*F+2)+sum+C/(tp*F+2);
			if (t1>t2)
			{
				sum=sum+C/(tp*F+2);
				tp++;
			}
			else
			{
				sum=t1;
				break;
			}
		}
		printf("Case #%d: %.7lf\n",ri+1,sum);
	}
}
