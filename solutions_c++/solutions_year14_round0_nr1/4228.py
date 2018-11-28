#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int a[2];
int b[2][4][4];

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; ++test)
    {
        for (int k = 0; k < 2; ++k)
        {
            scanf("%d", &a[k]);
            for (int i = 0; i < 4; ++i)
                for (int j = 0; j < 4; ++j)
                    scanf("%d", &b[k][i][j]);
        }
        vector <int> answers;
        for (int i = 1; i <= 16; ++i)
        {
            int ok = 0;
            for (int k = 0; k < 2; ++k)
            {
                for (int j = 0; j < 4; ++j)
                    if (b[k][a[k] - 1][j] == i)
                    {
                        ++ok;
                        break;
                    }
            }
            if (ok == 2)
                answers.push_back(i);
        }
        printf("Case #%d: ", test);
        if (answers.empty())
            printf("Volunteer cheated!\n");
        else if (answers.size() > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", answers[0]);
    }


    return 0;
}