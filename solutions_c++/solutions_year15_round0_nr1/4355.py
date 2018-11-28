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
    char in[] = "A-large.in";
    char out[] = "A-large.out";
    freopen(in, "r", stdin);
    freopen(out, "w", stdout);
    int T, Smax, Si, guests, i, caseNum = 0;
    scanf("%d", &T);
    while(T--)
    {
        guests = 0;
        int res = 0;
        scanf("%d", &Smax);
        getchar();
        for(int i=0; i<=Smax; i++)
        {
            Si = getchar()-'0';
//            printf("van %d i %d Si %d\n", guests, i, Si);
            res += guests < i ? i - guests : 0;
            guests += guests < i ? i - guests : 0;
            guests += Si;
        }
        printf("Case #%d: %d\n", ++caseNum, res);
    }
    return 0;
}
