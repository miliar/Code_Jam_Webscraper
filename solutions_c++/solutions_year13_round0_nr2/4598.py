#include<iostream>
#include<cstdio>
#include<cstdlib>

int grass[105][105];
int m,n;

void read()
{
    int i,j;
    scanf("%d%d", &n, &m);
    for(i=0; i<n; ++i)
        for(j=0; j<m; ++j)
            scanf("%d", &grass[i][j]);
}

bool lawn(int &r, int &c)
{
    int i(0);
    for(i=0; i<n; ++i)
    {
        if(grass[i][c]>grass[r][c])
            goto LINE_ROW;
    }
    return true;
LINE_ROW:
    for(i=0; i<m; ++i)
    {
        if(grass[r][i]>grass[r][c])
            return false;
    }
    return true;
}

bool pt()
{
    int i(0),j(0);
    for(i=0; i<n; ++i)
    {
        for(j=0; j<m; ++j)
        {
            if( !lawn(i,j) )
                return false;
        }
    }
    return true;

}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("b_s.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; )
    {
        read();
        if( pt() )
            printf("Case #%d: YES\n", ++i);
        else printf("Case #%d: NO\n", ++i);
    }
    return 0;
}
