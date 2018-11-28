#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

char str[110][110];

int len[110];

int now[110];

int val[110];
char ch;
int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.txt","w",stdout);
    int x,n,ans,sol,X;
    double xx;
    scanf("%d",&x);
    for ( int t=1 ; t<=x ; t++ )
    {
        sol = 0;
        scanf("%d",&n);
        for ( int c=1 ; c<=n ; c++ )
        {
            scanf("%s",str[c]+1);
            len[c] = strlen(str[c]+1);
            now[c] = 1;
        }
        printf("Case #%d: ",t);
        while ( len[1]+1 != now[1] )
        {
            ans = 0;
            ch = str[1][now[1]];
            //printf("%c\n",ch);
            for ( int c=1 ; c<=n ; c++ )
            {
                val[c] = 0;
                for ( ; str[c][now[c]] == ch ; now[c]++ )  val[c]++;
                if ( val[c] == 0 )  goto bu;
                ans += val[c];
            }
            xx = (double) ans/n;
            if ( xx - int(xx) > 0.5 )   X = int(xx) + 1;
            else    X = int (xx);
            for ( int c=1 ; c<=n ; c++ )    sol += abs ( X-val[c]) /*printf("%d ",now[c])*/;
            //printf("\n");
        }
        for ( int c=1 ; c<=n ; c++ )
        {
            if ( len[c]+1 != now[c] ) goto bu;
        }
        printf("%d\n",sol);
        continue;
        bu:;
        printf("Fegla Won\n");
    }
}
