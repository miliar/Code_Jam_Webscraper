#include <algorithm>
#include <cstdio>

int main(int argc, char** argv)
{
    int T = 0;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        int Smax = 0;
        scanf("%d ", &Smax);
        
        int amount_up = 0;
        int total_amount_to_invite = 0;
        
        for(int i = 0; i < Smax + 1; ++i)
        {
            char digit;
            scanf("%c", &digit);
            int idigit = digit - '0';
            
            if(amount_up >= i)
            {
                amount_up += idigit;
            }
            else
            {
                int amount_to_invite = (i - amount_up);
                total_amount_to_invite += amount_to_invite;
                amount_up += amount_to_invite + idigit;
            }
        }
        scanf(" ");
        printf("Case #%d: %d\n", t, total_amount_to_invite);
    }
}