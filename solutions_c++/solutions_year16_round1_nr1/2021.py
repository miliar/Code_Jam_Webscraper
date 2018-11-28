#include <bits/stdc++.h>

int main ()
{
	int T,t=0;
	scanf("%d",&T);
	while(t++ < T)
	{
		char a[1200],b[3000];
		int posi=1110,posf=1111;
		scanf("%s",a);
		b[posi]=a[0];
		for(int i=1;i<strlen(a);i++) 
		{
			if(a[i]<b[posi]) b[posf] = a[i], posf++;
			else posi--, b[posi] = a[i];
		}
		printf("Case #%d: ",t);
		for (int i=posi;i<posf;i++) printf("%c",b[i]);
		printf("\n");
	}
}