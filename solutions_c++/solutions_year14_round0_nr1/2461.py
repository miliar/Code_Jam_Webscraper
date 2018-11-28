#include<stdio.h>
int main(){
    int t,i=0;
    FILE *fp1=fopen("C:/Users/prasenjit/Desktop/A-small-attempt2.in","r");
    FILE *fp=fopen("C:/Users/prasenjit/Desktop/aaa.txt","w");
    fscanf(fp1,"%d",&t);
    while(i<t){
               int fq,sq,a1[4],j,k,count=0,ans,temp;
               fscanf(fp1,"%d",&fq);
               for(k=0;k<4;k++){
                                for(j=0;j<4;j++){
                                                 if(k!=fq-1){
                                                             fscanf(fp1,"%d",&temp);
                                                             }
                                                 else
                                                     fscanf(fp1,"%d",&a1[j]);
                                                 }
                                }
               fscanf(fp1,"%d",&sq);
               for(k=0;k<4;k++){
                                for(j=0;j<4;j++){
                                                 fscanf(fp1,"%d",&temp);
                                                 if(k==sq-1){
                                                             if(temp==a1[0] || temp==a1[1] || temp==a1[2] || temp==a1[3]){
                                                                                      ans=temp;
                                                                                      count++;
                                                                                      }
                                                      }
                                                 }
                                }
               if(count==1)
                           fprintf(fp,"Case #%d: %d\n",i+1,ans);
               else if(count>1)
                    fprintf(fp,"Case #%d: Bad magician!\n",i+1);
               else
                   fprintf(fp,"Case #%d: Volunteer cheated!\n",i+1);
               i++;
               }
    fclose(fp1);
    fclose(fp);
    return 0;
    }
