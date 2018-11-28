#include<stdio.h>
#include<stdlib.h>
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main()
{
    float k,l,p,t,c,na[1003],ke[1003];
    int i,j,n,m,q;
    scanf("%f",&t);
    for(p=0;p<t;p++)
    {
                    m=0;
                    scanf("%d",&n);
                    for(i=0;i<n;i++)
                    scanf("%f",&na[i]);
                    for(i=0;i<n;i++)
                    scanf("%f",&ke[i]);
                    qsort (na,n, sizeof(float), compare);
                    qsort (ke,n, sizeof(float), compare);
                    for(i=0;i<n;i++)
                    printf("%.3f ",na[i]);
                    printf("\n");
                    for(i=0;i<n;i++)
                    printf("%.3f ",ke[i]);
                    printf("\n");
                    i=0;
                    j=0;
                    while(i<n&&j<n)
                    {
                                   if(na[i]>ke[j])
                                   {
                                      i++;
                                      j++;
                                      m++;
                                   }
                                   else
                                   i++;
                    }
                    printf("%d\n",m);
    }                              
    system("pause");
    return(0);
}
 
