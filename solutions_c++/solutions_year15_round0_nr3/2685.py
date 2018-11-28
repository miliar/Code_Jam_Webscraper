#include <cstdio>
#include <cstring>
char S[10101], S2[10101];
int l, x, tab[10][10] = {
    { 0, 0, 0, 0, 0 },
    { 0, 1, 2, 3, 4 },
    { 0, 2, -1, 4, -3 },
    { 0, 3, -4, -1, 2 },
    { 0, 4, 3, -2, -1 },
};
int abs(int a){ return a>0?a:-a; }
int dt[11010][20][10][5];
bool dfs(int k, int cur, int target, bool just)
{
    bool ret = false;
    if( dt[k][cur+10][target][just] != -1 ) return dt[k][cur+10][target][just];
    if( k == l ) return target == 5 && just;
    int next = tab[abs(cur)][(int)(S[k+1]-'g')]*(cur<0?-1:1);
    if( cur == target ) ret |= dfs(k+1, (int)(S[(k+1)%l]-'g'), target+1, true);
    if( !ret ) ret |= dfs(k+1, next, target, false);
    return dt[k][cur+10][target][just] = ret;
}

int main()
{
    int T;
    freopen("C4.txt","r",stdin);
    freopen("resC.txt","w",stdout);
    scanf("%d", &T);
    for(int t = 1 ; t <= T ; t++ )
    {
        memset(dt, -1, sizeof(dt));
        scanf( "%d%d%s",&l,&x,S2);
        for(int i = 0 ; i < l*x ; i++ ) S[i] = S2[i%l];
        l*=x, x=1;
        printf( "Case #%d: %s\n", t, dfs(0,(int)(S[0]-'g'),2,true)?"YES":"NO");
    }
}

