#include <cstdio>
#include <cstring>

#define MAXN 1000

int audience[MAXN+1];
char line[MAXN+1];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int T; scanf("%d", &T);
    
    for(int caso = 1; caso <= T; caso++)
    {
        int S; scanf("%d", &S);
        scanf(" %s", line);
         
        for(int i = 0; i <= S; i++)
            audience[i] = line[i] - '0';
            
        
        int standup = 0;
        int sol = 0;
        
        for(int i = 0; i < S; i++)
        {
            standup += audience[i];
            
            while(i + 1 > standup) { sol++; standup++; }
        }
        
        printf("Case #%d: %d\n", caso, sol);
    }
    
    return 0;
}
