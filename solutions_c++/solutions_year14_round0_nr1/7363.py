#include <bits/stdc++.h>
using namespace std ;

int arr[5][5] ;
int arr2[5][5] ;

int main(){
int test , i, j ,k ,ans1 , ans2;
scanf("%d" ,&test) ;
for(int kase = 1 ; kase <= test ; kase++ ){
	  scanf("%d",&ans1);

	  for ( i= 1 ; i <= 4 ; i++){
	  	 for ( j = 1 ;j <= 4 ; j++)
	  	 scanf("%d" ,&arr[i][j]) ;
	  }
     scanf("%d",&ans2);
     for ( i = 1 ; i <= 4 ; i++)
     for ( j = 1 ; j <= 4 ; j++){
     	scanf("%d",&arr2[i][j]) ;
     }

     int match = 0 , ans = 0;
     for ( i = 1 ; i <= 4 ; i++)
     for ( j = 1 ; j <= 4 ; j++)
     if ( arr[ans1][i] == arr2[ans2][j]){
     match++ ; ans = arr[ans1][i] ; }
   
    // cout << match << endl;
    if ( match == 1){
    	printf("Case #%d: %d\n", kase , ans);
    }
    else if ( match == 0){
    	printf("Case #%d: Volunteer cheated!\n",kase);
    }
    else {
    	printf("Case #%d: Bad magician!\n", kase);
    }


}
return 0 ;

}