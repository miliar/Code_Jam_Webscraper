#include<stdio.h>
 int main()
 {
     int T,row1,row2,crds[2][4][4],rslt;
     int i,j,k,m,scs[4];
     FILE *p1,*p2;
     p1=fopen("A-small-attempt3.in","r");
     p2=fopen("output1","w");
     fscanf(p1,"%d",&T);
     for(i=0;i<T;i++)
     {
         fscanf(p1,"%d",&row1);
         for(k=0;k<4;k++)
         {
             for(m=0;m<4;m++)
             fscanf(p1,"%d",&crds[0][k][m]);
         }
         fscanf(p1,"%d",&row2);
         for(k=0;k<4;k++)
         {
             for(m=0;m<4;m++)
             fscanf(p1,"%d",&crds[1][k][m]);
         }
         rslt=0;
         for(k=0;k<4;k++)
         {
             for(m=0;m<4;m++)
             {
                 if(crds[0][row1-1][k]==crds[1][row2-1][m])
                 {
                     scs[rslt++]=crds[0][row1-1][k];
                 }
             }
         }
          fprintf(p2,"Case #%d: ",i+1);
         if(rslt==0)
          fprintf(p2,"Volunteer cheated!\n");
         if(rslt>1)
          fprintf(p2,"Bad magician!\n");
         if(rslt==1)
          fprintf(p2,"%d\n",scs[0]);
     }
     fclose(p1);
     fclose(p2);
     return 0;
 }
