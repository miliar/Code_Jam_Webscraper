#include<algorithm>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#include<sstream>
#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>

using namespace std;

int main()
{
    freopen("B-small-attempt0 (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt,a,b,k,i,j,result;
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
        scanf("%d%d%d",&a,&b,&k);
        result=0;
        for(i=0;i<a;i++)
            for(j=0;j<b;j++)
            {
                if((i&j)<k)result++;
            }
        printf("Case #%d: %d\n",tt,result);
    }

	return 0;
}
