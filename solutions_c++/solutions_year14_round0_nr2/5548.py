#include<bits/stdc++.h>
using namespace std;

long	double ar[201000],dn[201000],fabi[201000];
int N;
void oku ()
{		
		long	double fab,ka,mal,bol;
		scanf(" %d",&N)	;
		for(int j=1 ; j<=N ;j++)
		{ 
			scanf(" %Lf %Lf %Lf",&fab,&ka,&mal);
			bol=2.0;
			ar[0]=mal/bol;
			dn[0]=2.0;
			fabi[0]=0.0;
			for(int i=1 ; i ;i++)
			{		
					fabi[i]=fabi[i-1]+fab/dn[i-1];
					dn[i]=dn[i-1]+ka;
					ar[i]=fabi[i]+(mal/dn[i]);
					if(ar[i]>ar[i-1])
					{printf("Case #%d: %.7Lf\n",j,ar[i-1]);break;}
			}
		}
				
	
		
		
}


int main ()
{
		oku ();
		return  0;
}
