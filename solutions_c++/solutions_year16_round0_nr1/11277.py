#include<cstdio>
using namespace std;
bool isappeared[10];
int count;

void init()
{
	int i;
	for(i=0;i<=9;i++)
	  isappeared[i]=false;
	count=0;
}

int work(int n)
{
	int i=1,t,dig,x;
	x=n;
	while(1)
	{
		t=n;
		while(t!=0)
		{
			dig=t%10;
			if(isappeared[dig]==false)
			{
				isappeared[dig]=true;
				count++;
			}
			t/=10;
		}
		if(count!=10)
		{
			i++;
			n=x*i;
		}
		else
		  break;
	}
	return n;
}

int main()
{
	//freopen("CountingSheep.in","r",stdin);
	//freopen("CountingSheep.out","w",stdout);
	int i,n,t;
	
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		init();
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",i);
			continue;
		}
		printf("Case #%d: %d\n",i,work(n));
	}
	return 0;
}
