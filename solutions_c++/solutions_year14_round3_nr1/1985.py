#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LEN 17

int gcd(int a,int b)
{
    int r;
    while(b!=0){
       r=a%b;
       a=b;
       b=r;
    }
    return a;
}

int main(){
    FILE *fp1,*fp2;
    fp1 = fopen("A--small-attempt1.in","r"); 
    fp2 = fopen("A--dataout2.out","w"); 
    int m;
    fscanf(fp1,"%d",&m);
    for( int i = 1 ; i <= m ; i++ ){
        int  p,q;
        fscanf(fp1,"%d/%d",&p,&q);
        //fprintf(fp2,"%d %d\n",p,q);
        int gcdpq = gcd(p,q);
        //fprintf(fp2,"%d %d %d\n",p,q,gcdpq);
        p /= gcdpq;
        q /= gcdpq;
        if( q % 2 != 0 ){
            fprintf(fp2,"Case #%d: impossible\n",i);
            continue;
        }
        int gen = 1;
        int flag = 1;
        int qq = q;
        while(q > 1){
           if( q % 2 != 0 ){
                flag = 0;
                break;
            }
            q /= 2;        
        }
        q = qq;
        while( p * 2 < q ){
            gen ++;
            q /= 2;
        }
        if( flag == 1 ){
            fprintf(fp2,"Case #%d: %d\n",i,gen);
        }else if( flag == 0 ){
            fprintf(fp2,"Case #%d: impossible\n",i);
        }
        
    } 
   
   
    fclose(fp1);
    fclose(fp2);
    return 0;
    
}
