#include<cstdio>
#include<cstring>
using namespace std;
#define MAXN 120

int T;
int N, M;
int data[MAXN][MAXN];
int rows[MAXN];
int columns[MAXN];

int bigger(int A, int B)
{
    if(A > B)return A;
    return B;
}

int smaller(int A, int B)
{
    if(A > B)return B;
    return A;
}


bool Try()
{
    for(int i = 1;i <= N;i++)
        for(int j = 1;j <= M;j++)
        {
            if( smaller( rows[i], columns[j] ) != data[i][j] )return 0;
        }

    return 1;
}

void solve(int test)
{
    memset(rows, 0, sizeof(rows));
    memset(columns, 0, sizeof(columns));

    scanf("%d%d", &N, &M);
    for(int i = 1;i <= N;i++)
     for(int j = 1;j <= M;j++)scanf("%d", &data[i][j]);


    for(int i = 1;i <= N;i++)
    {
        for(int j = 1;j <= M;j++)rows[i] = bigger( rows[i], data[i][j] );
        //printf("ROW %d -> %d\n", i, rows[i]);
    }

    for(int i = 1;i <= M;i++)
    {
        for(int j = 1;j <= N;j++)columns[i] = bigger( columns[i], data[j][i] );
        //printf("COL %d -> %d\n", i, columns[i]);
    }

    ( Try() )? printf("Case #%d: YES\n", test) : printf("Case #%d: NO\n", test);

}

int main()
{
    scanf("%d", &T);
    for(int i = 1;i <= T;i++)solve(i);
    return 0;
}
