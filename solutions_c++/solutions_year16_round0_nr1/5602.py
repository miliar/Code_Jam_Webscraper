#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

int digits,exist[10];

void eval(int N)
{
    while (N>0)
    {
        int d=N%10;
        if (!exist[d])
        {
            digits++;
            exist[d]=true;
        }
        N/=10;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_output_large.txt","w",stdout);
    int T,N;
    scanf("%d",&T);
    for (int index=1;index<=T;index++)
    {
        memset(exist,0,sizeof(exist));
        digits=0;
        scanf("%d",&N);
        printf("Case #%d: ",index);
        if (N==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int M=N;
        while (digits<10)
        {
            eval(M);
            if (digits<10) M+=N;
        }
        printf("%d\n",M);
    }
    return 0;
}
