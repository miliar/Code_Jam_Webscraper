#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
    int T, n, temp;
    int cnt[10];
    
    scanf("%d", &T);
    
    for (int test = 1; test <= T; test++)
    {
        scanf("%d", &n);
        fill(cnt, cnt + 10, 0);
        temp = 0;
        
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", test);
        }
        else
        {
            for (int i = 1; i <10000; i++)
            {
                temp = n * i;
                
                while (temp > 0)
                {
                    cnt[temp % 10]++;
                    temp /= 10;
                }
                
                if (cnt[0] > 0 && cnt[1] > 0 && cnt[2] > 0 && cnt[3] > 0 && cnt[4] > 0 && cnt[5] > 0 && cnt[6] > 0 && cnt[7] > 0 && cnt[8] > 0 && cnt[9] > 0)
                {
                    printf("Case #%d: %d\n", test, n * i);
                    break;
                }
            }
        }
    }
    
    return 0;
}