/*
TASK: Minesweeper Master
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T,R,C;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k,a,b;
    scanf("%d",&T);
    int tt=0;
    char tb[55][55];
    while(T--)
    {
        scanf("%d%d%d",&R,&C,&M);
        tt++;
        printf("Case #%d:\n",tt);
        if(R==1 || C==1)
        {
            if(R==1)
            {
                for(i=1;i<=M;i++)
                    printf("*");
                for(i=M+1;i<=R*C-1;i++)
                    printf(".");
                printf("c\n");
            }
            else
            {
                for(i=1;i<=M;i++)
                    printf("*\n");
                for(i=M+1;i<=R*C-1;i++)
                    printf(".\n");
                printf("c\n");
            }
        }
        else if(R==2 || C==2)
        {
            if((M%2==1 && R*C-M!=1) || R*C-M==2)
                printf("Impossible\n");
            else
            {
                k=M/2;
                if(R==2)
                {
                    for(i=1;i<=k;i++)   printf("*");
                    for(;i<C;i++)       printf(".");
                    printf("c\n");
                    for(i=1;i<=k;i++)   printf("*");
                    for(;i<C;i++)       printf(".");
                    printf("%c",M%2? '*':'.');
                    printf("\n");
                }
                else
                {
                    for(i=1;i<=k;i++)   printf("**\n");
                    for(;i<R;i++)       printf("..\n");
                    printf("%cc\n",M%2? '*':'.');
                }
            }
        }
        else if(R==3 || C==3)
        {
            k=R*C-M;
            if(k==2 || k==3 || k==5 || k==7)
            {
                printf("Impossible\n");
                continue;
            }
            memset(tb,0,sizeof tb);
            int x=max(R,C),y=min(R,C);
            for(i=1;i<=x;i++)
                for(j=1;j<=y;j++)
                    tb[i][j]='.';
            tb[x][y]='c';
            N=M;
            for(i=1;i<=x && N;i++)
                for(j=1;j<=3 && N;j++)
                    tb[i][j]='*',N--;
            if(M%3==2)
            {
                for(i=1;i<=x;i++)
                {
                    if(tb[i][2]=='*' && tb[i][3]=='.')
                    {
                        tb[i+1][1]='*';
                        tb[i][2]='.';
                        break;
                    }
                }
            }
            if(x==R)
            {
                for(i=1;i<=x;i++)
                {
                    for(j=1;j<=y;j++)
                        printf("%c",tb[i][j]);
                    printf("\n");
                }
            }
            else
            {
                for(i=1;i<=y;i++)
                {
                    for(j=1;j<=x;j++)
                        printf("%c",tb[j][i]);
                    printf("\n");
                }
            }
        }
        else
        {
            k=R*C-M;
            if(k==2 || k==3 || k==5 || k==7)
                printf("Impossible\n");
            else
            {
                int x=R,y=C;
                R=min(x,y);
                C=max(x,y);
                memset(tb,0,sizeof tb);
                for(i=1;i<=R;i++)
                    for(j=1;j<=C;j++)
                        tb[i][j]='.';
                tb[R][C]='c';
                // process
                // block A
                for(i=1;i<=R-2 && M;i++)
                    for(j=1;j<=C-2 && M;j++)
                        tb[i][j]='*',M--;
                // block B
                if(M%2 && k!=1) M++,tb[R-2][C-2]='.';
                j=1,i=R-1,a=1,b=C-1;
                while(j<=C-2 && M)
                {
                        for(i=R-1;i<=R && M;i++)
                            tb[i][j]='*',M--;

                        for(b=C-1;b<=C && M;b++)
                            tb[a][b]='*',M--;
                    j++,a++;
                }

                // block D
                if(M)
                {
                    tb[R-1][C-1]='*';
                    tb[R-1][C]='*';
                    tb[R][C-1]='*';
                }
                // print
                if(R==x)
                {
                    for(i=1;i<=R;i++)
                    {
                        for(j=1;j<=C;j++)
                            printf("%c",tb[i][j]);
                        printf("\n");
                    }
                }
                else
                {
                    for(i=1;i<=C;i++)
                    {
                        for(j=1;j<=R;j++)
                            printf("%c",tb[j][i]);
                        printf("\n");
                    }
                }
            }
        }
    }
}
