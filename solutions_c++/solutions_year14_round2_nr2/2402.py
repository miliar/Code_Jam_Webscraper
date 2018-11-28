#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<fstream>
#include<vector>
#include<stack>
#include<map>

using namespace std;


int main()
{
    int t;
    FILE *inp,*ops;
    inp=fopen("inp.txt","r");
    ops=fopen("op.txt","w");

    fscanf(inp,"%d",&t);

    for(int l=0;l<t;l++)
    {
      int a,b,k;
      fscanf(inp,"%d%d%d",&a,&b,&k);

      int count=0;
      for(int i=0;i<a;i++)
      {
             for(int j=0;j<b;j++)
             {
                 int x=(i&j);

                 if(x<k)
                    count++;
             }
      }
      fprintf(ops,"Case #%d: %d\n",l+1,count);

    }
    fclose(inp);
    fclose(ops);
    return 0;
}
