#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include<algorithm>
#include <set>
#define MAX_INT 999999
#define LEN 10010*4
using namespace std;


int calc(int num,int all){//all is current ,num is accumulated

	if( all == 2){//i
	    switch(num){
	    	case 1:break;
	    	case 2:all = -1;break;
	    	case 3:all = -4;break;
	    	case 4:all = 3;break;
	    	case -1:all = -all;break;
	    	case -2:all = 1;break;
	    	case -3:all = 4;break;
	    	case -4:all = -3;break;
	    }
	}
	else if( all == 3 ){//j
	    switch(num){
	    	case 1:break;
	    	case 2:all = 4;break;
	    	case 3:all = -1;break;
	    	case 4:all = -2;break;
	    	case -1:all = -all;break;
	    	case -2:all = -4;break;
	    	case -3:all = 1;break;
	    	case -4:all = 2;break;
	    }
	}
	else if( all == 4){//k
	    switch(num){
	    	case 1:break;
	    	case 2:all = -3;break;
	    	case 3:all = 2;break;
	    	case 4:all = -1;break;
	        case -1:all = -all;break;
	    	case -2:all = 3;break;
	    	case -3:all = -2;break;
	    	case -4:all = 1;break;
	    }
	}	
	if( all == -1 || all == 1){
		return all;
	}
	return all;
}
int main(){
	FILE *fp1,*fp2;
	fp1 = fopen("C-small-attempt8.in","r");
	fp2 = fopen("C-small-attempt8.out","w");
	int T,N,L,X;

	
	fscanf(fp1,"%d",&T);
	//fprintf(fp2,"%d\n",T);
	
	for( int i = 0 ; i < T; i++){
		int flag = 0;
		char str[LEN];
		char repeated[LEN];
		int num[LEN];
		int pre[LEN];
		fscanf(fp1,"%d%d\n",&L,&X);
		fscanf(fp1,"%s",str);
		repeated[0] = '\0';
		for(int j = 0 ; j < 4 ; j++){
			strcat(repeated,str);
		}
	    //fprintf(fp2,"%s\n",repeated);
	    int l = L*2;
	    for(int j = 0 ; j < 4*L ; j++){
	    	num[j] = repeated[j] - 'i' + 2;
	    }
	    int all = num[0];

	    int a = 0;
	    int b = 0;
	    int c = 0;
	    int len1;
	    int len2;
	    int len3;
	    int len_sum = L*X;
	    int permit = X;
	    int pos = 0;
	    
	    a = num[0];
	    pre[0] = a;
	    for( int j = 1 ; j < 4*L ; j++){
	    	a = calc(a,num[j]);
	    	pre[j] = a;
	    }
	    if(pre[L-1] == 1){//1 in L
	    	fprintf(fp2,"Case #%d: NO\n",i+1);	
	    	printf("Case #%d: NO\n",i+1);
	    	continue;
	    }
	    
	    if(pre[L-1] == -1){//-1 in L
	    	for(int j = 0 ; j < L-1  && flag == 0; j++){
	    		if(pre[j] == 2){//2
	    			for(int k = j+1 ; k < L && flag == 0; k++){
	    				if(pre[k] == 4 ){
	    					if( permit >= 1 && permit % 2 == 1 ){
	    						flag = 1;
	    					}//if
	    					
	    				}//if
	    			}//for
	    			for( int k = 0 ; k < L && flag == 0; k++){
	    				if( pre[k] == 4 || pre[k] == -4){
	    					if(permit >= 3 && permit % 2 == 1){
	    					    flag = 1;
	    					}
	    				}
	    			}//for k


	    		}//if
	    		else if( pre[j] == -2){
	    			for(int k = j+1 ; k < L && flag == 0; k++){
	    				if(pre[k] == -4 ){
	    					if( permit >= 1 && permit % 2 == 1 ){
	    						flag = 1;
	    					}//if
	    					
	    				}//if
	    			}//for
	    			for( int k = 0 ; k < L && flag == 0; k++){
	    				if( pre[k] == 4 || pre[k] == -4){
	    					if(permit >= 3 && permit % 2 == 1){
	    					    flag = 1;
	    					}
	    				}
	    			}//for k
	    		}// j = -2 in L
	    		
	    	}//for
	    	
	    }// -1 in L
	    
	    L *= 2;
	    if(pre[L-1] == -1){//-1 in 2L
	    	for(int j = 0 ; j < L-1 && flag == 0; j++){
	    		if(pre[j] == 2){//2
	    			for(int k = j+1 ; k < L && flag == 0; k++){
	    				if(pre[k] == 4 ){
	    					if( permit >= 2 && permit % 4 == 2 ){
	    						flag = 1;
	    					}//if
	    					
	    				}//if
	    			}//for
	    			for( int k = 0 ; k < L && flag == 0; k++){
	    				if( pre[k] == 4 || pre[k] == -4){
	    					if(permit >= 6 && permit % 4 == 2){
	    					    flag = 1;
	    					}
	    				}
	    			}//for k
	    		}//if
	    		else if( pre[j] == -2){
	    			for(int k = j+1 ; k < L && flag == 0; k++){
	    				if(pre[k] == -4 ){
	    					if( permit >= 2 && permit % 4 == 2 ){
	    						flag = 1;
	    					}//if
	    					
	    				}//if
	    			}//for
	    			for( int k = 0 ; k < L && flag == 0; k++){
	    				if( pre[k] == 4 || pre[k] == -4){
	    					if(permit >= 6 && permit % 4 == 2){
	    					    flag = 1;
	    					}
	    				}
	    			}//for k
	    		}// j = -2 in L
	    	}//for
	    	
	    }// -1 in 2L
	    /*
	    for( int j = 0 ; j < 4*L && flag == 0 ; j++){
	    	if( pre[j] == 2){
	    		if(j < L){
	    			for(int k = 0 ; k < 4*L && flag == 0 ; k++){
	    				if(pre[k] == 4 && k > j && k < L){//[jk][-1][][1]
	    				    if(pre[L+L-1] == -1 &&permit >= 2 && ((permit-2) % 4 == 0)){ //[jk][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 1 && ((permit-1) % 2 == 0)){ //[j,k,-1][1][-1][]
	    				    	flag = 1;
	    				    }
	    				    
	    				}
	    				else if(pre[k] == 4 && k > j && k >= L && k < 2*L ){//[j][k,-1][-j][-k]	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 2 && ((permit-2) % 4 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){//[j][k][][] [-1][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				}
	    				else if(pre[k] == 4 && k > j && k >= 2*L && k < 3*L ){//[j][][k][1] [][-1]
	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-6) % 4 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){//[j][][k][] [-1][][][]
	    				    	flag = 1;
	    				    }
	    				}
	    				else if(pre[k] == 4 && k > j && k >= 3*L && k < 4*L ){ //[j][ ][ ][k][][-1]

	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){ //[j][][][k] [][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){ 
	    				    	flag = 1;
	    				    }
	    				}
	    				//end : if k > j , j < L
	    				else if(pre[k] == 4 && k < j && k < L){//[kj][-1][][][k][-1]
	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [kj][][][] [k][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}
	    				//end: if k < j, j < L
	    				else if(pre[k] == -4 && k > j && k < L){//[j,-k][k][][]

	    				}
	    				else if(pre[k] == -4 && k > j && k >= L){//[j,-k][k][][]

	    				}
	    				else if(pre[k] == -4 && k < j && k < L){//[j,-k][k][][]

	    				}
  
	    			}//for k
	    			
	    		}//end if : j < L
	    		else if(j >= L && j < 2 * L){
	    			for(int k = 0 ; k < 4*L && flag == 0 ; k++){
				        if(pre[k] == 4 && k > j && k < j && k < L){//[k][j][][][k][-1]
    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [k][j][][] [k][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}//if k == 4
	    				else if(pre[k] == 4 && k < j && k >= L && k < 2 * L){//[][kj][][] [][k,-1]

	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [][kj][][] [][k][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    else if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}//if k == 4
	    				else if(pre[k] == 4 && k > j && k < 2*L){//[][j,k,-1][] 
    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 2 && ((permit-2) % 4 == 0)){// [][j,k,-1][][] [][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}//if k == 4
	    			    else if(pre[k] == 4 && k > j && k >= 2*L && k < 3*L){//[][j][k][] [][-1]

	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [][j][k][] [][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}//if k == 4
	    				else if(pre[k] == 4 && k > j && k >= 3*L && k < 4*L){//[][j][][k] [][-1]

	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [][j][][k] [][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    
	    				}//if k == 4   				
					}//for k
					
	    		}//if j >= L, j < 2L
	    		
				else if(j >= 2*L && j < 3 * L){
	    			for(int k = 0 ; k < 4*L && flag == 0 ; k++){
				        if(pre[k] == 4 && k > j && k < j && k < L){//[k][][j][] [k][-1][][]
	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [k][][j][] [k][-1][][] 
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    
	    				}//if k == 4
	    				else if(pre[k] == 4 && k < j && k >= L && k < 2 * L){//[][k][j][] [][k,-1][][]

	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [][k][j][] [][k,-1][][] [][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 9 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				}//if k == 4
	    				else if(pre[k] == 4 && k < j && k >= 2*L && k < 3 * L){//[][][kj][] [][][k][] [][-1][][]

	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 10 && ((permit-2) % 4 == 0)){ //[][][kj][] [][][k][] [][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 9 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    
	    				}//if k == 4
	    				else if(pre[k] == 4 && k > j && k < 3*L){//[][][jk][] [][-1]
	    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [][][jk][] [][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    
	    				}//if k == 4
	    				else if(pre[k] == 4 && k > j && k >= 3*L && k < 4*L){//[][j][][k] [][-1]
	    				   if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){// [][j][][k] [][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}//if k == 4   				
					}//for k
					
	    		}//j >= 2*L && j < 3 * L
	    		
	    		else if(j >= 3*L && j < 4 * L){
	    			for(int k = 0 ; k < 4*L && flag == 0 ; k++){
				        if(pre[k] == 4 && k > j && k < j && k < L){//[k][][][j] [k][-1][][]

	    				    
							if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){//[k][][][j] [][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				}//if k == 4
	    				else if(pre[k] == 4 && k < j && k >= L && k < 2 * L){//[][k][][j] [][k,-1][][]
	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){ //[][k][][j] [][k,-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 9 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}//if k == 4
	    				else if(pre[k] == 4 && k < j && k >= 2*L && k < 3 * L){//[][][k][j] [][][k][] [][-1][][]

	    				    if(pre[L+L-1] == -1 &&permit >= 10 && ((permit-2) % 4 == 0)){// [][][k][j] [][][k][] [][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 9 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    
	    				}//if k == 4
	    				else if(pre[k] == 4 && k < j && k >= 3*L && k < 4 * L){//[][][][kj] [][][][k]  [][-1][][]
    				    
	    				    if(pre[L+L-1] == -1 &&permit >= 10 && ((permit-2) % 4 == 0)){// [][][][kj] [][][][k] [][][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 9 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				    
	    				    
	    				}//if k == 4
	    				else if(pre[k] == 4 && k > j && k >= 3*L && k < 4*L){//[][][][jk] [][-1][][]

	    				    if(pre[L+L-1] == -1 &&permit >= 6 && ((permit-2) % 4 == 0)){ //[][][][jk] [][-1][][]
	    				    	flag = 1;
	    				    }
	    				    
	    				    if(pre[L-1] == -1 && permit >= 5 && ((permit-1) % 2 == 0)){
	    				    	flag = 1;
	    				    }
	    				}//if k == 4   				
					}//for k
					
	    		}//j >= 3*L && j < 4 * L
	    		
	    	}//if pre[j] == 2
	    }//for j
	    
	   */
	    if(flag == 0){
	        fprintf(fp2,"Case #%d: NO\n",i+1);	
			printf("Case #%d: NO\n",i+1);
        }else if(flag == 1){
        	fprintf(fp2,"Case #%d: YES\n",i+1);		
        	printf("Case #%d: YES\n",i+1);
        }
        
	}
	
	
	fclose(fp1);
	fclose(fp2);
	return 0;
	
}
