#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <vector>
#include <map>
#include <bitset>
#include <set>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>

using namespace std;
/* Define Data-types */

int main()
{
    /* Input routine */
    int T;
    scanf("%d",&T);
    for(int test_case = 0; test_case < T; test_case++)
    
{        int row1, row2;
        bool pos[17] = {0};
        scanf("%d",&row1);
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                int temp;
                scanf("%d", &temp);
                if(i+1==row1)
                    pos[temp] = true;
            }
        }
        scanf("%d",&row2);
        int sol = 0;
        int n_sol = 0;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                int temp;
                scanf("%d", &temp);
                if(i+1==row2)
                {
                    if(pos[temp])
                    {
                        n_sol++;
                        sol = temp;
                    }
                }
            }
        }

        if(n_sol==1)
        {
            printf("Case #%d: %d\n", test_case+1, sol);
        }
        else if (n_sol>1)
        {
            printf("Case #%d: Bad magician!\n", test_case+1);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n", test_case+1);
        }
    }




    return 0;
}

