#include <cstdio>  
#include<iostream>
#include <cstring>  
#include <algorithm>  
using namespace std ;  
int a[1200] ;  
int main() {  
    int t , step = 0 ;  
    int n , i , j , max1=0, min1=0, sum ;  
    FILE* fp1;
	FILE* fp2;
	fp1=fopen("input.in","rt+");
	fp2=fopen("output.in","wt+"); 
    fscanf(fp1,"%d",&t) ;  
    while( t-- ) {  
        fscanf(fp1,"%d", &n) ;  
        
        for(i = 0 ; i < n ; i++) {  
            fscanf(fp1,"%d", &a[i]) ;  
            max1 = max(max1,a[i]) ;
        }  
        
        min1 = max1 ; 
		//cout<<max1<<endl; 
        for(i = 1 ; i <= max1 ; i++) {  
            sum = i ;  
            
            for(j = 0 ; j < n ; j++) {  
                if( a[j] > i ) {  
                    if( a[j]%i == 0 )  
                        sum += (a[j]/i-1) ;  
                    else  
                        sum += (a[j]/i) ;  
                }  
            }  
            min1 = min(min1,sum) ;  
        }  
        
        fprintf(fp2,"Case #%d: %d\n", ++step, min1) ;  
    }  
    return 0 ;  
}  