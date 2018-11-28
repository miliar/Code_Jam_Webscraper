#include<bits/stdc++.h>
using namespace std;
int tab[100000001];
int czy[10];
int ile;
void akt(int x)
{
	while(x>0)
	{
		ile+=1-czy[x%10];
		czy[x%10]=1;
		x/=10;
	}
	return;
}
int main()
{
	int n;
	scanf("%d", &n);
	for(int i=1; i<=1000000; i++)
	{
		int x=0;
		for(int j=0; j<10; j++)
			czy[j]=0;
		ile=0;
		while(ile<10)
		{
			x+=i;
			akt(x);
		}
		tab[i]=x;
	}
	for(int i=1; i<=n; i++)
	{
		int a;
		scanf("%d", &a);
		if(a==0)
			printf("Case #%d: INSOMNIA\n", i);
		else
			printf("Case #%d: %d\n", i, tab[a]);
	}



}
