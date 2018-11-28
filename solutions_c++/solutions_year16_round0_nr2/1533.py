#include <cstdio>
#include <cstdlib>
#include <string.h>

using namespace std;

bool pancake[105];
char str[105];
int len;

int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%s", str);

        len = strlen(str);

        for(int i = 0; i < len; i++)
        {
            if(str[i] == '+')
                pancake[i] = true;
            else
                pancake[i] = false;
        }

        int flip_count = 0;

        for(int i = len - 1; i >=0; i--)
        {
            if((pancake[i] && (flip_count&1) == 0 ) 
                || (!pancake[i] && (flip_count&1) == 1))
                continue;

            flip_count++;
        }

        printf("Case #%d: %d\n", t, flip_count);


    }
}