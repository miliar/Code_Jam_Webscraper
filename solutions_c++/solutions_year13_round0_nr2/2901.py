#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

FILE *in = fopen("B-large.in","r");
FILE *out = fopen("B-large.out","w");

main()
{
       int r,c,p,n,max;
       int T[101][101];
       fscanf(in,"%d",&n);
       for(int i=0;i<n;i++){
               p=1;
               fscanf(in,"%d %d",&r,&c);
               for(int j=0;j<r;j++)
                       for(int k=0;k<c;k++)
                               fscanf(in,"%d",&T[j][k]);
               for(int j=0;j<r;j++) {
                       max=0;
                       for(int k=0;k<c;k++)
                               max>?=T[j][k];
                       for(int k=0;k<c;k++)
                               if(T[j][k]<max) {
                                        //printf("%d %d %d %d\n",j,k,T[j][k],max);
                                        for(int l=0;l<r;l++)
                                                if(T[l][k]>T[j][k])
                                                         p=0;
                               }
               }
               //printf("%d\n",p);
               fprintf(out,"Case #%d: %s\n",i+1,p?"YES":"NO");
       }
       fclose(in);
       fclose(out);
       system("PAUSE");
}
