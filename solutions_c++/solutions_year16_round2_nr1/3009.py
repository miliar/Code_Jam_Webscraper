#include<cstdio>
#include<conio.h>
#include<string.h>
int main()
{
	int T,cas=1;
	scanf("%i\n",&T);
	while(T--)
	{
		int abjad[10],total,panjang,Z=0,E=0,R=0,O=0,N=0,T=0,W=0,H=0,F=0,U=0,I=0,V=0,S=0,X=0,G=0;
		abjad[0]=0;
		abjad[1]=0;
		abjad[2]=0;
		abjad[3]=0;
		abjad[4]=0;
		abjad[5]=0;
		abjad[6]=0;
		abjad[7]=0;
		abjad[8]=0;
		abjad[9]=0;
		char kalimat[2002];
		total=0;
		scanf("%s",kalimat);
		panjang=strlen(kalimat);
		for(int ii=0;ii<panjang;ii++)
		{
			if(kalimat[ii]=='Z')Z++;
			else if(kalimat[ii]=='E')E++;
			else if(kalimat[ii]=='R')R++;
			else if(kalimat[ii]=='O')O++;
			else if(kalimat[ii]=='T')T++;
			else if(kalimat[ii]=='W')W++;
			else if(kalimat[ii]=='H')H++;
			else if(kalimat[ii]=='F')F++;
			else if(kalimat[ii]=='U')U++;
			else if(kalimat[ii]=='I')I++;
			else if(kalimat[ii]=='V')V++;
			else if(kalimat[ii]=='S')S++;
			else if(kalimat[ii]=='X')X++;
			else if(kalimat[ii]=='G')G++;
			else N++;
		}
		//printf("            %i     ",Z);
		while(panjang!=0)
		{
			if(Z!=0)
			{
				abjad[0]++;
				Z--;
				E--;
				R--;
				O--;
				panjang=panjang-4;
			}
			else if(W!=0)
			{
				abjad[2]++;
				T--;
				W--;
				O--;
				panjang=panjang-3;
			}
			else if(U!=0)
			{
				abjad[4]++;
				F--;
				O--;
				U--;
				R--;
				panjang=panjang-4;
			}
			else if(F!=0)
			{
				abjad[5]++;
				F--;
				I--;
				V--;
				E--;
				panjang=panjang-4;
			}
			else if(X!=0)
			{
				abjad[6]++;
				S--;
				I--;
				X--;
				panjang=panjang-3;
			}
			else if(V!=0)
			{
				abjad[7]++;
				S--;
				E=E-2;
				V--;
				N--;
				panjang=panjang-5;
			}
			else if(G!=0)
			{
				abjad[8]++;
				//printf("delapan");
				E--;
				I--;
				G--;
				H--;
				T--;
				panjang=panjang-5;
			}
			else if(T!=0)
			{
				abjad[3]++;
				T--;
				H--;
				R--;
				E=E-2;
				panjang=panjang-5;
			}
			else if(O!=0)
			{
				abjad[1]++;
				O--;
				N--;
				E--;
				panjang=panjang-3;
			}
			else
			{
				abjad[9]++;
				N--;
				I--;
				E=E-2;
				panjang=panjang-4;
			}
			total++;
		}
		printf("Case #%i: ",cas++);
		for(int ii=0;ii<total;ii++)
		{
			if(abjad[0]!=0)
			{
				printf("0");
				abjad[0]--;
			}
			else if(abjad[1]!=0)
			{
				printf("1");
				abjad[1]--;
			}
			else if(abjad[2]!=0)
			{
				printf("2");
				abjad[2]--;
			}
			else if(abjad[3]!=0)
			{
				printf("3");
				abjad[3]--;
			}
			else if(abjad[4]!=0)
			{
				printf("4");
				abjad[4]--;
			}
			else if(abjad[5]!=0)
			{
				printf("5");
				abjad[5]--;
			}
			else if(abjad[6]!=0)
			{
				printf("6");
				abjad[6]--;
			}
			else if(abjad[7]!=0)
			{
				printf("7");
				abjad[7]--;
			}
			else if(abjad[8]!=0)
			{
				printf("8");
				abjad[8]--;
			}
			else
			{
				printf("9");
				abjad[9]--;
			}
		}
		printf("\n");
	}
}
