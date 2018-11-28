#include <cstdio>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <deque>
#include <cmath>

using namespace std;

int main()
{
    char in[] = "D-small-attempt0.in";
    char out[] = "D-small-attempt0.out";
    freopen(in, "r", stdin);
    freopen(out, "w", stdout);
    int T,X,R,C, caseNum=0;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d %d %d", &X, &R, &C);
        if(X == 1)
            printf("Case #%d: GABRIEL\n", ++caseNum);
        else if(X == 2)
        {
            if(R%2 == 0 or C%2 == 0)
                printf("Case #%d: GABRIEL\n", ++caseNum);
            else
                printf("Case #%d: RICHARD\n", ++caseNum);
        }
        else if(X == 3)
        {
            if(R%3 and C%3)
                printf("Case #%d: RICHARD\n", ++caseNum);
            else
            {
                if(R*C == 3)
                    printf("Case #%d: RICHARD\n", ++caseNum);
                else
                    printf("Case #%d: GABRIEL\n", ++caseNum);
            }
        }
        else
        {
            if(R%4 and C%4)
                printf("Case #%d: RICHARD\n", ++caseNum);
            else
            {
                if(R*C == 4 or R*C == 8)
                    printf("Case #%d: RICHARD\n", ++caseNum);
                else
                    printf("Case #%d: GABRIEL\n", ++caseNum);
            }
        }
    }
    return 0;
}
