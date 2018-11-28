#include<cstdio>
#include<cstring>
using namespace std;

char str[101];
int len;

bool isHappy()
{
    len = strlen(str);
    for(int i=0; i<len; i++)
    {
        if(str[i] == '-')
            return false;
    }
    return true;
}

void mane()
{
    char str2[len];
    int i, j;
    str2[0] = str[0];
    for(i=1, j=1; i<len; i++, j++)
    {
        if(str[i] == str[i-1])
            str2[j] = str[i];
        else
        {
            i++; j++;
            break;
        }
    }
    if(str2[0] == '+')
    {
        for(int k=0; k<j; k++)
            str[k] = '-';
    }
    else
    {
        for(int k=0; k<j; k++)
            str[k] = '+';
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t, c=0;

    scanf("%d", &t);
    getchar();
    while(t--)
    {
        gets(str);
        if(isHappy())
            printf("Case #%d: 0\n", ++c);
        else
        {
            for(int i=1; ; i++)
            {
                mane();
                if(isHappy())
                {
                    printf("Case #%d: %d\n", ++c, i);
                    break;
                }
            }
        }
    }

    return 0;
}
