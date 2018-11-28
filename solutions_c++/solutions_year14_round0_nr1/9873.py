#include<iostream>
#include <stdio.h>
using namespace std;
int main()
{


    int T,t;
    FILE *fp1 , *fp2;
    fp1 = fopen("A-small-attempt3.in", "r");
   fp2 = fopen("output.in", "w");
    fscanf(fp1 ,"%d",&T);
    t=T;
    while(!feof(fp1)&&t)
    {
        int n,m,g,h;
        int a[4][4];
        int b[4][4];
       fscanf(fp1 ,"%d",&n);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                fscanf(fp1,"%d",&a[i][j]);

            fscanf(fp1 ,"%d",&m);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
          fscanf(fp1,"%d",&b[i][j]);
            int count =0;
            for(int i=0;i<4;i++)
               {

                for(int j=0;j<4;j++)
                {
                if(a[n-1][i] == b[m-1][j])
                {count++;
                    if(count ==1)
                    g=i;
                }
                }
    }
    t--;
            if(count == 1)
                 fprintf(fp2,"Case #%d: %d \n",T-t,a[n-1][g]);
            else if(count == 0)
               fprintf(fp2,"Case #%d: Volunteer cheated! \n",T-t);
            else
                fprintf(fp2,"Case #%d: Bad magician! \n",T-t);

    }
    fclose(fp1);
   fclose(fp2);
     return 0;
}
