#include<stdio.h>
int arr[10];
void initials_arr(){
	for (int i = 0 ; i < 10 ; i++ ){
		arr[i] = 0 ;
	}

}
void find_mod(int dig ){
	int modVal;
	//printf (" \nin mod val \n");
	for( int i = 0 ; dig > 0 ; i++ ){
		modVal = dig % 10 ;
		arr[modVal] = 1 ;
		dig = dig / 10 ;
	//	printf (" %d  ", modVal);
	}
	//printf ("\nout mod val \n");
}
bool check_arr (){
	int flag = 1 ;
	//printf ("\narr val \n");
	for ( int i = 0 ; i < 10 ; i++ ){
		if( arr[i] == 0 ){
			flag = 0 ;
		}
        //printf("%d ",arr[i]);
	}
	if ( flag == 0){
		return true ;
	}
	else return false ;
}

int main(){
    int t , n , caseCount , choose_n;
    //printf("give input case \n");
    freopen("A-large (1).in","r",stdin);
    freopen("AoutputBB.txt","w",stdout);
    scanf("%d", &t );
    caseCount = t ;

    while( t != 0 ){
		initials_arr();
	    //printf("give chosen number \n");
    	scanf("%d", &n );
    	choose_n = n ;
	    int multiplier = 0 ;
	    if(choose_n == 0){
    		printf("Case #%d: INSOMNIA\n", (caseCount - t)+1);
    	}
    	else{
    		while(check_arr()){
    		multiplier ++ ;
    		n = choose_n * multiplier ;
	    	//	printf("\n	multiplier = %d ,  current choose mul = %d \n ", multiplier, n );
	    		find_mod(n);
	    	}
	        printf("Case #%d: %d\n", (caseCount - t)+1, n );
	    }
    	t--;
    }
}
