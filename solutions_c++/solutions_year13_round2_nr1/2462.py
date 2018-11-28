#include<conio.h>
#include<stdio.h>

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
               //cout<<"p="<<p<<" r="<<r<<"\n";
               if(p<r){
                      q=(p+r)/2;
                      merge_sort(a,p,q);
                      merge_sort(a,q+1,r);
                      merge(a,p,q,r);               
               }
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,mysize,nsnake,gn,ln,i,j,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++){
               gn=11;ln=0;
               scanf("%d %d",&mysize,&nsnake);
               int nsize[nsnake];
               for(i=0;i<nsnake;i++){
                                     scanf("%d",&nsize[i]);
               }
               merge_sort(nsize,0,nsnake-1);
               
                            for(i=0;i<nsnake;i++){
                                                   if(mysize>nsize[i])
                                                                       mysize+=nsize[i];
                                                   else{
                                                        j=nsnake-i;
                                                        if(gn>ln+j){
                                                                    gn=ln+j;
                                                        }
                                                        if(mysize>1){
                                                        while(mysize<=nsize[i]){
                                                                                mysize+=mysize-1;
                                                                                ln++;
                                                        }
                                                        mysize+=nsize[i];}
                                                        else{
                                                            ln=j;
                                                            break;
                                                            }
                                                   }
                                                   if(ln>gn)
                                                            break;
                            }
               
               if(gn<ln)
                        printf("Case #%d: %d\n",k,gn);
               else
                        printf("Case #%d: %d\n",k,ln);
    }
} 
                                                                                               
                                                                               
                                          
                                          
                                          
                                          
