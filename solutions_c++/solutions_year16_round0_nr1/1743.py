#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cfloat>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#define ARBLIMIT 1000
using namespace std;

int main()
{
    int n, T;
    scanf("%d", &T);
    for(int t=1; t <= T; ++t)
    {
        scanf("%d", &n);
        printf("Case #%d: ", t);
        if(n)
        {
            int unseen[10] = {true, true, true, true, true, true, true, true, true, true};
            int numSeen = 0;
            long long result = n;

            for(int i=1; i <= ARBLIMIT; ++i)
            {
                long long tmp = result;
                while(tmp > 0)
                {
                    if(unseen[tmp%10])
                    {
                        unseen[tmp%10] = false;
                        if(++numSeen == 10)
                            break;
                    }

                    tmp /= 10;
                }

                if(numSeen == 10)
                {
                    printf("%lld", result);
                    break;
                }

                result += n;
            }
        }
        else
            printf("INSOMNIA");
        printf("\n");
    }

    return 0;
}
