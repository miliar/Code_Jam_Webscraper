#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#define f cin
#define g cout

using namespace std;

int T;
int R, C, M;
char Mat[100][100];
bool found;
queue< pair<int, int> > Q;

void Print ()
{
    Mat[1][1]='c';
    for (int i=1; i<=R; i++)
    {
        for (int j=1; j<=C; j++)
            g << Mat[i][j];
        g << '\n';
    }
}

const int dx[8]= {-1, 0, 1, 0, 1, 1, -1, -1};
const int dy[8]= {0, 1, 0, -1, 1, -1, 1, -1};

int hash=0;
int Viz[100][100];

bool IsOK ()
{
    hash++;

    Q.push(make_pair(1, 1));
    Viz[1][1]=hash;


    int i, j;
    while (!Q.empty())
    {
        i=Q.front().first;
        j=Q.front().second;
        Q.pop();

        int cnt=0;
        for (int d=0; d<8; d++)
            if (Mat[i+dx[d]][j+dy[d]]=='*')
                cnt++;

        if (cnt!=0)
            continue;

        for (int d=0; d<8; d++)
            if (Mat[i+dx[d]][j+dy[d]]=='.' && Viz[i+dx[d]][j+dy[d]]!=hash)
            {
                Viz[i+dx[d]][j+dy[d]]=hash;
                Q.push(make_pair(i+dx[d], j+dy[d]));
            }
    }

    for (int i=1; i<=R; i++)
        for (int j=1; j<=C; j++)
            if (Mat[i][j]=='.' && Viz[i][j]!=hash)
                return 0;

    return 1;
}

void Back (int i, int j, int rem)
{
    if (j>C)
    {
        i++;
        j=1;
    }

    if (i>R)
    {
        if (rem==0 && IsOK())
            found=1;
        return;
    }

    if (rem>0 && found==0)
    {
        Mat[i][j]='.';
        Back(i, j+1, rem-1);
    }
    if (found==0 && (i!=1 || j!=1))
    {
        Mat[i][j]='*';
        Back(i, j+1, rem);
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
#endif

    f >> T;
    for (int t=1; t<=T; t++)
    {
        f >> R >> C >> M;

        g << "Case #" << t << ":\n";

        memset(Mat, 0, sizeof(Mat));
        found=0;

        Back(1, 1, R*C-M);

        if (found)
            Print();
        else
            g << "Impossible\n";
    }

    return 0;
}



