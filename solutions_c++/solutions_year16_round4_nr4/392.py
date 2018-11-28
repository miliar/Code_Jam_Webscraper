#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

char c[20][20];
int per[20];

bool hv[20];
int N;

bool check(int P, int learn)
{
    if( P == N ) return true;
    int O = per[P];

    bool flag = false;

    for(int Ni = 0; Ni < N; Ni++)
        if( !hv[Ni] && ( (learn&(1<<(O*N+Ni) ) ) || c[O][Ni] == '1') ) flag = true;

    if( !flag ) return false;

    for(int Ni = 0; Ni < N; Ni++)
        if( !hv[Ni] && ( (learn&(1<<(O*N+Ni) ) ) || c[O][Ni] == '1') )
        {
            hv[Ni] = true;

            if( !check(P+1, learn) )
            {
                hv[Ni] = false;
                return false;
            }

            hv[Ni] = false;
        }

    return true;
}

int main()
{
    freopen("D-small.in", "r", stdin);
    freopen("D-small_out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {

        scanf("%d", &N);

        for(int Ni = 0; Ni < N; Ni++)
            scanf("%s", c[Ni]);

        int ans = N*N;

        for(int i = 0; i < (1<<(N*N) ); i++)
        {
            for(int Ni = 0; Ni < N; Ni++)
                per[Ni] = Ni;

            int cnt = 0;

            while(1)
            {
                if( !check(0, i) ) goto flag;

                if( !next_permutation(per, per+N) ) break;
            }

            for(int Ni = 0; Ni < N; Ni++)
                for(int Nj = 0; Nj < N; Nj++)
                    if( c[Ni][Nj] == '0' && (i&(1<<(Ni*N+Nj) ) ) )
                        cnt++;

            ans = min(ans, cnt);
            flag:;
        }

        printf("Case #%d: %d\n", Ti, ans);
    }
}
