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

char c[10];

int main()
{

    int i,j,k,t,s,z,n,tp;
    string a,b,c,d;
    i=1;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d%d",&j,&k);
        tp=0;
        s = sqrt(j);
        if(s*s<j)
            s++;
        z = sqrt(k);
        for(n=s;n<=z;n++)
        {
            sprintf(&c[0],"%d",n*n);
            int len = strlen(&c[0]);
            bool btip = false;
            for(j=0;j<len/2+1;j++)
                if(c[j]!=c[len-j-1])
                {
                    btip = true;
                    break;
                }
            sprintf(&c[0],"%d",n);
            len = strlen(&c[0]);
            for(j=0;j<len/2+1;j++)
                if(c[j]!=c[len-j-1])
                {
                    btip = true;
                    break;
                }

            if(!btip){
                tp++;
            }
        }
        printf("Case #%d: %d\n",i+1,tp);
    }
    return 0;
}
