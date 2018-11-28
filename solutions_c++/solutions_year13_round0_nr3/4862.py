#include <stdio.h>
int ha[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,4160653865,4258500833};
int main()
{
	freopen("D:\\13.in","r",stdin);
	freopen("D:\\out.out","w",stdout);
	int t,i,ii,j,sum;
	j=23;
	__int64 a,b;
	scanf("%d",&t);ii=1;
	while (t--)
	{
		scanf("%I64d%I64d",&a,&b);
		int x1,x2;
		for (i=0;i<j&&ha[i]<a;i++);
		x1=i;
		for (i=x1;i<j&&ha[i]<=b;i++);
		x2=i;
		sum=x2-x1;
		printf("Case #%d: %d\n",ii++,sum);
	}
	return 0;
}

