#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <queue>
#include <list>
#include <algorithm>
#include <iostream>
typedef long long ll;
using namespace std;
char str[100];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outl.txt","w",stdout);
    int t,n,i,need,nn,c,C=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %s",&n,str);
        c=need=0;
        for(i=0;str[i];i++)
        {
            int a=str[i]-'0';
            if(a>0)
            {
                if(c>=i)
                    c+=a;
                else
                {
                    nn=i-c;
                    if(c+nn<n)
                    {
                        need+=nn;
                        c+=nn;
                        c+=a;
                    }
                    else
                    {
                        nn=n-c;
                        need+=nn;
                        c+=nn;
                    }
                }
            }
            if(c>=n) break;
        }

        if(c<n)
        {
            need+=(n-c);
        }
        printf("Case #%d: %d\n",C++,need);
    }

    return 0;
}
