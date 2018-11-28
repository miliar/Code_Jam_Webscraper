#include<stdio.h>
#include<algorithm>
using namespace std;
int a[27],b[27],n;
void sortingo()
{ int f,i,j;
     for(i=1;i<=n;i++)
        {

            for(j=1;j<=n-i;j++)
            {
                if(a[j]<=a[j+1])
                {
                    f=a[j];
                    a[j]=a[j+1];
                    a[j+1]=f;
                    f=b[j];
                    b[j]=b[j+1];
                    b[j+1]=f;
                }
            }
        }
}
int main()
{

    int t,i,k,f,v;
     FILE *P,*Q;
     P=fopen("C:/Users/PRIYANKAR KING/Desktop/pinj.in","r");
Q=fopen("C:/Users/PRIYANKAR KING/Desktop/eeeeeeee.txt","w");
      fscanf(P,"%d",&t);
   // scanf("%d",&t);
    for(k=1;k<=t;k++)
    {f=0;
        fscanf(P,"%d",&n);
        for(i=1;i<=n;i++)
        {
            fscanf(P,"%d",&a[i]);
            b[i]=i;
        }
       sortingo();

       /*for(i=1;i<=n;i++)
        {
            printf("%d ",a[i]);

        }
        printf("\n");*/
 fprintf(Q,"Case #%d: ",k);
       while(a[1]!=0)
       {
           if(a[1]==a[2] && a[1]!=1 && a[2]!=1)
           {
               a[1]=a[1]-1;
               a[2]=a[2]-1;
               fprintf(Q,"%c%c ",b[1]+64,b[2]+64);
               sortingo();

           }
           else
            if(a[1]!=a[2] && a[1]!=1 && a[2]!=1)
           {
               a[1]=a[1]-2;
                fprintf(Q,"%c%c ",b[1]+64,b[1]+64);
                 sortingo();


           }
           else
            if(a[1]==1 && a[2]==1 && n%2==0)
           {
                a[1]=a[1]-1;
               a[2]=a[2]-1;
               fprintf(Q,"%c%c ",b[1]+64,b[2]+64);
               sortingo();
               n=n-2;


           }
           else
            if(a[1]==1 && a[2]==1 && n%2!=0)
           {
               a[1]=a[1]-1;
               fprintf(Q,"%c ",b[1]+64);

               sortingo();
                n=n-1;
            /* printf("\n");
       for(i=1;i<=n;i++)
        {
            printf("%d ",a[i]);

        }
        printf("\n");*/

           }
           else
            if(a[1]!=a[2] && a[1]!=1 && a[2]==1)
           {
               a[1]=a[1]-2;

               fprintf(Q,"%c%c ",b[1]+64,b[1]+64);
               if(a[1]==0)
                v=1;
               sortingo();
               if(v==1)
                n=n-1;


           }
           //if(f==5)
           //break;
          // printf("\n***1******\n");
           //f++;
       }
       fprintf(Q,"\n");

    }
    return 0;
}

