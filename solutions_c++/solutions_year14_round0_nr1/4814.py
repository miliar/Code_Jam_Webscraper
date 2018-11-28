#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;


typedef int Matrix[4][4];

Matrix A, B;

void ReadMatrix(Matrix m)
{
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            cin >> m[i][j];
}

int main()
{
    int T;
    cin >> T;

    for(int c=0; c<T; c++)
    {
        int row1, row2;

        cin >> row1; row1--;
        ReadMatrix(A);

        cin >> row2; row2--;
        ReadMatrix(B);

        bool sel[17];
        memset(sel, false, sizeof(sel));

        for(int j=0; j<4; j++)
            sel[A[row1][j]] = true;

        int selcount = 0, selval;
        for(int j=0; j<4; j++)
        {
            if(sel[B[row2][j]])
            {
                selval = B[row2][j];
                selcount++;
            }
        }

        printf("Case #%d: ", c+1);
        if(selcount == 0)
            printf("Volunteer cheated!\n");
        else if(selcount > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", selval);
    }

    return 0;
}
