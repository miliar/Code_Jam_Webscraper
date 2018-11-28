#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<queue>
#define S(x) scanf("%d",&x);
#define SL(x) scanf("%lld",&x);
#define SS(x) scanf("%s",&x);
#define ll long long
#define ii int
using namespace std;
int main()
{
	freopen("E:\\in.in","r",stdin);
	freopen("E:\\out.txt","w",stdout);
	ll t,i,j,k,n,m;
	ll num[42]={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,1112111,200002,2001002,100000000};
	SL(t);
	ll sqr[42];
	for(i=0;i<42;i++)
		sqr[i]=num[i]*num[i];
	k=0;
	while(k<t)
	{
		k++;
		SL(n);
		SL(m);
		for(i=0;i<42;i++)
		{
			if(sqr[i]>=n)
			{
				n=i;
				break;
			}
		}
		for(i=n;i<42;i++)
		{
			if(sqr[i]>m)
			{
				m=i;
				break;
			}
		}
//		cout<<n<<" "<<m<<endl;
		printf("Case #%lld: %lld\n",k,m-n);
	}
	return 0;
}
