#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LEN 17
int main(){
    FILE *fp1,*fp2;
    fp1 = fopen("A--small-attempt0.in","r"); 
    fp2 = fopen("A--dataout.out","w"); 
    int m;
    int ans[2];
    int map[4][4];
    int map2[4][4];
    int cnt1[LEN];
    int cnt2[LEN];
    fscanf(fp1,"%d",&m);
    
    
    
    for( int k = 0 ; k < m ; k++ ){
        int cnt_res = 0;
        int res = 0;
        fscanf(fp1,"%d",&ans[0]);  
        for( int j = 0 ; j < 4 ; j++ ){
               for( int l = 0 ; l < 4 ; l++ ){
                   fscanf(fp1,"%d",&map[j][l]);  
                   cnt1[map[j][l]] = j;
                   //fprintf(fp2,"%d  ",map[j][l]);
               }     
              //fscanf(fp1,"%\n"); 
              //fprintf(fp2,"\n");
         }    
         //fprintf(fp2,"\n");
        fscanf(fp1,"%d",&ans[1]);  
        for( int j = 0 ; j < 4 ; j++ ){
            for( int l = 0 ; l < 4 ; l++ ){
                   fscanf(fp1,"%d",&map2[j][l]);  
                   cnt2[map2[j][l]] = j;
            }     
               //fscanf(fp1,"%\n"); 
              // fprintf(fp2,"\n");
        }//for j    
         /*
        for( int i = 1 ; i < 17 ; i++){
             if(cnt1[i] == cnt2[i]){
                 res = i;
                 cnt_res++;
             }
        }*/
        for( int i = 0 ; i < 4 ; i++ ){
           
                if( ans[1]-1  == cnt2[map[ans[0]-1][i]]){
                    res = map[ans[0]-1][i];
                    cnt_res++;
                }
              
        }
        
        
        if( cnt_res == 1 ){
            fprintf(fp2,"Case #%d: %d\n",k+1,res);
        } else if( cnt_res > 1){
            fprintf(fp2,"Case #%d: Bad magician!\n",k+1);
        } else if( cnt_res == 0 ){
            fprintf(fp2,"Case #%d: Volunteer cheated!\n",k+1);
        }
           
    }
    
   
    fclose(fp1);
    fclose(fp2);
    return 0;
    
}
