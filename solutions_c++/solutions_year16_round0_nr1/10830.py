#include <iostream>
#include <string>
#include <cstdio>
#include <set>
using namespace std;

#define USEFILE

int main(void)
{
    
#ifdef USEFILE
    FILE* inf = freopen("A.in", "r", stdin);
    FILE* outf = freopen("A_out.txt", "w", stdout);
#endif
    
    
    int tc;
    cin >> tc;
    for(int tcNum = 1; tcNum <= tc; tcNum++)
    {
        long long n;
        cin >> n;
        
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", tcNum);
            continue;
        }
        
        set<char> digits;
        for(int i = 1; i < 5000; i++)
        {
            long long lastNum = n * i;
            
            char numStr[100] = {0, };
            sprintf(numStr, "%lld", lastNum);
            
            string lastNumStr = string(numStr);
            for(int i = 0; i < lastNumStr.size(); i++)
            {
                digits.insert(lastNumStr[i]);
            }
            
            if(digits.size() == 10)
            {
                printf("Case #%d: %lld\n", tcNum, lastNum);
                break;
            }
        }
        
        if(digits.size() != 10)
        {
            printf("Case #%d: INSOMNIA\n", tcNum);
        }
    }
    
    
    return 0;
}
