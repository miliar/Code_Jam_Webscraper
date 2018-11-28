#include<stdio.h>
#include<iostream.h>
#include<conio.h>
int N,M;
int a[100][100];
int check_col(int i,int j){
    int z;
    int maxc = a[i][j];
    for(z=0;z<N;z++){
                    
                     if(a[z][j]>maxc){
                                      return 0;
                                      }
                     }
                     return 1;
    
    }
int main(){
int T,i,j,w,soln=1;
scanf("%d",&T);
for(w=0;w<T;w++){
scanf("%d%d",&N,&M);
for(i=0;i<N;i++){
                 for(j=0;j<M;j++)
                 scanf("%d",&a[i][j]);
                 }
for(i=0;i<N;i++){
                 
                 int max = a[i][0];
                 for(j=0;j<M;j++){
                                  if(a[i][j]>max)
                                  max = a[i][j];
                                  }
                 for(j=0;j<M;j++){
                                  if(a[i][j]<max)
                                  soln = check_col(i,j);
                                  if(soln==0)
                                  break;
                                  
                                  }
                 if(soln==0)
                 break;
                 }
                 if(soln==1)
                 printf("Case #%d: YES\n",w+1);
                 else
                 {printf("Case #%d: NO\n",w+1);
                  soln = 1;
                  }
                 
}
getch();
return 0;
}
