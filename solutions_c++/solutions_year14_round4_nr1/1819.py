#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAX 1010

int main()
{
    int v[MAX];
    int t;
    scanf("%d",&t);
    for(int ccnt=1; ccnt<=t; ++ccnt)
    {
        int k, n;
        int i,j;
        scanf("%d %d",&n,&k);
        for(i=0; i<n; ++i)
            scanf("%d",&v[i]);
        sort(v,v+n);
        i=0; j=n-1;
        int resp = 0;
        while(i<=j)
        {
            if(v[i]+v[j]>k)
                --j;
            else
            {
                --j; ++i;
            }
            ++resp;
        }
        printf("Case #%d: %d\n",ccnt, resp);
    }
    return 0;
}
