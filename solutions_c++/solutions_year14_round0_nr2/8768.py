#include<cstdio>
#include<iostream>
#include<algorithm>
int main()
{
	int i,j,t,T;
	double c,f,x,m,m1,p,p1,p2;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		m=0,m1=0,p=0,p1=0,p2=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        m=2;
        p=(double)x/m;
        p1=(double)c/m;
        m=m+f;
        p2=p1+(double)x/m;
//       	if(p>p2)
        while(p>p2)
        {
            p=p2;
//            printf("p %.7lf\n",p);
            p1+=(double)c/m;
//            printf("p1 %.7lf\n",p1);
            m=m+f;
//            printf("m %.7lf\n",m);
            p2=p1+(double)x/m;
//            printf("p2 %.7lf\n",p2);
        }
//        else
//            p2=p;
        printf("Case #%d: %.7lf\n",t,p);
	}
	return 0;
}
