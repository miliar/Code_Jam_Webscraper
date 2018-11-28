#include<stdio.h>
#include<conio.h>
#include<iostream.h>
void merge(int a[],int p,int q,int r)
{
          int n1,n2,i,j,n;
          n1=q-p+1;
          n2=r-q;       
          int left[n1],right[n2];
          
          for(i=0;i<n1;i++){
                            left[i]=a[p+i];
          }
          
          for(j=0;j<n2;j++){
                            right[j]=a[q+j+1];
          }
          i=0;j=0;n=p;
          while(i<n1 && j<n2){
                     if(left[i]<right[j])
                                          a[n++]=left[i++];
                     else
                                          a[n++]=right[j++];
          }
          if(i==n1){
                    while(j<n2)
                                a[n++]=right[j++];
          }
          else{
                    while(i<n1)
                               a[n++]=left[i++];
          }
                                
}
void merge_sort(int a[],int p,int r)
{
               int q;
               if(p<r){
                      q=(p+r)/2;
                      merge_sort(a,p,q);
                      merge_sort(a,q+1,r);
                      merge(a,p,q,r);               
               }
}
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    unsigned long t,n,caseno=1,i,op,g=9999,l=0,flag=0;
    unsigned long a;
    scanf("%lu",&t);
    while(t--)
    {
              l=0;g=999,flag=0;
        scanf("%lu %lu",&a,&n);
        int size[n];
        for(i=0;i<n;i++){
                         scanf("%lu",&(size[i]));
        }
        if(a==1){
                printf("Case #%lu: %lu\n",caseno,n);
                caseno++;
        }
        else{
                merge_sort(size,0,n-1);
                
                for(i=0;i<n;i++){
                                if(a>size[i]){
                                              a=a+size[i];
                                }
                                else{
                                     if(g>l+(n-i))
                                                g=l+(n-i);
                                     while(a<=size[i]){
                                                       a=a+(a-1);
                                                       l++;
                                     }
                                     a=a+size[i];
                                     if(l>g){
                                             flag=1;
                                             break;
                                     }
                                }
                }
                if(flag==1){
                    printf("Case #%lu: %lu\n",caseno,g);
                    caseno++;
                }
                else{
                     printf("Case #%lu: %lu\n",caseno,l);
                    caseno++;
                }
        
        }
    }
    
    return(0);
}
