// gcj 2015 
// problem A

#include <iostream>
#include <cstdio>

using namespace std;

#define MAXN 1010

char s[MAXN];

int main()
{
    int test_case, test_case_now;
    int i, j, res, n;
    
    scanf("%d", &test_case);
    
    for (test_case_now = 1; test_case_now <= test_case; test_case_now++)
    {
        scanf("%d%s", &n, s);
        res = 0;
        j = int(s[0] - '0');
        for (i = 1; i <= n; i++)
        {
            if (j < i)
            {
                  res += (i - j);
                  j = i;
            }
            
            j += int(s[i] - '0');
        }
        
        printf("Case #%d: %d\n", test_case_now, res);
    }
    
    return 0;
}
