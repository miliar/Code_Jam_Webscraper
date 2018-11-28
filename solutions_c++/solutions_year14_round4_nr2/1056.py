#include <cstdio>
#include <algorithm>
#include <cstdlib>

const int MAXN = 1024;

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for(int lp=1;lp<=t;++lp)
    {
        int n;
        int list[MAXN];
        scanf("%d", &n);
        for(int i=0;i<n;++i)
        {
            scanf("%d", &list[i]);            
        }
        
        int ret = 0;
        auto first = &list[0];
        auto last = &list[n];
        while(first < last)
        {
            auto it = min_element(first, last);
            if(it - first < last - it - 1)
            {
                ret += it - first;
                rotate(first, it, it+1);
                ++first;
            }
            else
            {
                ret += last - it - 1;
                rotate(it, it+1, last);
                --last;
            }
        }
        
        printf("Case #%d: %d\n", lp, ret);
        
    }
    
    return 0;
}