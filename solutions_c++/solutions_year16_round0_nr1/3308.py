#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
char seen[10];

int fill(int n)
{
    int nb=0;
    while(n>0)
    {
        nb+=1-seen[n%10];
        seen[n%10]=1;
        n/=10;
    }
    return nb;
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for(int i = 0; i < T; i++)
    {
        int N;
        scanf("%d", &N);
        
        printf("Case #%d: ", i+1);
        
        if(N==0)printf("INSOMNIA\n");
        else
        {
            for(int j = 0; j < 10; j++)
                seen[j]=0;
            int curseen=0;
            int nb=N;
            for(int j = 1; j < 1000; j++)
            {
                curseen+=fill(nb);
                if(curseen==10)
                {
                    break;
                }
                nb += N;
                
                /*if(j==999)
                {
                    printf("FATAL ERROR\n");
                    exit(0);
                }*/
            }
            printf("%d\n", nb);
        }
    }
    
    return 0;
}

