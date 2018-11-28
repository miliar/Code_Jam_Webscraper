#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>

int compare( const void* a, const void* b);
int compare_reverse( const void* a, const void* b);

// use:
//    qsort(p,D,sizeof(int),compare_reverse);

int T,N;
int m[100000];
int md[100010];

int solve(){
    int i,j,k;
    // ...
    
    int sum=0;
    
    for(i=0;i<N-1;i++){
        md[i]=m[i+1]-m[i];
        md[i]=(md[i]<0?-md[i]:0);
        sum+=md[i];
    }
    
    return sum;
    
}

int solve2(){
    int i,j,k;
    int sum=0;
    // ...
    //md already done
    int rate=0;
    
    for(i=0;i<N-1;i++){
        if(md[i]>rate){
            rate=md[i];
        }
    }
    sum=0;
    for(i=0;i<N-1;i++){
        sum+=(m[i]>rate?rate:m[i]);
    }
    return sum;
}

int main(){
    int i,res,res2,j,k;
    scanf("%d",&T);

    for(i=1;i<=T;i++){
       scanf("%d",&N);
       for(j=0;j<N;j++){
           scanf("%d",&m[j]);
       }
        // ...
        
        res = solve();
        res2 = solve2();
        
        //...
        printf("Case #%d: %d %d\n",i,res,res2);
    }
    return 0;
}

//####################################################################################################
int compare( const void* a, const void* b)
{
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );

     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return -1;
     else return 1;
}

int compare_reverse( const void* a, const void* b)
{
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );

     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return 1;
     else return -1;
}


