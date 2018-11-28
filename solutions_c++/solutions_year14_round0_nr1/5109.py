#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j,k,l,m,n,p,q,t,ar[17],c;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
                    for(p=0;p<17;p++)
                    ar[p]=0;
                    c=0;
                    scanf("%d",&n);
                    for(p=0;p<4;p++)
                    {
                                    for(j=0;j<4;j++)
                                    {
                                                    scanf("%d",&l);
                                                    if(p==(n-1))
                                                    ar[l]++;
                                    }
                    }
                    scanf("%d",&k);
                    for(p=0;p<4;p++)
                    {
                                    for(j=0;j<4;j++)
                                    {
                                                    scanf("%d",&m);
                                                    if(p==(k-1))
                                                    ar[m]++;
                                    }
                    }
                    k=0;
                    for(p=0;p<17;p++)
                    {
                                     if(ar[p]>1)
                                     {
                                                k=p;
                                                c++;
                                     }
                    }
                    if(c>1)
                    printf("Case #%d: Volunteer cheated!\n",i+1);
                    else if(c<1)
                    printf("Case #%d: Bad magician!\n",i+1);
                    else
                    printf("Case #%d: %d\n",i+1,k);
    }
    system("pause");
    return(0);
}                
