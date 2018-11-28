#include<iostream>
using namespace std;
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<stack>
#include<map>
#include<set>
#include<string.h>
#include<math.h>
#define MOD 1000000007
#define MIN -100000000
#define MAX 100000000
#define ll long long int
/* HOPE n WILL :)
	NGU :)
	_/\_ 	*/
// MG

int main()
{
	ll t,x,r,c,i,n,k=1,temp;
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld %lld %lld",&x,&r,&c);
		temp=r*c;
		if(x==1)
		{
			printf("Case #%lld: GABRIEL\n",k);
		}
		else if(x==2)
		{
			if(temp%2==0)
			printf("Case #%lld: GABRIEL\n",k);
			else printf("Case #%lld: RICHARD\n",k);
		}
		else if(x==3)
		{
			if(temp%3==0)
			{
				if(temp==6 || temp==9 || temp==12 || temp==15)
				printf("Case #%lld: GABRIEL\n",k);
				else printf("Case #%lld: RICHARD\n",k);
			}
			else printf("Case #%lld: RICHARD\n",k);
		}
		else if(x==4)
		{
			if(temp%4==0)
			{
				if(temp==12 || temp==16)
				printf("Case #%lld: GABRIEL\n",k);
				else printf("Case #%lld: RICHARD\n",k);
			}
			else printf("Case #%lld: RICHARD\n",k);
		}
		k++;
	}
	return 0;
}