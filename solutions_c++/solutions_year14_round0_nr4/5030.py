#include<cstdio>
#include<conio.h>
#include<algorithm>

using namespace std;

int main()
{
    int t,n,i,k,j;
    float a[11],b[11],c[11],d[11];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
                     int x=0,y=0,z=0;
                     scanf("%d",&n);
                     for(k=0;k<n;k++)
                     {
                                     scanf("%f",&a[k]);
                     }
                     
                     for(k=0;k<n;k++)
                     {
                                     scanf("%f",&b[k]);
                     }
                     
                     for(k=0;k<n;k++)
                     {
                                     c[k]=a[k];
                     }
                     
                     for(k=0;k<n;k++)
                     {
                                     d[k]=b[k];
                     }
                     
                      sort(a,a+n);
                      sort(b,b+n);
                     
                     for(k=0;k<n;k++)
                     {
                                     for(j=0;j<n;j++)
                                     {
                                                     
                                                 if(a[k]>b[j]&& b[j]!=-1)
                                                 {
                                                              a[k]=-1;
                                                              b[j]=-1;
                                                              x++;
                                                              break;
                                                 }
                                     }
                     }
                     
                     sort(c,c+n);
                     sort(d,d+n);
                     
                     for(k=0;k<n;k++)
                     {
                                     for(j=0;j<n;j++)
                                     {
                                                     
                                                 if(d[k]>c[j] && c[j]!=-1)
                                                 {
                                                              c[j]=-1;
                                                              d[k]=-1;
                                                              y++;
                                                              break;
                                                 }
                                     }
                     }
                     
                     z = n-y;
                     
                     printf("Case #%d: %d %d\n",i,x,z);
    }
    
    getch();
    return 0;
}
    
    
