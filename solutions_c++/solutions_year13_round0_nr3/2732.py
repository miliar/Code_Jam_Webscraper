#include<stdio.h>
#include<string.h>
#include<math.h>
const int N=1050;
int s[N];
bool isMagic(int x)
{
	char buf[100];
	sprintf(buf,"%d",x);
	int len=strlen(buf);
	int k=len/2,i;
	for(i=0;i<k;i++)
		if(buf[i]!=buf[len-i-1])
			return false;
	return true;
}
int main()
{
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("output","w",stdout);
	int t,cnt,a,b,i,r;
	for(i=1;i<=N;i++)
		s[i]=i*i;
	scanf("%d",&t);
	for(cnt=1;cnt<=t;cnt++)
	{
		r=0;
		scanf("%d%d",&a,&b);
		i=sqrt(a);
		if(i*i<a)
			i++;
		for(;i*i<=b;i++)
		{
			if(isMagic(i)&&isMagic(i*i))
			{
				r++;
			}
		}
		printf("Case #%d: %d\n",cnt,r);
	}
	return 0;
}