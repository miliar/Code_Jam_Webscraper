#include <cstdio>
#include <iostream>
#include <cstring>
#include <climits>
#include <algorithm>
using namespace std;

char s[16];
int v[10];
int n,l;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,i,j;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d",&n);
        printf("Case #%d: ",c+1);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        memset(v,0,sizeof(v));
        for(i=n;i<INT_MAX;i=i+n)
        {
            l=sprintf(s,"%d",i);
            for(j=0;j<l;j++)
            {
                v[s[j]-'0']=1;
            }
            if(find(v,v+10,0)==v+10)
            {
                break;
            }
        }
        printf("%d\n",i);
    }
    return 0;
}
