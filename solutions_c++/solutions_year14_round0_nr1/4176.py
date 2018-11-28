#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
FILE *fout;
ifstream fin("t.in");
int caract[20];
int main()
{
    int l,x,sol=0,nr=0;
    fout=fopen("output.txt","w");
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
    {
        nr=0;
        for(int j=1;j<=17;j++)caract[j]=0;
        fin>>l;
        for(int j=1;j<=4;j++)
            for(int k=1;k<=4;k++)
            {
                fin>>x;
                if (j==l) caract[x]=1;
            }
        fin>>l;
        for(int j=1;j<=4;j++)
            for(int k=1;k<=4;k++)
            {
                fin>>x;
                if(j==l)
                {
                    if(caract[x]==1)
                    {
                        nr++;
                        sol=x;
                    }
                }

            }
         fprintf(fout,"Case #%d: ",i);
         if(nr==0) fprintf(fout,"Volunteer cheated!\n");
         else if (nr>1)  fprintf(fout,"Bad magician!\n");
            else fprintf(fout,"%d\n",sol);

    }
}
