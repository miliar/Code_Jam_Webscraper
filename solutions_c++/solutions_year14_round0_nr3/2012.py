#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char gsp_map[55][55];

bool putMines(int fin_r, int fin_c, int fin_m, int fin_ofr, int fin_ofc)
{
    if (fin_m<0) return false;
    if (fin_r==1 || fin_c == 1) return false;
    if (fin_m==0) return true;
    int ln_mxmines = (fin_r-2)*(fin_c-2);
    int tn_cnt = 0;
    if (fin_m <= ln_mxmines)
    {
        for (int i=fin_ofr; i<fin_ofr+fin_r-2 && tn_cnt < fin_m; ++i)
        {
            for (int j=fin_ofc;j<fin_ofc+fin_c-2 && tn_cnt < fin_m;++j)
            {
                gsp_map[i][j] = '*';
                tn_cnt ++;
            }
        }
        return true;
    }
    else
    {
        if(putMines(fin_r-1, fin_c, fin_m-fin_c, fin_ofr+1, fin_ofc))
        {
            for (int j=fin_ofc;j<fin_c+fin_ofc;++j)
            {
                gsp_map[fin_ofr][j] = '*';
            }
            return true;
        }
        else if(putMines(fin_r, fin_c-1, fin_m-fin_r, fin_ofr, fin_ofc+1))
        {
            for (int j=fin_ofr;j<fin_r+fin_ofr;++j)
            {
                gsp_map[j][fin_ofc] = '*';
            }
            return true;
        }
        else
            return false;
    }
}

void solve(int ln_cas)
{
    int ln_r,ln_c,ln_m;
    scanf("%d%d%d", &ln_r, &ln_c, &ln_m);
    for (int i=0;i<ln_r;++i)
    {
        for (int j=0;j<ln_c;++j)
        {
            gsp_map[i][j] = '.';
        }
    }
    if (ln_m==ln_r*ln_c-1)
    {
        for (int i=0;i<ln_r;++i)
        {
            for (int j=0;j<ln_c;++j)
            {
                gsp_map[i][j] = '*';
            }
        }
        gsp_map[ln_r-1][ln_c-1] = 'c';
        for (int i=0;i<ln_r;++i)
        {
            for (int j=0;j<ln_c;++j)
            {
                printf("%c", gsp_map[i][j]);
            }
            puts("");
        }
        return ;
    }
    int ln_mn = (ln_r<ln_c)?ln_r:ln_c;
    bool lb_longside = (ln_mn==ln_r);
    if (ln_mn==1)
    {
        if (lb_longside)
        {
            for (int i=0;i<ln_m;++i)
                gsp_map[0][i] = '*';
            gsp_map[0][ln_c-1] = 'c';
        }
        else
        {
            for (int i=0;i<ln_m;++i)
                gsp_map[i][0] = '*';
            gsp_map[ln_r-1][0] = 'c';
        }
        for (int i=0;i<ln_r;++i)
        {
            for (int j=0;j<ln_c;++j)
            {
                printf("%c", gsp_map[i][j]);
            }
            puts("");
        }
        return ;
    }
    if (ln_mn==2)
    {
        if ((ln_m&1)||(ln_m==ln_r*ln_c-2))
        {
            puts("Impossible");
        }
        else
        {
            if (lb_longside)
            {
                for (int i=0;i<ln_m/2;i++)
                {
                    gsp_map[0][i] = '*';
                    gsp_map[1][i] = '*';
                }
            }
            else
            {
                for (int i=0;i<ln_m/2;i++)
                {
                    gsp_map[i][0] = '*';
                    gsp_map[i][1] = '*';
                }
            }
            gsp_map[ln_r-1][ln_c-1] = 'c';
            for (int i=0;i<ln_r;++i)
            {
                for (int j=0;j<ln_c;++j)
                {
                    printf("%c", gsp_map[i][j]);
                }
                puts("");
            }
        }
        return ;
    }
    if (putMines(ln_r, ln_c, ln_m, 0, 0))
    {
        gsp_map[ln_r-1][ln_c-1] = 'c';
        for (int i=0;i<ln_r;++i)
        {
            for (int j=0;j<ln_c;++j)
            {
                printf("%c", gsp_map[i][j]);
            }
            puts("");
        }
    }
    else puts("Impossible");
}

int main()
{
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-small-attempt0.out","w",stdout);
    int ln_t;
    scanf("%d", &ln_t);
    for (int ln_cas=1;ln_cas<=ln_t;++ln_cas)
    {
        printf("Case #%d:\n", ln_cas);
        solve(ln_cas);
    }
    return 0;
}
