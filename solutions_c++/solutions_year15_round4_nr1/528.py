#include <iostream>
#include <cstdio>

using namespace std;

int T, N, M;
char c[200][200];

int vx[] = {-1, 0, 1, 0};
int vy[] = {0, 1, 0, -1};

int ch(char c)
{
    if( c == '^' ) return 0;
    else if( c == '>' ) return 1;
    else if( c == 'v' ) return 2;
    else return 3;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d %d", &N, &M);

        for(int Ni = 0; Ni < N; Ni++)
            scanf("%s", c[Ni]);

        bool OK = true;
        int cnt = 0;

        for(int Ni = 0; Ni < N; Ni++)
            for(int Mi = 0; Mi < M; Mi++)
            {
                if( c[Ni][Mi] == '.' ) continue;

                int dir = ch(c[Ni][Mi] );

                bool fine = true;
                int x = Ni, y = Mi;

                while(1)
                {
                    x += vx[dir];
                    y += vy[dir];

                    if( 0 > x || x >= N || 0 > y || y >= M )
                    {
                        fine = false;
                        break;
                    }

                    if( c[x][y] != '.' ) break;
                }

                if( fine ) continue;

                cnt++;

                for(int i = 0; i < 4; i++)
                {
                    fine = true;

                    int x = Ni, y = Mi;

                    while(1)
                    {
                        x += vx[i];
                        y += vy[i];

                        if( 0 > x || x >= N || 0 > y || y >= M )
                        {
                            fine = false;
                            break;
                        }

                        if( c[x][y] != '.' ) break;
                    }

                    if( fine ) break;
                }

                if( !fine ) OK = false;
            }

        printf("Case #%d: ", Ti);
        if( !OK ) puts("IMPOSSIBLE");
        else printf("%d\n", cnt);
    }
}
