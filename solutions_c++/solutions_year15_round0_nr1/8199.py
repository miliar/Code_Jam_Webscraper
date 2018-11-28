#include <cstdio>
#include <cstring>

using namespace std;

int v[2000];
char audience[2000];

int main()
{
    freopen("/Users/Cosmin/Documents/info/Standing Ovation/Standing Ovation/in", "r", stdin);
    
    freopen("/Users/Cosmin/Documents/info/Standing Ovation/Standing Ovation/out", "w", stdout);
    
    int t, smax, needed, sum;
    
    scanf("%d\n", &t);
    
    for(int i = 1; i <= t; i ++)
    {
        scanf("%d ", &smax);
        
        gets(audience);
        
        needed = 0;
        sum = audience[0] - '0';
        
        for(int j = 1; j <= smax; j ++)
        {
            if(j > sum)
            {
                needed = needed + j - sum;
                sum = sum + audience[j] - '0' + j - sum;
            }
            else
                sum = sum + audience[j] - '0';
        }
        printf("Case #%d: %d\n", i, needed);
    }
    
    return 0;
}