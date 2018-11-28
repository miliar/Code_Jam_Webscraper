#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int lawn[101][101];
char vst[101][101];

int N, M;

int judge(int x, int y, int high)
{
    int i;
    int status = 0;
    for(i=1;i<=N;++i)
    {
        if(lawn[i][y]<=high) ++status;
        //if(lawn[i][y]==high) vst[i][y]=1;
    }
    if(status == N) return 1;

    status = 0;
    for(i=1;i<=M;++i)
    {
        if(lawn[x][i]<=high) ++status;
        //if(lawn[x][i]==high) vst[x][i]=1;
    }
    if(status == M) return 1;

    return 0;
}

int main()
{
    int T,i,j,k;
    int ans=0;
    scanf("%d", &T);

    for(i=1;i<=T;++i)
    {
        ans = 1;
        scanf("%d%d", &N, &M);
        memset(lawn, 0, sizeof(lawn));
        memset(vst, 0, sizeof(vst));
        for(j=1;j<=N;++j)
        {
            for(k=1;k<=M;++k)
            {
                scanf("%d", &lawn[j][k]);
            }
        }
        for(j=1;j<=N;++j)
        {
            for(k=1;k<=M;++k)
            {
                if(vst[j][k]==0)
                    ans = judge(j, k, lawn[j][k]);
                if(ans==0)
                    break;
            }
            if(ans==0) break;
        }
        printf("Case #%d: %s\n", i, ans==1?"YES":"NO");
    }
    
    return 0;
}
