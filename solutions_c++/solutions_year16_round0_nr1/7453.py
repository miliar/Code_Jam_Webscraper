#include <stdio.h>
#include <conio.h>

int main()
{
	int i,j,k,N,flag[10],T,cas=1;
	scanf("%i\n",&T);
	while(T--)
	{
		scanf("%i\n",&N);
		if(N==0) printf("Case #%i: INSOMNIA\n",cas++);
		else 
		{
			int flagangka=10,Ni=1,hasilakhir,hasil=0,hasilmodulo=0;
			flag[0]=0;
			flag[1]=0;
			flag[2]=0;
			flag[3]=0;
			flag[4]=0;
			flag[5]=0;
			flag[6]=0;
			flag[7]=0;
			flag[8]=0;
			flag[9]=0;
			while(flagangka)
			{
				flagangka=10;
				hasil=N*Ni++;
				hasilakhir=hasil;
				while(hasil)
				{
					hasilmodulo=hasil%10;
					hasil=hasil/10;
					flag[hasilmodulo]=1;
				}
				for(i=0;i<10;i++)
				{
					if(flag[i]==1)flagangka--;
				}
			}
			printf("Case #%i: %i\n",cas++,hasilakhir);
		}
	}
}
