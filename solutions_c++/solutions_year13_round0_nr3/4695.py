#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
const long long int num=1e+14;
const int num1=1e+6;
int cout;
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	cout=39;
	long long int di[100]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
	long long int A,B;
	int T;
	scanf("%d",&T);
	int cas=0;
	while(T--)
	{
		scanf("%lld%lld",&A,&B);
		//printf("%lld %lld\n",A,B);
		int nn=0;
		long long int tt;
		for(int i=0;i<cout;i++)
		{
		   tt=di[i]*di[i];
			if(tt>B)break;
			else if(tt>=A&&tt<=B)
				  nn++;
		}
		printf("Case #%d: ",++cas);
		printf("%d\n",nn);
	}
return  0;
}