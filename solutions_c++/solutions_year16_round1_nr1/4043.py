#include<cstdio>
#include<conio.h>
#include<string.h>
int main()
{
	int T,cas=1;
	scanf("%i\n",&T);
	while(T--)
	{
		char S[1002],init;
		int panjang,initnumber;
		scanf("%s\n",S);
		panjang=strlen(S);
		init=S[0];
		initnumber=1;
		for(int i=1;i<panjang;i++)
		{
			if(S[0]<=S[i])
			{
				init=S[i];
				for(int j=initnumber;j>0;j--)
				{
					S[j]=S[j-1];
				}
				S[0]=init;
				initnumber++;
			}
			else
			{
				initnumber++;
			}
		}
		printf("Case #%i: %s\n",cas++,S);
	}
}
