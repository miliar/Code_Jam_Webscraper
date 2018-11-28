#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    int cas=1;
    int a[102][102];
    int m,n;
    while(cas<=t){
        scanf("%d %d",&n,&m);
        int i=0,j=0,k=0;
        for(i=0;i<n;i++)
        {
             for(j=0;j<m;j++)
               scanf("%d",&a[i][j]);
        }
        int max[102];
        for(i=0;i<n;i++){
                         max[i]=a[i][0];
               for(j=0;j<m;j++){
                         if(max[i]<a[i][j]){
                             max[i]=a[i][j];
                            }
               }          
        }
        if(m==1 || n==1){ printf("Case #%d: YES\n",cas); cas++; continue;}
       
     
        int val=1;
        for(i=0;i<n;i++){
         
               for(j=0;j<m;j++){
                       if(a[i][j]<max[i]){
                                 for(k=0;k<n;k++){
                                        if(a[k][j]>a[i][j]) { val=0; break;}          
                                 }                     
                       }
                       if(!val) break;
               }          
              if(!val) break;
        }
     
         int max2[102];
       if(val){
            for(j=0;j<m;j++){
                             max2[j]=a[0][j];
                   for(i=0;i<n;i++){
                             if(max2[j]<a[i][j]){
                                  max2[j]=a[i][j];
                                }
                   }          
            }
           
       
            for(j=0;j<m;j++){
             
                   for(i=0;i<n;i++){
                           if(a[i][j]<max2[j]){
                                     for(k=0;k<m;k++){
                                            if(a[i][k]>a[i][j]) { val=0; break;}          
                                     }                     
                           }
                           if(!val) break;
                   }          
                  if(!val) break;
            }
       }        
        if(!val) printf("Case #%d: NO\n",cas);
        else printf("Case #%d: YES\n",cas);
        cas++;
    }
}
