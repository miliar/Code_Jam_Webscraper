#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

void simplify(char str[]);
//void strrev(char str[]);
int cal(char str[]);
int main()
{
    int T, cnt;
    scanf("%d", &T);
    cnt = 1;

    while(cnt <= T)
    {
        char str[500] = {0};
        scanf("%s", str);
        simplify(str);
        strrev(str);
        int result = cal(str);
        printf("Case #%d: %d\n", cnt, result);
        cnt++;
    }
    return 0;
}

void simplify(char str[])
{
    char tmp[500]={0};
    int len = strlen(str);
    tmp[0] = str[0];
    for(int i=1, j=1; i<len; i++)
    {
        if(str[i]!=str[i-1])
        {
            tmp[j] = str[i];
            j++;
        }
    }
    memset(str, 0, 500);
    strcpy(str, tmp);
}
/*
void strrev(char str[])
{
    char tmp[500] = {0};
    int len = strlen(str);
    strcpy(tmp, str);
    for(int i=0; i<len; i++)
    {
        str[i] = tmp[len-i-1];
    }
}
*/
int cal(char str[])
{
    int len = strlen(str);
    int cnt = 0;
    for(int i=0; i<len;)
    {
        if(i==0 && str[i] == '+')
        {
            i++;
        }
        else
        {
            if(i+1 < len)
            {
                cnt = cnt + 2;
                i = i + 2;
            }
            else
            {
                cnt = cnt + 1;
                i++;
            }
        }
    }
    return cnt;
}
