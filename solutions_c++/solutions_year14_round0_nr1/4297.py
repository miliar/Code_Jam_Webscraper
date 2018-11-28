#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>

using namespace std;



int main()
{
    int t;
    bool cards[17];
    int ans1, ans2, tmp, count, ind;

    scanf("%d", &t);

    for(int k = 1; k <= t; ++k)
    {
        for(int i = 1; i <= 16; ++i)
            cards[i] = false;
        
        scanf("%d", &ans1);
        for(int i = 1; i <= 4; ++i)
        {
            for(int j = 1; j <= 4; ++j)
            {
                scanf("%d", &tmp);
                if(i == ans1)
                {
                    cards[tmp] = true;
                }
            }
        }
        count = 0;
        scanf("%d", &ans2);
        for(int i = 1; i <= 4; ++i)
        {
            for(int j = 1; j <= 4; ++j)
            {
                scanf("%d", &tmp);
                if(i == ans2 && cards[tmp])
                {
                    ++count;
                    ind = tmp;
                }
            }
        }
        if(count > 1)
        {
            printf("Case #%d: Bad magician!\n", k);
        }
        else if(count)
        {
            printf("Case #%d: %d\n", k, ind);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n", k);
        }
    }

    return 0;
}
