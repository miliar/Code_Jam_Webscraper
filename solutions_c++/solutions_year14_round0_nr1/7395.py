#include<stdio.h>
using namespace std;
int  main()
{
FILE* file = fopen ("A-small-attempt0.in", "r");
int t=0;
int l=16;
fscanf (file, "%d", &t);
int a[l],b[l];
int c1,c2,n,no;

for(int x=0;x<t;x++)
    {
        fscanf (file, "%d", &c1);
        for(int i=0;i<l;i++)
                fscanf (file, "%d", &a[i]);
        fscanf (file, "%d", &c2);
        for(int i=0;i<l;i++)
                fscanf (file, "%d", &b[i]);
         n=0;
         int a1=(4*c1);
         int a2=4*c2;
         for(int i=4*(c1-1);i<a1;i++)
               for(int j=4*(c2-1);j<a2;j++)
               {
               if(a[i]==b[j])
               {
                   n++;
                   no=a[i];
               }

               }

         if(n==1) printf("Case #%d: %d\n",x+1,no);
         else if(n==0) printf("Case #%d: Volunteer cheated!\n",x+1);
         else printf("Case #%d: Bad magician!\n",x+1);
         n=0;

    }


return 0;
}


