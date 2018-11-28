#include <iostream>
#include <cstdio>
#include <set>
#define f cin
#define g cout
#define NM 10010

using namespace std;

string inverse[8];
int mult[8][8];

int minusv (int x)
{
    return (x<4?x+4:x-4);
}

void BuildOp ()
{
    inverse[0] = "-1";
    inverse[1] = "-i";
    inverse[2] = "-j";
    inverse[3] = "-k";

    inverse[4] = "1";
    inverse[5] = "i";
    inverse[6] = "j";
    inverse[7] = "k";
            ///    1                     i                     j                     k
    /* 1 */mult[4][4] = 4;/* 1*/ mult[4][5] = 5;/* i*/ mult[4][6] = 6;/* j*/ mult[4][7] = 7;/* k*/
    /* i */mult[5][4] = 5;/* i*/ mult[5][5] = 0;/*-1*/ mult[5][6] = 7;/* k*/ mult[5][7] = 2;/*-j*/
    /* j */mult[6][4] = 6;/* j*/ mult[6][5] = 3;/*-k*/ mult[6][6] = 0;/*-1*/ mult[6][7] = 5;/* i*/
    /* k */mult[7][4] = 7;/* k*/ mult[7][5] = 6;/* j*/ mult[7][6] = 1;/*-i*/ mult[7][7] = 0;/*-1*/

    for (int i=0; i<8; i++)
        for (int j=0; j<8; j++)
        {
            if (i>=4 && j>=4)
                continue;

            int a=i, b=j, cnt=0;
            if (i < 4)
            {
                a=i+4;
                cnt++;
            }
            if (j < 4)
            {
                b=j+4;
                cnt++;
            }

            if (cnt%2==0) //nr par de -
                mult[i][j] = mult[a][b];
            else
                mult[i][j] = minusv(mult[a][b]);
        }
}

void verif ()
{
    for (int i=0; i<8; i++)
    {
        for (int j=0; j<8; j++)
        {
            if (inverse[i].size()==1)
                g << ' ';
            if (inverse[j].size()==1)
                g << ' ';
            if (inverse[mult[i][j]].size()==1)
                g << ' ';
            g << inverse[i] << " * " << inverse[j] << " = " << inverse[mult[i][j]] << " | ";
        }
        g << '\n';
    }
}


int N;
long long X;
char S[NM];
int all;
int up[NM], down[NM], val[NM];
int pow[7];

void buildVal ()
{
    all = up[0] = down[N+1] = 4; // 1
    for (int i=1; i<=N; i++)
    {
        if (S[i]=='1')
            val[i] = 4;
        if (S[i]=='i')
            val[i] = 5;
        if (S[i]=='j')
            val[i] = 6;
        if (S[i]=='k')
            val[i] = 7;

        all = mult[all][val[i]];
        up[i] = mult[up[i-1]] [val[i]];
    }
    for (int i=N; i>=1; i--)
        down[i] = mult[val[i]] [down[i+1]]; // now * next

    pow[0] = 4; // 1
    for (int i=1; i<7; i++)
        pow[i] = mult[pow[i-1]][all];
}

bool CheckNoMid ()
{
    int i, j;
    int midVal;
    int a, b;
    for (i=1; i<=N; i++)
    {
        midVal = 4; // 1
        for (j=i; j<=N; j++)
        {
            midVal = mult[midVal][val[j]];
            //mid e intre i si j inclusiv
            if (midVal != 6) // nu e j
                continue;

            for (a=0; a<=3; a++)
                if (mult[pow[a]][up[i-1]] == 5) // de a ori all, apoi pana la (i-1) sa fie i
                    for (b=0; b<=3; b++)
                        if (mult[down[j+1]][pow[b]] == 7) // de la j+1 la N apoi de b ori all sa fie k
                            if (a+b+1<=X && (X-(a+b+1))%4==0) // acelasi rest cu 4
                                return true;
        }
    }

    return false;
}

bool CheckWithMid ()
{
    int i, j;
    int midVal;
    int fi, m, l;
    int add;

    for (i=1; i<=N+1; i++) // iau pana la i-1 din primu apoi de la i pana la N am midu
        for (j=0; j<=N; j++) // iau pana la j din mid apoi de la j+1 am ultimu
        {
            add=2;

            for (fi=0; fi<=3; fi++)
                if (mult[pow[fi]][up[i-1]] == 5) // de f ori all, apoi pana la i-1 sa fie i
                    for (m=1; m<=4; m++)
                        if (mult[ down[i] ] [ mult[pow[m]][up[j]] ] == 6) // de de la i pana la N, apoi de m ori mid, apoi pana la j
                            for (l=0; l<=3; l++)
                                if (mult[down[j+1]] [pow[l]] == 7) // de la j+1 la N, apoi de l ori last sa fie k
                                    if (fi + m + l + add <= X && (X - (fi + m + l + add))%4==0)
                                        return true;
        }

    return false;
}

bool Check ()
{
    if (CheckNoMid())
        return true;
    return CheckWithMid();
}

int main ()
{
    /*
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    /* */

    BuildOp();

    int T;
    f >> T;

    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";
        f >> N >> X;
        f >> (S+1);

        buildVal();
        if (Check())
            g << "YES\n";
        else
            g << "NO\n";
    }

    return 0;
}
