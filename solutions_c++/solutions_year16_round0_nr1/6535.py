#include <stdio.h>

#define PRINTF //printf

int T;
int N;

long process()
{
     int i;
     int hsh[10];
     int cnt=0;
     long k,prd;
     // initialize hsh
     for(i=0;i<10;i++)
        hsh[i]=0;
     if( N==0)
         return -1;
     i=1;
     k=N;
     while( cnt < 10 )
     {
        
        k = N*i;
        prd=k;
        PRINTF("\nPROCESSING ... %d, cnt = %d",k,cnt);        
        while(k != 0)
        {
           int x;
           x = k%10;
           if( hsh[x] == 1 )
           {
               // no effect , ignore
           }
           else
           {
               hsh[x] = 1;
               cnt++;
           }
           k=k/10;
        }
        
        i++;
     }
     PRINTF("\nReturning : %d",prd);
     return prd;
}

int main(){
    int i;
    long ret; 
    scanf("%d",&T);
    PRINTF("\nT=%d",T);
    
    for( i=0 ; i<T; i++ )
    {
         scanf("%d",&N);
         PRINTF("\nN=%d",N);
         ret = process();
         if( ret == -1 )
             printf("Case #%d: INSOMNIA\n",i+1);
         else
             printf("Case #%d: %ld\n",i+1,ret);
    }
    return 0;
}
