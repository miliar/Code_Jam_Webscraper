#include <cstdio>
#include <cmath>
int main()
{
	double PI=acos(-1);
	int s;
	int T,r,t,rings;

	scanf("%d",&T);
	for(int c=1;c<=T;c++)
	{
		s=0.0d;rings=0;
		scanf("%d%d",&r,&t);
		for(int i=r;s<=t;i=i+2)
		{
			s+=((i+1)*(i+1)-i*i);
			rings++;
		}
		printf("Case #%d: %d\n",c,rings-1);
	}
}