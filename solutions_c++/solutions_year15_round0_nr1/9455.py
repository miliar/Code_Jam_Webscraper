#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

char buf[1001];

int solve(int levels)
{
    //printf("solving for %d levels\n", levels);
    int cheering = 0;
    int res = 0;
    for(int i = 0; i < levels; ++i)
    {
        if(cheering < i)
        {
            const int extra = i-cheering;
            res += extra;
            cheering += extra;
        }
        cheering += (int)  (buf[i] - '0');
    }
    return res;
}


int main()
{
    int test_cases;
    scanf(" %d ", &test_cases);
    for(int count = 0; count < test_cases; ++count)
    {
        int levels;
        scanf(" %d ", &levels);
        scanf(" %[^\n]", buf);//read line, consuming leading whitespace.
        printf("Case #%d: %d\n", count+1, solve(levels+1));
    }
    fflush(stdout);
    return EXIT_SUCCESS;
}


