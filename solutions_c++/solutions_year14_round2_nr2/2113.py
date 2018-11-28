#include <cstdio>

using namespace std;
int tstCASE;

void CNT(int A,int B,int C)
{
    int cnt = 0;
    for(int i = 0; i < A; ++i)
        for(int j = 0; j < B; ++j)
            if( (i&j) < C )
                    ++ cnt;
    printf("Case #%d: %d\n",++tstCASE,cnt);
}

int main()
{
    freopen("formula.in","r",stdin);
    ///freopen("formula.out","w",stdout);
    freopen("formula.txt","w",stdout);
    int T;
    scanf("%d",&T);
    while(T--)
    {
        int a,b,c;
        scanf("%d%d%d",&a,&b,&c);
        CNT(a,b,c);
    }

    return 0;
}
