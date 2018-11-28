#include <cstdio>
#include <algorithm>

const int MAXN = 20000;
int files[MAXN];

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for(int lp=1;lp<=t;++lp)
    {
        int n, c;
        scanf("%d %d", &n, &c);
        for(int i=0;i<n;++i)
        {
            scanf("%d", &files[i]);
        }
        
        sort(&files[0], &files[n]);
        int ret = 0;
        auto first = &files[0];
        auto last = &files[n-1];
        while(first <= last)
        {
            ++ret;
            int space = c;
            space -= *last;
            last--;
            if(first <= last)
            {
                if(space >= *first)
                {
                    ++first;
                }
            }
        }
        
        printf("Case #%d: %d\n", lp, ret);
        
    }
    
    return 0;
}