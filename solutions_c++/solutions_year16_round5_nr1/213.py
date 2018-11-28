#include <iostream>
#include <cstring>
#include <cstdio>
#include <stack>

using namespace std;

char s[20001]; int sn;

int main()
{
    freopen("A_big_in.txt", "r", stdin);
    freopen("A_big_out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%s", s);
        sn = strlen(s);

        stack<char> stk;
        int cnt = 0;

        for(int si = 0; si < sn; si++)
            if( stk.empty() || stk.top() != s[si] ) stk.push(s[si] );
            else stk.pop(), cnt++;

        printf("Case #%d: %d\n", Ti, cnt*10+stk.size()/2*5);
    }
}
