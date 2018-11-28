#include<bits/stdc++.h>
using namespace std;
main()
{
	freopen("B-small-attempt5.in","r",stdin);
	freopen("out-B-small.txt","w",stdout);
	int a,b,c;
	double d,e,edx,edy,stx1,stx2,sty1,sty2;
	scanf("%d",&a);
	for(b=1;b<=a;b++)
	{
		scanf("%d",&c);
		scanf("%lf %lf",&edx,&edy);
		if(c==1)
		{
			scanf("%lf %lf",&stx1,&sty1);
			if(sty1==edy)printf("Case #%d: %lf\n",b,edx/stx1);
			else printf("Case #%d: IMPOSSIBLE\n",b);
		}
		else if(c==2)
		{
			scanf("%lf %lf",&stx1,&sty1);
			scanf("%lf %lf",&stx2,&sty2);
			if(min(sty1,sty2)>edy||max(sty1,sty2)<edy)printf("Case #%d: IMPOSSIBLE\n",b);
			else
			{
				if(sty1>sty2)swap(sty1,sty2),swap(stx1,stx2);
				if(sty1==sty2&&sty1==edy)printf("Case #%d: %lf\n",b,edx/(stx1+stx2));
				else if(edy==sty1)printf("Case #%d: %lf\n",b,edx/stx1);
				else if(edy==sty2)printf("Case #%d: %lf\n",b,edx/stx2);
				else
				{
					d=(edy-sty2)/(sty1-edy);
					e=max(stx2*d/stx1,1.00);
					//printf("[%lf %lf]",d,e);
					printf("Case #%d: %lf\n",b,edx*e/(stx2*(1+d)));
				}
			}
		}
	}
}
