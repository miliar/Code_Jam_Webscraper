#include<bits/stdc++.h>
using namespace std;

int N,M,T,ar[100][100],used[100],be[100][100];

void oku ()
{
		scanf(" %d",&N);
		
		
		for(int i=1 ; i<=N ;i++)
		{
				scanf(" %d",&M);
				for(int j=1 ; j<=4 ;j++)
					for(int k=1 ; k<=4 ;k++)
						scanf(" %d",&ar[j][k]);
				scanf(" %d",&T);
				for(int j=1 ; j<=4 ;j++)	
					for(int k=1 ; k<=4 ;k++)
						scanf(" %d",&be[j][k]);
				int top=0,tut;
				for(int j=1 ; j<=4 ;j++)
					for(int k=1 ; k<=4 ;k++)
						if(ar[M][j]==be[T][k] &&!used[k])
						{top++;tut=ar[M][j];used[k]=1;break;}
				for(int m=1 ; m<=10 ;m++)
					used[m]=0;
				if(top==1)
					printf("Case #%d: %d\n",i,tut);
				if(top>1)
					printf("Case #%d: Bad magician!\n",i);
				if(!top)
					printf("Case #%d: Volunteer cheated!\n",i);
		}
		
		
}

int main ()
{
		oku ();
		return 0;
		
}
