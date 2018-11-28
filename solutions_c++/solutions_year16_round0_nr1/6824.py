#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
bool num[10];
int main()
{
    /*FILE *in,*out;
    in = fopen("in","r");
    out = fopen("out","w");*/
    int t,n,q;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int ant=10,cnt=1;
        memset(num,false,sizeof(num));
        scanf("%d",&n);
        while(ant>0&&n!=0)
        {
            q=cnt*n;
            while(q)
            {
                if(!num[q%10])
                {
                    num[q%10]=true;
                    ant--;
                }
                q=q/10;
            }
            cnt++;
        }
        if(n)
            printf("Case #%d: %d\n",i,(cnt-1)*n);
        else printf("Case #%d: INSOMNIA\n",i);
    }
    return 0;
}
