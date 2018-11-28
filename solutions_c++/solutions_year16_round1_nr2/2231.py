#include<bits/stdc++.h>
using namespace std;


const int maxn = 100+10;
int n;

int A[maxn][maxn];
int res[maxn][maxn];

//int seq[maxn];
//
//int
//
//bool cmp0(int a,int b)
//{
//    return A[a][id] < A[b][id];
//}
//
//bool cmp1(int a,int b)
//{
//    return A[a][id] > A[b][id];
//}
//
//bool used[maxn];
//
//bool judgecol(int id,int c)
//{
//    for(int i = 1;i <= n;++i)
//        if(res[i][c] != -1)
//            if(res[i][c] != A[id][i])
//                return false;
//    return true;
//}
//
//
//bool solve(int r1,int c1,int r2,int c2,int remain)
//{
//    int cnt = 0;
//    for(int i = 1;i <= 2*n-1;++i)
//        if(!used[i])
//        {
//            seq[++cnt] = i;
//        }
//
//    id = r1;
//    sort(seq+1,seq+1+cnt,cmp0);
//    int nowlft = seq[1];
//    if(judgecol(nowlft,c1))
//    {
//
//    }
//



vector<int> G[maxn];

int seq[maxn];
int used[maxn];


int ss[maxn];

void print()
{
for(int i = 1;i <= n;++i)
            for(int j = 1;j <= n;++j)
                printf("%d%c",res[i][j]," \n"[j == n]);

}

int ttt;

bool cmp(int a,int b)
{
    for(int i = 1;i <= n;++i)
        if(A[a][1] != A[b][1])
            return A[a][1] < A[b][1];
//    return A[a][1] < A[b][1];
}
bool dfs(int c)
{

    if(c > n)
    {
  //      puts("************  ");
        int cnt = 0;
        for(int i = 1;i <= 2*n-1;++i)
            if(!used[i])
            {
                ss[++cnt] = i;
            }
//            else
//                printf("*   %d\n",i);
//        puts("        ");
//
//        printf("***** %d\n",cnt);


        sort(ss+1,ss+1+cnt,cmp);

        assert(cnt == n-2);
        int xx = 0;
        int cur =  1;
        for(int i = 2;i <= n;++i)
        {
            if(i == n && xx == 0)
            {
                ttt = i;
                return true;
            }
            int p = ss[cur];
            bool flag = true;
            for(int j = 1;j <= n;++j)
            {
                assert(res[i][j] != -1);
                if(res[i][j] != A[p][j])
                {
                    xx++;
                    flag = false;
                    ttt = i;

                    break;
                }
            }


         //   printf("****  %d %d\n",i,xx);
            if(flag)
                cur++;
            if(xx > 1) return false;
        }


        return xx <= 1;
    }

    for(int i = 0;i < G[c].size();++i)
    {
        int nowlft = G[c][i];
        used[nowlft] = 1;
        for(int j = 2;j <= n;++j)
            res[j][c] = A[nowlft][j];

        if(dfs(c+1)) return true;
        used[nowlft] = 0;
        for(int j = 2;j <= n;++j)
            res[j][c] = -1;
    }
    return false;

}


bool dfsx(int c)
{

    if(c > n)
    {
  //      puts("************  ");
        int cnt = 0;
        for(int i = 1;i <= 2*n-1;++i)
            if(!used[i])
            {
                ss[++cnt] = i;
            }


        sort(ss+1,ss+1+cnt,cmp);

        assert(cnt == n-2);
        int xx = 0;
        int cur =  1;
        for(int i = 1;i <= n-1;++i)
        {
            if(i == n-1 && xx == 0)
            {
                ttt = i;
                return true;
            }
            int p = ss[cur];
            bool flag = true;
            for(int j = 1;j <= n;++j)
            {
                assert(res[i][j] != -1);
                if(res[i][j] != A[p][j])
                {
                    xx++;
                    flag = false;
                    ttt = i;

                    break;
                }
            }


         //   printf("****  %d %d\n",i,xx);
            if(flag)
                cur++;
            if(xx > 1) return false;
        }


        return xx <= 1;
    }

    for(int i = 0;i < G[c].size();++i)
    {
        int nowlft = G[c][i];
        used[nowlft] = 1;
        for(int j = 1;j <= n-1;++j)
            res[j][c] = A[nowlft][j];

        if(dfsx(c+1)) return true;
        used[nowlft] = 0;
        for(int j = 1;j <= n-1;++j)
            res[j][c] = -1;
    }
    return false;

}

bool cmpx(int a,int b)
{
    for(int i = n;i >= 1;--i)
        if(A[a][n] != A[b][n])
            return A[a][n] > A[b][n];
  //  return A[a][n] > A[b][n];
}

bool solve()
{
    memset(res,-1,sizeof(res));
    for(int i = 0;i < maxn;++i) G[i].clear();

    for(int i = 1;i <= 2*n-1;++i)
            seq[i] = i;
    sort(seq+1,seq+1+2*n-1,cmp);
    int nowup = seq[1];
    memset(used,0,sizeof(used));
    used[nowup] = 1;
    for(int i = 1;i <= n;++i)
    {
        res[1][i] = A[nowup][i];
        for(int j = 1;j <= 2*n-1;++j)
            if(!used[j] && A[j][1] == res[1][i])
                G[i].push_back(j);


    }

    //print();
    ttt = -1;
    if(dfs(1)) return true;


    memset(res,-1,sizeof(res));
    for(int i = 0;i < maxn;++i) G[i].clear();

    nowup = seq[2];

    memset(used,0,sizeof(used));
    used[nowup] = 1;
    for(int i = 1;i <= n;++i)
    {
        res[1][i] = A[nowup][i];
        for(int j = 1;j <= 2*n-1;++j)
            if(!used[j] && A[j][1] == res[1][i])
                G[i].push_back(j);


    }

    ttt = -1;
    if(dfs(1)) return true;



    memset(res,-1,sizeof(res));
    for(int i = 0;i < maxn;++i) G[i].clear();

    for(int i = 1;i <= 2*n-1;++i)
            seq[i] = i;
    sort(seq+1,seq+1+2*n-1,cmpx);
     nowup = seq[1];
    memset(used,0,sizeof(used));
    used[nowup] = 1;
    for(int i = 1;i <= n;++i)
    {
        res[n][i] = A[nowup][i];
        for(int j = 1;j <= 2*n-1;++j)
            if(!used[j] && A[j][n] == res[n][i])
                G[i].push_back(j);

    }

    ttt = -1;
    if(dfsx(1)) return true;


    memset(res,-1,sizeof(res));
    for(int i = 0;i < maxn;++i) G[i].clear();

    for(int i = 1;i <= 2*n-1;++i)
            seq[i] = i;
    sort(seq+1,seq+1+2*n-1,cmpx);
    nowup = seq[2];
    memset(used,0,sizeof(used));
    used[nowup] = 1;
    for(int i = 1;i <= n;++i)
    {
        res[n][i] = A[nowup][i];
        for(int j = 1;j <= 2*n-1;++j)
            if(!used[j] && A[j][n] == res[n][i])
                G[i].push_back(j);

    }

    ttt = -1;
    if(dfsx(1)) return true;

    return false;

}

int main()
{
    freopen("./B-small-attempt1.in","r",stdin);
    freopen("./out.txt","w",stdout);
  // freopen("./test.txt","r",stdin);
    int kase;
    scanf("%d",&kase);
    for(int z = 1;z <= kase;++z)
    {
        scanf("%d",&n);
        for(int i = 1;i <= 2*n-1;++i)
            for(int j = 1;j <= n;++j)
                scanf("%d",&A[i][j]);



        printf("Case #%d:",z);
        assert(solve());
        assert(ttt != -1);

        for(int i = 1;i <= n;++i)
            printf(" %d",res[ttt][i]);
        putchar('\n');
       // printf("xxxx %d\n",ttt);



    }
    return 0;
}
