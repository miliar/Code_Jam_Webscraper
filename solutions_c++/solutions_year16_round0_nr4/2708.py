#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t<=T; t++)
    {
        int K,C,S;
        scanf("%d%d%d",&K,&C,&S);
        
        printf("Case #%d:", t);
        
        long long kc = 1;
        
        for(int i = 1; i < C; i++)
            kc *= K;
         
        //printf("debug : %lld\n", kc);
        
        for(int i = 0; i < S; i++) //small, K=S
        {
            printf(" %lld", kc*i+1ll);
        }
        
        printf("\n");
    }
    
    return 0;
}

