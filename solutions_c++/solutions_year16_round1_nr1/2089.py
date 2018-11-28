#include <bits/stdc++.h>

int main ()
{
	int T,t=0;
	scanf("%d",&T);
	while(t++ < T)
	{
		char a[1200],b[3000];
		int pi=1110,pf=1111;
		scanf("%s",a);
		b[pi]=a[0];
		for(int i=1;i<strlen(a);i++) 
		{
			if(a[i]<b[pi]) b[pf] = a[i], pf++;
			else pi--, b[pi] = a[i];
		}
		printf("Case #%d: ",t);
		for (int i=pi;i<pf;i++) printf("%c",b[i]);
		printf("\n");
	}
	return 0;
}