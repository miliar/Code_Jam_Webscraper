#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;
using ll = long long;
using ii = pair<ll, ll>;

#define MAX 1010

char S[MAX];

void precomp()
{
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; ++test)
    {
        scanf("%s", S);
        list<char> L;

        L.push_back(S[0]);

        for (auto p = &S[1]; *p; ++p)
        {
            if (*p >= L.front())
                L.push_front(*p);
            else
                L.push_back(*p);
        }

        printf("Case #%d: ", test);

        for (auto c : L)
            printf("%c", c);

        printf("\n");
    }

    precomp();

    return 0;
}
