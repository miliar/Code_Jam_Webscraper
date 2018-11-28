#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>

using namespace std;


void solve(int test_num)
{
    int cur_have = (1<<16) - 1;
    for (int q = 0; q < 2; q++) {
        int ans;
        scanf("%d", &ans);
        ans--;
        for (int i = 0; i < 4; i++)
        {
            int curmask = 0;
            for (int j = 0; j < 4; j++)
            {
                int x;
                scanf("%d", &x);
                x--;
                curmask = curmask | (1 << x);
            }
            
            if (i == ans) {
                cur_have &= curmask;
            }
        }
    }
    
    int count = 0, chosen;
    for (int i = 0; i < 16; i++)
        if ((cur_have >> i) & 1) {
            count++;
            chosen = i;
        }
        
    printf("Case #%d: ", test_num + 1);
    if (count > 1) {
        printf("Bad magician!\n");
    } else if (!count) {
        printf("Volunteer cheated!\n");
    } else  {
        printf("%d\n", chosen + 1);
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        solve(i);
}