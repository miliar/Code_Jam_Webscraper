#include<stdio.h>
int main(){
    int t,i;
    FILE *fp=fopen("C:/Users/prasenjit/Desktop/A-small-attempt3.in","r");
    FILE *fp1=fopen("C:/Users/prasenjit/Desktop/output1.txt","w");
    fscanf(fp,"%d",&t);
    for(i=1;i<=t;i++){
                      char s[10];
                      fscanf(fp,"%s",s);
                      int j,p=0,q=0;
                      for(j=0;s[j]!='/';j++){
                                             p=(p<<3)+(p<<1)+(s[j]-'0');
                                             }
                      for(j=j+1;s[j]!='\0';j++){
                                                q=(q<<3)+(q<<1)+(s[j]-'0');
                                                }
                      int flag=2,count;
                      while(1){
                               //printf("p: %d, q: %d\n",p,q);
                               for(j=0;q>p;j++){
                                                if(q%2!=0){
                                                           flag=1;
                                                           break;
                                                           }
                                                q/=2;
                                                }
                               if(flag==2){
                                           count=j;
                                           flag=0;
                                           }
                               else if(flag==1)
                                    break;
                               p-=q;
                               if(p==0)
                                       break;
                               }
                      if(flag==1){
                                  fprintf(fp1,"Case #%d: impossible\n",i);
                                  }
                      else{
                           fprintf(fp1,"Case #%d: %d\n",i,count);
                           }
                      }
    fclose(fp);
    fclose(fp1);
    //scanf("%d",&t);
    return 0;
    }
