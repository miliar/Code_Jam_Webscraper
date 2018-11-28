#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

char s[N];
bool solve()
{
    scanf("%s", s);
    int length = strlen(s);
    int ans = 0;
    for (int i = length - 1; i >= 0; --i) {
        if (s[i] == '+')
            continue;
        int j = 0;
        while (s[j] == '+') j++;
        if (s[0]=='+') {
            reverse(s, s + j);
            for_each(s, s + j, [](char &c){ c = (c=='-' ? '+' : '-'); });
            ans++;
        }
        reverse(s, s + i + 1);
        for_each(s, s + i + 1, [](char &c){ c = (c=='-' ? '+' : '-'); });
        ans++;
    }
    printf("%d\n", ans);
    return false;
}

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
