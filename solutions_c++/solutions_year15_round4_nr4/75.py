#include <stdio.h>

long long dp12[110][220] ,dp3[110][220];
long long ni[20];
int gcd(int aa ,int bb)
{
	int temp;
	while (bb)
	{
		temp=aa%bb;
		aa=bb;
		bb=temp;	
	}	
	return aa;
}
int sta[40];
int main(void)
{
	int tt ,ii;
	int n ,m;
	int i ,j ,j2;
	long long ye3 ,ye4 ,ye6;
	long long ans;
	long long mod=1000000007;
	long long dd;
	int g;
	long long mm;	
	int np;
	long long pp ,p2;
	
	mm=mod-2;
	np=0;
	while (mm)
	{	
		sta[++np]=mm&1;
		mm>>=1;
	}
	for (i=1 ; i<=12 ; i++)
	{
		pp=i;
		p2=1;
		for (j=1 ; j<=np ; j++)
		{
			if (sta[j])
			{
				p2=(p2*pp)%mod;
			}
			pp=(pp*pp)%mod;
		}
		ni[i]=p2;
	}
/*	for (i=1 ; i<=12 ; i++)
	{
		printf("%d\n" ,ni[i] );
	}*/
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&n ,&m);
		if (m%12==0)
		{
			ye3=1;
			ye4=1;												
			ye6=1;
		}
		else if (m%6==0)
		{
			ye3=1;
			ye4=0;												
			ye6=1;										
		}
		else if (m%3==0)
		{
			ye3=1;
			ye4=0;												
			ye6=0;										
		}
		else if (m%4==0)
		{
			ye3=0;
			ye4=1;												
			ye6=0;								
		}
		else
		{
			ye3=-1;
		}		
		if (ye3==-1)
		{
			if (n%3==0)
			{
				ans=2;
			}
			else 
			{
				ans=1;
			}			
		}
		else
		{
			for (i=0 ; i<=n ; i++)
			{
				for (j=1 ; j<=12 ; j++)
				{
					dp12[i][j]=0;
					dp3[i][j]=0;
				}
			}
			dp3[0][1]=1;
			dp3[2][1]=1;			
			for (i=0 ; i<=n ; i++)
			{
				for (j2=1 ; j2<=12 ; j2++)
				{
					if (j2==1||j2==3||j2==4||j2==6||j2==12)
					{
						dd=dp3[i][j2];
						
						dp12[i+1][j2]=(dp12[i+1][j2]+dd)%mod;
						
						g=j2*3/gcd(j2,3);
						dp12[i+2][g]=(dp12[i+2][g]+dd*3*ye3)%mod;
						
						g=j2*4/gcd(j2,4);
						dp12[i+3][g]=(dp12[i+3][g]+dd*4*ye4)%mod;						

						g=j2*6/gcd(j2,6);
						dp12[i+2][g]=(dp12[i+2][g]+dd*6*ye6)%mod;						
						
					}					
				}
				
				for (j2=1 ; j2<=12 ; j2++)
				{	
					dp3[i+2][j2]=(dp3[i+2][j2]+dp12[i][j2])%mod;
				}				
			}
			ans=0;
			for (j=1 ; j<=12 ; j++)
			{
				ans=(ans+dp3[n][j]*ni[j])%mod;
				ans=(ans+dp12[n][j]*ni[j])%mod;				
			}
		}
		printf("Case #%d: %d\n" ,ii ,ans);
	}

	return 0;
}
