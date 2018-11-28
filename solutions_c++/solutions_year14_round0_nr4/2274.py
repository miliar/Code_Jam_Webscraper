#include<stdio.h>
int split(double *a,int lb,int ub){
    int p,q,pivot;
    pivot=lb;
    p=lb+1;
    q=ub;
    while(p<=q){
               for(;a[p]<a[pivot];p++);
               for(;a[q]>a[pivot];q--);
               if(p<q)
                      a[p]=a[p]+a[q]-(a[q]=a[p]);
               }
    a[pivot]=a[pivot]+a[q]-(a[q]=a[pivot]);
    return q;
    }
void quicksort(double *a,int lb,int ub){
     int i;
     if(lb<ub){
               i=split(a,lb,ub);
               quicksort(a,lb,i-1);
               quicksort(a,i+1,ub);    
               }
     }
int main(){
    int t,i=0;
    FILE *fp=fopen("C:/Users/prasenjit/Desktop/D-large.in","r");
    FILE *fp1=fopen("C:/Users/prasenjit/Desktop/aaa.txt","w");
    fscanf(fp,"%d",&t);
    while(i<t){
               int n,j,dw=0,w=0;
               fscanf(fp,"%d",&n);
               double a[n],b[n];
               for(j=0;j<n;j++)
                               fscanf(fp,"%lf",&a[j]);
               for(j=0;j<n;j++)
                               fscanf(fp,"%lf",&b[j]);
               quicksort(a,0,n-1);
               quicksort(b,0,n-1);
               int lb=0,ub=n-1;
               for(j=0;j<n;j++){
                                if(a[j]>b[lb]){
                                               dw++;
                                               lb++;
                                               }
                                else{
                                     ub--;
                                     }
                                }
               lb=0,ub=n-1;
               for(j=0;lb<n;j++){
                                 for(;b[lb]<a[j] && lb<n;lb++,w++);
                                 lb++;
                                 }
               fprintf(fp1,"Case #%d: %d %d\n",i+1,dw,w);
               i++;
               }
    fclose(fp);
    fclose(fp1);
    return 0;
    }
