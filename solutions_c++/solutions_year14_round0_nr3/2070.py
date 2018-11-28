#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int gra[55][55];
char ggg[4] = "c.*";
void out(int, int, int);
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
//    ios_base::sync_with_stdio(false);
    int r, c, rev, m, re;
    int C = 0;
    cin >> r;
    while (cin >> r >> c >> m)
    {
        cout << "Case #" << (++C) << ':' << endl;
        rev = 0;
        re = r*c - m;
        if (r > c)
        {
            swap(r, c);
            rev = 1;
        }
        if (r == 1)
        {
            for (int i=1;i<c;++i)
                gra[0][i] = 1 + (i >= re);
            out(r, c, rev);
        }
        else if (r == 2)
        {
//            cout << re << endl;
            if (((m&1)||(re < 4)) && re != 1)
                cout << "Impossible" << endl;
            else
            {
                for (int i=0;i<r;++i)
                    for (int j=0;j<c;++j)
                        gra[i][j] = 1 + (j >= re/2);
                out(r, c, rev);
            }
        }
        else
        {
            if ((re < 4 && re != 1) || re == 5 || re == 7)
                cout << "Impossible" << endl;
            else if(re == 1)
            {
                for (int i=0;i<r;++i)
                    for (int j=0;j<c;++j)
                        gra[i][j] = 2;
                out(r, c, rev);
            }
            else if(re == 4 || re == 6)
            {
                for (int i=0;i<r;++i)
                    for (int j=0;j<c;++j)
                        gra[i][j] = 2;
                for (int i=0;i<re/2;++i)
                    gra[i][0] = gra[i][1] = 1;
                out(r, c, rev);
            }
            else
            {
                int a = 3, b = 3, rr;
                for (;a*b < re && b<c;++b);
                for (;a*b < re && a<r;++a);
                rr = re - a*2-b*2+4;
                for (int i=0;i<r;++i)
                    for (int j=0;j<c;++j)
                    {
                        if (i >= a || j >= b)
                            gra[i][j] = 2;
                        else if (i < 2 || j < 2)
                            gra[i][j] = 1;
                        else if (rr)
                        {
                            gra[i][j] = 1;
                            --rr;
                        }
                        else
                            gra[i][j] = 2;
                    }
                out(r, c, rev);
            }

        }
    }
    return 0;
}
void out(int r, int c, int rev)
{
    gra[0][0] = 0;
    if (rev)
    {
        for (int i=0;i<c;++i, cout<<endl)
            for (int j=0;j<r;++j)
                cout << ggg[gra[j][i]];
    }
    else
        for (int i=0;i<r;++i, cout<<endl)
            for (int j=0;j<c;++j)
                cout << ggg[gra[i][j]];
}
