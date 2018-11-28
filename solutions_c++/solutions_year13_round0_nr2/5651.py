#include<stdio.h>
#include<conio.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,x,r,c,j,max,found;
    scanf("%d",&t);
    for(x=1;x<=t;x++){
                      printf("Case #%d: ",x);
                      scanf("%d %d",&r,&c);
                      int a[r][c],row[r],col[c];
                      for(i=0;i<r;i++){
                                       for(j=0;j<c;j++){
                                                        scanf("%d",&a[i][j]);
                                       }
                      }
                      for(i=0;i<r;i++){
                                       max=a[i][0];
                                       for(j=1;j<c;j++){
                                                       if(a[i][j]>max)
                                                                      max=a[i][j];
                                       }
                                       row[i]=max;
                      }
                      for(j=0;j<c;j++){
                                       max=a[0][j];
                                       for(i=1;i<r;i++){
                                                        if(a[i][j]>max)
                                                                       max=a[i][j];
                                       }
                                       col[j]=max;
                      }
                      found=0;
                      for(i=0;i<r;i++){
                                       for(j=0;j<c;j++){
                                                        if(a[i][j]<row[i] && a[i][j]<col[j]){
                                                                          found=1;
                                                                          break;
                                                        }
                                       }
                                       if(found==1)
                                                   break;
                      }
                      if(found==1)
                                  printf("NO\n");
                      else
                                  printf("YES\n");
    }
    return(0);
}
                                                            
                                                        
    
