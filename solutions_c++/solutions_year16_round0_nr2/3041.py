#include <cstdio>
#include <cstring>

using namespace std;

char str[101] = {0};

int main(int argc, char *argv[])
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%s", str);
        int l = strlen(str);
        int g = 1;
        for (int i = 1; i < l; i++)
            if (str[i] != str[i - 1])
                g++;
        int answ = g - 1;
        answ += ((g - 1) % 2) ^ (str[0] == '-');
        printf("Case #%d: %d\n", i + 1, answ);
    }
    return 0;
}
