#include <iostream>
#include <cstdio>
#define f cin
#define g cout

using namespace std;

int T;
int A[10][10], B[10][10];
int l1, l2;

void Read ()
{
    f >> l1;
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            f >> A[i][j];

    f >> l2;
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            f >> B[i][j];
}

void Solve ()
{
    int cnt=0, match=-1;

    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            if (A[l1][i]==B[l2][j])
            {
                match=A[l1][i];
                cnt++;
            }

    if (cnt==0)
        g << "Volunteer cheated!" << '\n';
    if (cnt==1)
        g << match << '\n';
    if (cnt>=2)
        g << "Bad magician!" << '\n';
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
        Read();

        g << "Case #" << t << ": ";
        Solve();
    }

    return 0;
}
