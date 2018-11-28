#include<cstdio>
#include<list>
#include<cstring>
using namespace std;

int main()
{
    list<char> ans;
    char str[1005];
    int Case;
    scanf("%d", &Case);
    getchar();
    for (int c = 1; c <= Case; c++)
    {
        ans.clear();
        gets(str);
        int len = strlen(str);
        ans.push_back(str[0]);
        for (int i = 1; i<len; i++)
        {
            if (str[i]>=ans.front())
                ans.push_front(str[i]);
            else
                ans.push_back(str[i]);
        }

        printf("Case #%d: ", c);
        for (char ch : ans)
            putchar(ch);
        putchar('\n');
    }

    return 0;
}