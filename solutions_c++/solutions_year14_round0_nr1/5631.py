#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cassert>
using namespace std;

int order[4][4];
int S[2][4];
vector<int> ints;

void test(int testNum)
{
    int round, row, i, j;
    for(round = 0; round < 2; ++round)
    {
        scanf("%d", &row);
        for(i = 0; i < 4; ++i)
            for(j = 0; j < 4; ++j)
                scanf("%d", &order[i][j]);
        for(j = 0; j < 4; ++j)
            S[round][j] = order[row - 1][j];
    }
    ints.clear();
    for(i = 0; i < 4; ++i)
        for(j = 0; j < 4; ++j)
            if(S[0][i] == S[1][j])
                ints.push_back(S[0][i]);
    
    printf("Case #%d: ", testNum);
    if(ints.size() == 0)
        puts("Volunteer cheated!");
    else if(ints.size() == 1)
        printf("%d\n", ints[0]);
    else
        puts("Bad magician!");
}

int main()
{
    assert(freopen("/Users/seriy/Google Code Jam 2014/Qualification Round/A/A/A-small-attempt1.in", "r", stdin) != NULL);
    freopen("/Users/seriy/Google Code Jam 2014/Qualification Round/A/A/output.txt", "w", stdout);
    int t, testn;
    scanf("%d", &testn);
    for(t = 1; t <= testn; ++t)
        test(t);
    return 0;
}

