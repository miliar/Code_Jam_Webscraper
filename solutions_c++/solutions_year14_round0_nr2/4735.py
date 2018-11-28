#include<stdio.h>
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	float c,f,x,inti,a,b,d,flag=0,ans; int it;
	for(it=0;it<test;it++)
	{
		scanf("%f %f %f",&c,&f,&x);
		inti=2; ans=0;
		while(flag!=1)
		{
			a=x/inti;
			b=inti+f;
			d=(c/inti)+(x/b);
			if(d<a)
			ans=ans+(c/inti);
			else
			{
				ans=ans+(x/inti);
				break;
			}
			inti=inti+f;
		}
		printf("Case #%d: ",it+1);
		printf("%.07f\n",ans);
	}
	return 0;
}
