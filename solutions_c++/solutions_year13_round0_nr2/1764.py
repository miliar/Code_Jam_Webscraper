#include<cstdio>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;
#define L(x) tree[x].ch[0]
#define R(x) tree[x].ch[1]
#define INF 0x7fffffff
#define inf 99999999.9
#define eps 1e-9
#define MAXN 100015
#define db double
#define op operator
#define cp const P&
#define cs const
//typedef __int64 ll;
int n,m,ar[105][105],tmp[105][105],row[105],line[105];
int ok(){
    for(int i = 0; i < n; i ++){
        for(int j = 0; j < m; j ++)
            if(ar[i][j] != tmp[i][j])
            return false;
    }
    return true;
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T,cas = 1;
    int i,j,k;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        memset(row,0,sizeof(row));
        memset(line,0,sizeof(line));
        for(i = 0; i < n; i ++){
            for(j = 0; j < m; j ++){
                scanf("%d",&ar[i][j]);
                row[i] = max(row[i],ar[i][j]);
                line[j] = max(line[j],ar[i][j]);
            }
        }
        for(i = 0; i < n; i ++){
            for(j = 0; j < m; j ++){
                tmp[i][j] = min(row[i],line[j]);
            }
        }
        printf("Case #%d: ",cas ++);
        if(ok()) puts("YES");
        else{
//            puts("");
//            for(i = 0; i < n; i ++){
//            for(j = 0; j < m; j ++)
//                printf("%d\t",ar[i][j]);
//            puts(" ");
//            }
//            puts("");
//            for(i = 0; i < n; i ++){
//            for(j = 0; j < m; j ++)
//                printf("%d\t",tmp[i][j]);
//            puts(" ");
//            }
            puts("NO");
        }
    }
return 0;
}
