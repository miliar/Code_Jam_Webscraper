#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
//#include<conio.h>

#define MOD 1000000007

using namespace std;

int main()
{
int c,t;
long long int r,paint,sum,term,n;
scanf("%d",&t);

for(int c=1;c<=t;c++)
{
    scanf("%lld%lld",&r,&paint);
    n=1;
	long long int ctr=0;
	sum=0;

	while(sum<=paint)
	{
		term=2*r+(4*n-3);
		sum=sum+term;
		n++;
		ctr++;
	}

	ctr--;

	printf("\nCase #%d: %lld",c,ctr);
}

//	getch();
	return 0;
}
