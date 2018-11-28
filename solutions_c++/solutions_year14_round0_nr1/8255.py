#include <bits/stdc++.h>
using namespace std ;
int a2[5][5] ;
int a1[5][5] ;
int main()
{
	int ntc, g2 , g1,j, k ,i ;
	scanf("%d" ,&ntc) ;

	for(int loopVar = 1 ; loopVar <= ntc ; loopVar++ )
	{
		  scanf("%d",&g1);
		  for ( i= 1 ; i <= 4 ; i++)
		  {
	  	 	for ( j = 1 ;j <= 4 ; j++)
	  	 	scanf("%d" ,&a1[i][j]) ;
	  	  }
		  scanf("%d",&g2);
	          for ( i = 1 ; i <= 4 ; i++)
     			for ( j = 1 ; j <= 4 ; j++)
			{
     				scanf("%d",&a2[i][j]) ;
     			}
		  int match = 0 , answer = 0;
     		  for ( i = 1 ; i <= 4 ; i++)
     		  	for ( j = 1 ; j <= 4 ; j++)
     				if ( a1[g1][i] == a2[g2][j]){
     		  match++ ; answer = a1[g1][i] ; 
	}
   
       
        if ( match == 1)
	{
    		printf("Case #%d: %d\n", loopVar , answer);
    	}
    	else if ( match == 0)
	{
	    	printf("Case #%d: Volunteer cheated!\n",loopVar);
	}
    	else 
	{
    		printf("Case #%d: Bad magician!\n", loopVar);
    	}

  }
  return 0 ;
}
