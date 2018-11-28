#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <list>
#include <map>
using namespace std;

int ir[100][100];
int line[100];
int row[100];

int main()
{

    int i,j,k,t,s,z,n,tp;
    string a,b,c,d;
    i=1;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d%d",&j,&k);
        memset(line,0,100*sizeof(int));
        memset(row,0,100*sizeof(int));
        for(t=0;t<j;t++)
            for(s=0;s<k;s++)
            {
                scanf("%d",&ir[t][s]);
                if(ir[t][s]>line[t])
                    line[t] = ir[t][s];
            }
        for(s=0;s<k;s++)
            for(t=0;t<j;t++)
                if(ir[t][s]>row[s])
                    row[s] = ir[t][s];
        bool btip = false;
        for(t=0;t<j;t++)
        {
            for(s=0;s<k;s++)
            {
                if(line[t]>=row[s])
                {
                    if(ir[t][s]!=row[s])
                    {
                        btip = true;
                        break;
                    }
                } else
                {
                    if(ir[t][s]!=line[t])
                    {
                        btip = true;
                        break;
                    }
                }

            }
            if(btip)
                break;
        }
        if(btip)
            printf("Case #%d: NO\n",i+1);
        else
            printf("Case #%d: YES\n",i+1);
    }
    return 0;
}
