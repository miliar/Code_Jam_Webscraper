#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	short int t,la,lb,n,i,c_no=0,countd,countf;
	scanf("%hd",&t);
	while(t--)
	{
		c_no++;
		scanf("%hd",&n);
		float a[n],b[n];
		for(i=0;i<n;i++)
			scanf("%f",&a[i]);
		for(i=0;i<n;i++)
			scanf("%f",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		lb=0;
		countd=0;
		countf=0;
		for(i=0;i<n;i++)
		{
			if(b[lb]<a[i])
			{
				countd++;
				lb++;
			}
		}
		short int hb=n-1;
		for(i=n-1;i>=0;i--)
		{
			if(a[i]>b[hb])
				countf++;
			else
				hb--;
		}
		printf("Case #%hd: %hd %hd\n",c_no,countd,countf);
	}
}
