/*        L I N O N Y M O U S          */

#include <iostream>
#include <algorithm>
#include <iomanip>
#include <list>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>
#include <stdbool.h>
#include <map>
#include <utility>

/* I N P U T    A N D     O U T P U T  */

#define si(a) 		scanf("%d",&a)
#define sli(a) 		scanf("%ld",&a)
#define slli(a) 	scanf("%lld",&a)
#define sf(a) 		scanf("%f",&a)
#define sd(a) 		scanf("%lf",&a)
#define ss(a) 		scanf("%s",a)
#define NL 		printf("\n")
#define pi(a) 		printf("%d",a)
#define pli(a)	 	printf("%ld",a)
#define plli(a) 	printf("%lld",a)

/*  L O O P S  */

#define TEST 		while(t--)
#define fi(a,b) 	for(i=a;i<b;i++)
#define fj(a,b)		for(j=a;j<b;j++)
#define fk(a,b) 	for(k=a;k<b;k++)
#define fx(a,b) 	for(x=a;x<b;x++)

/*  O T H E R   */

#define MAX(a,b) 	((a>b)?a:b)
#define SQUARE(a) 	(a*a)
#define MIN(a,b) 	((a<b)?a:b)
#define pb(a) 		push_back(a)
#define pf(a) 		push_front(a)

/*  HERE GOES THE CODE   */

typedef long long int ll;
typedef long int li;

using namespace std;

int main()
{
	ll t,smax,i,j,ans,cnt,x=1;
	slli(t);
	char a[10000];
	while(t--)
	{
		slli(smax);
		ss(a);
		ans=0;
		cnt=a[0]-'0';
		for(i=1;i<=smax;i++)
		{
			//printf("%lld %c\n",cnt,a[i]);
			if(cnt<i)
			{
				ans+=1;
				cnt+=1;
			}
			cnt+=(a[i]-'0');	
		}
		printf("Case #%lld: %lld\n",x,ans);
		x++;
	}
	return 0;	
}
