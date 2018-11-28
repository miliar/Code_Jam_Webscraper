#include <stdio.h>
#include <string.h>

int check(char *str);
int judge(char *str);
int flip(char *str);
void flip_once(char *str, int idx);

int main(void)
{
    int TC, TC_i=1;
    char str[100];

    scanf("%d", &TC);
    while (TC_i <= TC)
    {
        str[0]='\0';
        scanf("%s", str);
        if(!check(str))
        {
            printf("input format is invalid\n");
            return 0;
        }
        //printf("%s, %ld\n", str, strlen(str));

        printf("Case #%d: %d\n", TC_i, flip(str));
        TC_i++;
    }

    return 0;
}

int check(char *str)
{
    int i;
    for (i=0; i<strlen(str); i++)
        if (!(str[i] == '-' || str[i] == '+'))
            return 0;
    return 1;
}

int judge(char *str)
{
    int i;
    for (i=0; i<strlen(str); i++)
        if (str[i] == '-')
            return 0;
    return 1;
}

int flip(char *str)
{
    int cnt=0;

    int end = strlen(str);
    while(!judge(str))
    {
        if(str[end-1] == '-')
        {
            flip_once(str, end-1);
            cnt++;
        }
        end--;
//        printf("%s\n", str);
    }
    return cnt;
}

void flip_once(char *str, int idx)
{
    if (idx > strlen(str))
    {
        printf("idx must be under strlen(str)\n");
        return;
    }

    int i;
    for (i=0; i<=idx; i++)
    {
        if (str[i] == '-')
            str[i] = '+';
        else if (str[i] == '+')
            str[i] = '-';
    }
}
