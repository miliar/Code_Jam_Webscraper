#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;
int T;

int main()
{
    scanf("%d", &T);
    
    for(int t = 1; t <= T; t++)
    {
        char bidule[105];
        scanf("%s", bidule);
        printf("Case #%d: ", t);
        
        int N = strlen(bidule);
        
        int step = (bidule[N-1]=='-');
        
        for(int i = 0; i < N-1; i++)
            if(bidule[i]!=bidule[i+1])
                step++;
        
        printf("%d\n", step);
    }
    
    return 0;
}

