#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define LEN 17
#define MAX 10000
int cmp(const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}
int main(){
    FILE *fp1,*fp2;
    fp1 = fopen("D--large.in","r"); 
    fp2 = fopen("D--large.out","w"); 
    int n;
    double tmp;
    fscanf(fp1,"%d",&n);
    for( int ii = 0 ; ii < n ; ii++ ){
         int m;
         int naomi[2000] = {0};
         int  ken[2000] = {0};
         int v1[2000] = {0};
         int v2[2000] = {0};
         int sco1 = 0;
         int scok = 0;
        fscanf(fp1,"%d",&m);
        for( int  i = 0 ; i < m ; i++ ){
            fscanf(fp1,"%lf",&tmp);
            naomi[i] = (int)floor(tmp * MAX);
        }
        for( int  i = 0 ; i < m ; i++ ){
            fscanf(fp1,"%lf",&tmp);
            ken[i] = (int)floor(tmp * MAX);
        }
        qsort(naomi, m, sizeof(int),cmp);
        qsort(ken, m, sizeof(int),cmp);
        /*
        for( int  i = 0 ; i < m ; i++ ){
            fprintf(fp2,"%d ",naomi[i]);
        }fprintf(fp2,"\n");
        */
        for( int i = 0 ; i < m ; i ++ ){
            for( int j = 0 ; j < m ; j++ ){
                if( v2[j] == 0 && naomi[i] < ken[j] ){
                    scok++;
                    v2[j] = 1;
                    break;
                }
            }     
        }
       // fprintf(fp2,"\n%d\n",m-scok);
       int pos = 0;
       int ck = 0;
       int lastk = m-1;
       int vk[2000]= {0};
       for( int i = 0 ; i < m ; i++ ){
           for( int j = 0 ; j < m ; j++ )
           {
               if( naomi[i] < ken[j]&& vk[j] == 0 ){
                   ck++;
                   vk[lastk--] = 1;
                   break;
               }else if( naomi[i] > ken[j] && vk[j] == 0 ){
                   vk[j] = 1;
                   break;
               } 
           }
       }
       fprintf(fp2,"Case #%d: %d %d\n",ii+1,m-ck,m-scok);
    }
    
    fclose(fp1);
    fclose(fp2);
    return 0;
    
}
