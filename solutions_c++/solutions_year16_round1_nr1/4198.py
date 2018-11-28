#include <cstdio>
#include <queue>

using namespace std;

char s[5010];

int main(int argc, char* argv[])
{
    int t;
    scanf("%d", &t);
    for (int T = 1; T <= t; ++T)
    {
        deque<char> dque;
        scanf("%s", s);
        dque.push_back(s[0]);
        for (int i = 1; s[i] != '\0'; ++i)
        {
            if (s[i] >= dque.front())
                dque.push_front(s[i]);
            else
                dque.push_back(s[i]);
        }
        printf("Case #%d: ", T);
        while (!dque.empty())
        {
            putchar(dque.front());
            dque.pop_front();
        }
        putchar('\n');
    }
    return 0;
}
