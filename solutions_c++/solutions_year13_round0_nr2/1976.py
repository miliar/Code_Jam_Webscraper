#include <cstdio>
#define MAX 105

int n, m;
int ary[MAX][MAX];
bool vis[MAX][MAX];

void done(int idx, int type, int k)
{
    bool flag = 1;
    if(!type)
    {
        for(int j=0; j<m; j++)
            if(ary[idx][j] > k)
                flag = 0;

        if(!flag)
            return ;

        for(int j=0; j<m; j++)
            vis[idx][j] = 1;
    }
    else
    {
        for(int i=0; i<n; i++)
            if(ary[i][idx] > k)
                flag = 0;
        if(!flag)
            return ;
        for(int i=0; i<n; i++)
            vis[i][idx] = 1;
    }
}


int main()
{
    int T;

    scanf("%d", &T);

    for(int Ti=1; Ti<=T; Ti++)
    {
        scanf("%d %d", &n, &m);

        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                scanf("%d", &ary[i][j]);

        bool ans = 1;
        for(int k=100; k>0; k--)
        {
            for(int i=0; i<n; i++)
                for(int j=0; j<m; j++)
                    vis[i][j] = 0;

            for(int i=0; i<n; i++)
                done(i, 0, k);

            for(int j=0; j<m; j++)
                done(j, 1, k);

            for(int i=0; i<n; i++)
                for(int j=0; j<m; j++)
                    if(vis[i][j] == 0 && ary[i][j] == k)
                        ans = 0;
            /*
            for(int i=0; i<n; i++)
            {
                for(int j=0; j<m; j++)
                    printf("%d ", vis[i][j]);
                printf("\n");
            }

            printf("%d %d\n", k, ans);
            */
        }
        printf("Case #%d: %s\n", Ti, ans ? "YES" : "NO");
    }
}
