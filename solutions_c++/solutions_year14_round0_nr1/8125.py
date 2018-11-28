#include <bits/stdc++.h>
using namespace std ;
int array2[5][5] ;
int array1[5][5] ;
int main()
{
	int noTestCase, guess1 , guess2,i, j ,k ;
	scanf("%d" ,&noTestCase) ;
	for(int loopVar = 1 ; loopVar <= noTestCase ; loopVar++ )
	{
		  scanf("%d",&guess1);
		  for ( i= 1 ; i <= 4 ; i++)
		  {
	  	 	for ( j = 1 ;j <= 4 ; j++)
	  	 	scanf("%d" ,&array1[i][j]) ;
	  	  }
		  scanf("%d",&guess2);
	          for ( i = 1 ; i <= 4 ; i++)
     			for ( j = 1 ; j <= 4 ; j++)
			{
     				scanf("%d",&array2[i][j]) ;
     			}
		  int match = 0 , ans = 0;
     		  for ( i = 1 ; i <= 4 ; i++)
     		  	for ( j = 1 ; j <= 4 ; j++)
     				if ( array1[guess1][i] == array2[guess2][j]){
     		  match++ ; ans = array1[guess1][i] ; 
	}
   
       // cout << match << endl;
        if ( match == 1)
	{
    		printf("Case #%d: %d\n", loopVar , ans);
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
