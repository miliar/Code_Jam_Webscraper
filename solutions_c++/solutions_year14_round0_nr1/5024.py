#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cctype>

using namespace std;

int main(int argc, const char *argv[])
{
	string inputFileName = "A-small-attempt1.in";
	string outputFileName = "output.txt";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

    int test, a[10][10], b[10][10], row1, row2;
    int i, j, k, d, chk;

    scanf("%d",&test);

    for(k = 1; k<=test; k++)
    {
        scanf("%d",&row1);

        for(i = 1; i<=4; i++)
        {
            for(j = 1; j<=4; j++)
            {
                scanf("%d",&a[i][j]);
            }
        }

        scanf("%d",&row2);

        for(i = 1; i<=4; i++)
        {
            for(j = 1; j<=4; j++)
            {
                scanf("%d",&b[i][j]);
            }
        }

        chk = 0;
        for(i = 1; i<=4; i++)
        {
            for(j = 1; j<=4; j++)
            {
                if(a[row1][i] == b[row2][j])
                {
                    chk = chk + 1;
                    d = b[row2][j];

                }
            }

        }

        if(chk == 0)
        {
            printf("Case #%d: Volunteer cheated!\n", k);
        }
        else if(chk>1)
        {
             printf("Case #%d: Bad magician!\n",k);

        }

        else if(chk == 1)
        {
             printf("Case #%d: %d\n",k,d);
        }
   }
    return 0;
}
