#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#define maxn 105
using namespace std;

char ch[maxn][maxn];
int r,c;

int check(int x,int y)
{
    int i;
    if (ch[x][y] == '.') return 0;
    int fl=0,fr=0,fu=0,fd=0,f;

    for ( i = 1 ; i < y ; i++)
        if (ch[x][i] != '.') fl=1;
    for ( i = y+1 ; i <= c ; i++)
        if (ch[x][i] != '.') fr=1;

    for ( i = 1 ; i < x ; i++)
        if (ch[i][y] != '.') fu=1;
    for ( i = x+1 ; i <= r ; i++)
        if (ch[i][y] != '.') fd=1;

    f=fl|fr|fu|fd;

    if (ch[x][y] == '<' && fl==1) return 0;
    if (ch[x][y] == '>' && fr==1) return 0;
    if (ch[x][y] == '^' && fu==1) return 0;
    if (ch[x][y] == 'v' && fd==1) return 0;

    if (f) return 1;
    else return -1;
}

int main()
{
    int T,tt=0;
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
    cin>>T;

    while (T--)
    {
        cin>>r>>c;
        printf("Case #%d: ",++tt);
        int i,j;
        for (i = 1 ; i <= r ; i++)
            for ( j = 1 ; j <= c ; j++)
                scanf(" %c",&ch[i][j]);

        int sum = 0;
        int flag = 1;

        for ( i = 1 ; i <= r ; i++)
            for ( j = 1 ; j <= c ; j++)
            {
               int x = check(i,j);
               if (x == -1)
               {
                   flag = 0;i = r+1;j=c+1;
               }
               else if (x == 1) sum++;
            }
        if (flag == 0) cout<<"IMPOSSIBLE"<<endl;
        else cout<<sum<<endl;
    }

    return 0;
}
