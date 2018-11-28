/*
Name: Saikat Dey
College: IIEST Shibpur
Deptt: CS(4th Sem)
*/

#include<bits/stdc++.h>
int main(){
    FILE *fp,*fp1;
    fp=fopen("A-large.in","r");
    fp1=fopen("out_large.txt","w");
    int t,j;
    fscanf(fp,"%d",&t);
    for(j=1;j<=t;j++){
        int n,i,a[10001],sum1=0,sum2=0,test,max1=0;
        fscanf(fp,"%d",&n);
        for(i=0;i<n;i++){
            fscanf(fp,"%d",&a[i]);
        }
        for(i=1;i<n;i++){
            test=a[i-1]-a[i];
            if(test>0){
                sum1+=test;
                if(test>max1){
                    max1=test;
                }
            }
        }
       // printf("%d\n",max1);
        for(i=0;i<n-1;i++){
            if(a[i]>=max1)
                sum2+=max1;
            else
                sum2+=a[i];
        }
        fprintf(fp1,"Case #%d: %d %d\n",j,sum1,sum2);

    }
    return 0;
}
