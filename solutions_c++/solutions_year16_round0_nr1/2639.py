#include <iostream>
#include <stdio.h>
#include <limits.h>
using namespace std;

typedef long long ll;

ll ans_loop(ll n)
{
	//int ret = 1;
	bool arr[10];
	for(int i=0;i<10;i++)
		arr[i]=false;
	//bool check;
	int counter=0;
	ll n1=n;
	while(1)
	{
		ll z = n1;
		while(z > 0)
		{
			if(!arr[z%10])
			{
				counter++;
				arr[z%10]=true;
			}
			z=z/10;
		}
		if(counter==10)
			break;
		n1+=n;
	}
	return n1;
}

int main()
{
	int t;
	scanf("%d",&t);
	int case1=1;
	while(t--)
	{
		ll n;
		scanf("%lld",&n);
		//printf("Case #%d: ",case1);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",case1);
		else
			printf("Case #%d: %lld\n",case1,ans_loop(n));
		case1++;
	}
}