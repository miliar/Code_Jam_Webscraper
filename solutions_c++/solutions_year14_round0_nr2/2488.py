#include<stdio.h>
int main(){
    int t,i=0;
    FILE *fp=fopen("C:/Users/prasenjit/Desktop/B-large.in","r");
    FILE *fp1=fopen("C:/Users/prasenjit/Desktop/aaa.txt","w");
    fscanf(fp,"%d",&t);
    while(i<t){
               double c,f,x,time=0,ck=2;
               fscanf(fp,"%lf",&c);
               fscanf(fp,"%lf",&f);
               fscanf(fp,"%lf",&x);
               while(1){
                        if(time+c/ck+x/(ck+f)<time+x/ck){
                                                         time+=c/ck;
                                                         ck+=f;
                                                         }
                        else{
                             time+=x/ck;
                             break;
                             }
                        }
               fprintf(fp1,"Case #%d: %.7lf\n",i+1,time);
               i++;
               }
    fclose(fp);
    fclose(fp1);
    return 0;
    }
