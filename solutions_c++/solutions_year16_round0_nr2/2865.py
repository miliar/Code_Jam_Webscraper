#include <stdio.h>
#include <string.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("large_output.txt","w",stdout);

    int cases;
    scanf("%d",&cases);
    for(int T = 1; T <= cases; T++)
    {
        char str[110];
        scanf("%s",str);

        int pos = 0,neg = 0;
        bool lastPos = str[0] == '-';

        for(int i = 0; i < strlen(str); i++)
        {
            if( lastPos && str[i] == '-' )
            {
                neg++;
                lastPos = false;
            }
            else if( !lastPos && str[i] == '+' )
            {
                pos++;
                lastPos = true;
            }
        }

        printf("Case #%d: %d\n",T,pos+neg-lastPos);
    }
}

