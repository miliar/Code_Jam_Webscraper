#include<stdio.h>
int a[1001] ;  
int main() {  	freopen("B-large.in","r",stdin);
	freopen("code.out","w",stdout);
    int  s= 0,t ;  
    int j,i,min,max,sum,n ;  
    scanf("%d",&t) ;  
    while( t--){  
        scanf("%d",&n) ;  
        for(i=0;i<n;i++) {  
           scanf("%d",&a[i]) ;  
          if(a[i]>max)
          max=a[i];
        }  
        min=max;  
        for(i=1;i<= max;i++){  
            sum=i;  
            for(j=0;j<n;j++){  
                if(a[j]>i){  
                    if(a[j]%i==0)  
                        sum+=(a[j]/i-1);  
                    else  
                        sum+=(a[j]/i);  
                }  
            }  
            if(sum<min)
            min=sum;
        }  
        printf("Case #%d: %d\n", ++s, min) ;  
    }  
    return 0 ;  
}  

