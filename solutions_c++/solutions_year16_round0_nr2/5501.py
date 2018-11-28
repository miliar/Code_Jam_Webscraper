#include <bits/stdc++.h>
#include <string>
using namespace std;

char str[100],aux[100];

void troca(int f)
{
	for(int i=0;i<=f;i++)
	{
		if (str[i]=='+') aux[f-i]='-';
		else aux[f-i]='+';
	}
	for(int i=0;i<=f;i++) str[i] = aux[i];
}

int main (void)
{
	int T,t=1;
	scanf("%d",&T);
	while(t<=T)
	{
		int n,posi=0,posf,cont=0;
		scanf("%s",str);
		n=strlen(str);
		posf=n-1;
		while (posf>=0)
		{
			if ( str[posf] == '+') posf--;
			else if (str[posi] == '-') troca(posf),cont++;
			else
			{
				while (str[posi]=='+') posi++;
				troca(posi-1),cont++;
			}
			posi=0;
		}
		printf("Case #%d: %d\n",t,cont);
		t++;
	}
}
