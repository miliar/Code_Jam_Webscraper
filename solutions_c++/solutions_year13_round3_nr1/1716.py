#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <map>

#define MAXLENGTH 100

using namespace std;

int countc(char a[],int s,int e)
{
    int ret=0,c=0;
    for(int i=s; i<e; ++i)
    {
        if(a[i]!='a' && a[i]!='e' && a[i]!='i' && a[i]!='o' && a[i]!='u')
            c++;
        else
            c=0;
        ret = max(ret,c);
    }
    return ret;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int tc=0, t=0, n=0, la=0, ret=0,l=0,i=0;
    char a[MAXLENGTH];
    scanf("%d",&tc);
    for(t=1; t<=tc; ++t)
    {
        scanf("%s %d", a, &n);
        //printf("\n%d\n",n);
        la = strlen(a);
        ret=0;
        l=la;
        while(l>=n)
        {
            for(i=0; i+l<=la; ++i)
            {
                int x = countc(a,i,i+l);
                if(x >= n)
                {
                    //for(int j=i; j<i+l; ++j)printf("%c",a[j]);
                    //printf("\n");
                    ret++;
                }
            }
            l--;
        }
        printf("Case #%d: %d\n",t,ret);
    }
    return 0;
}

