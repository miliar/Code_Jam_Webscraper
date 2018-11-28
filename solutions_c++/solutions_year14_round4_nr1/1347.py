#include "cstdio"
#include "cstring"
#include "algorithm"
#include "set"
#include "vector"
#include "cmath"

using namespace std;

int main(void)
{
    int t;
    scanf("%d",&t);
    for(int test = 1;test<=t;test++)
    {
        int ans = 0;
        int n,x;
        bool ok[12000];
        
        vector<int> disc;
        
        scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++)
        {
            int buff;
            scanf("%d",&buff);
            disc.push_back(buff);
            ok[i] = false;
        }
        
        sort(disc.begin(), disc.end());
        int pointer = n-1;
        
        for(int i=0;i<n;i++)
        {
            if(ok[i])
                continue;
            
            ok[i] = true;
            
            while(pointer >= 0)
            {
                if(ok[pointer])
                {
                    pointer--;
                    continue;
                }
                else if(disc[pointer] + disc[i] > x)
                {
                    pointer--;
                    continue;
                }
                else
                {
                    ok[pointer] = true;
                    pointer--;
                    break;
                }
            }
            
            ans++;
        }
        
        printf("Case #%d: %d\n",test,ans);
    }
    return 0;
}
