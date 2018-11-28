#include <cstdio>


using namespace std;

char str[105], strsize;
int arr[105];

void readinput()
{
    char c;
    strsize = 0;
    c = getchar();
    while(c != '-' && c != '+')
        c = getchar();
    while(c == '-' || c == '+')
    {
        //printf("%c\n", c);
        str[strsize++] = c;
        c = getchar();
    }
    return;
}

void transfer()
{
    for (int i = 0; i < strsize; ++i)
    {
        if(str[i] == '+')
            arr[i] = 1;
        else
            arr[i] = 0;
    }
}

int countalt()
{
    int count = 0, curr;
    int i = strsize - 1;
    while(i > -1 && arr[i] == 1)
        i--;
    if(i == -1)
        return count;
    count++;
    curr = 0;
    for (; i > -1; --i)
    {
        if(curr == arr[i]^1)
        {
            count++;
            curr = arr[i];
        }
    }
    return count;
}

int main(void)
{
    int t, res;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &t);

    for (int i = 0; i < t; ++i)
    {
        readinput();
        transfer();
        res = countalt();

        printf("Case #%d: %d\n", i+1, res);
    }

    return 0;
}