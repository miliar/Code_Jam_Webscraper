#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
	freopen("C:\\Users\\ytimex\\Desktop\\gcj\\B-large.in","rb",stdin);
	freopen("C:\\Users\\ytimex\\Desktop\\gcj\\B-large.out","wb",stdout);
	int T,t=1;
	double C,F,X;
	scanf("%d",&T);
	while(t <=T)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		//当前生产力p1,买一个农场后生产力p2,当前到达X的时间t1
		double p1,p2,t1,t2,money,ans=0.0;
		p1 = 2.0; p2 = p1+F;
		t1 = X / p1; t2 = (C/p1)+X/(p2);
		while(t1 > t2)
		{
			ans += C/p1;
			p1 = p2;
			p2 = p1+F;
			t1 = X/p1;
			t2 = (C/p1)+X/(p2);
		}
		ans += t1;
		printf("Case #%d: %.7f\n",t,ans);
		t++;
	}
	return 0;
}
