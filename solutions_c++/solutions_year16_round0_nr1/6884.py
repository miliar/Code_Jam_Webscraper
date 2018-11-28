#include<bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long int
#define MOD 1000000007

using namespace std; 

int A[10];

void fun_add(int a)
{
	while(a)
	{
		A[a%10]++;
		a/=10;
	}
	return;
}

bool check()
{
	int i;
	for(i=0;i<10;i++)
		if(!A[i])
			break;
	if(i==10)
		return 1;
	else
		return 0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outpt.txt","w",stdout);
	int t,n,g;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		for(int i=0;i<10;i++)
			A[i]=0;
		cin>>n;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",k);
			continue;
		}
		g=n;
		while(1)
		{
			fun_add(g);
			if(check())
				break;
			g+=n;
			assert(g<2000000000);
		}
		printf("Case #%d: %d\n",k,g);
	}
	return 0;
}
