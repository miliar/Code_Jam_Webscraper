#include<stdio.h>
#include<conio.h>
int main(){
    int array[4][4],final,t,ans_1,ans_2,second[4][4],sum=0,j,k,l,m,n,p,i;
    scanf("%d",&t);
    for(i=0;i<t;i++){
                     scanf("%d",&ans_1);
                     ans_1--;
                     for(j=0;j<4;j++){
                                      for(k=0;k<4;k++){
                                                       scanf("%d",&array[j][k]);
                                                       }
                                                       }
                     scanf("%d",&ans_2);
                     ans_2--;
                     for(l=0;l<4;l++){
                                      for(m=0;m<4;m++){
                                                       scanf("%d",&second[l][m]);
                                                       }
                                                       }
                      for(n=0;n<4;n++){
                                       for(p=0;p<4;p++){
                                                        if(array[ans_1][n]==second[ans_2][p]){
                                                                                              sum++;
                                                                                              final=array[ans_1][n];
                                                                                              }   
                                                                                              
                                                                                              }
                                                                                              }   
                                                                                              
                             if(sum==0){
                                        printf("Case #%d: Volunteer cheated!\n",i+1);
                                        }
                             else if(sum==1){
                                        printf("Case #%d: %d\n",i+1,final);
                                        }
                              else{
                                   printf("Case #%d: Bad magician!\n",i+1);
                                   }
                                   sum=0;
                                   }
                                   getch();
                                   }                       
