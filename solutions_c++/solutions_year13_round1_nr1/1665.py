#include <stdio.h>
using namespace std;
int main()
{
	int ca,tt,r,t;
	int s,num;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&tt);
	for (ca=1;ca<=tt;ca++)
	{
		scanf("%d%d",&r,&t);
		s=0;num=0;
		while (s<=t)
		{
			s=s+(r+1)*(r+1)-r*r;
			r=r+2;
			num++;
		}
		printf("Case #%d: %d\n",ca,num-1);
	}
	return 0;
}
