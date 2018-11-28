#include <iostream>
#include <cstdio>

using namespace std;

int N, R, P, S;

char ch(int x)
{
    if( x == 0 ) return 'P';
    else if( x == 1 ) return 'R';
    else return 'S';
}

string sol(int x, int N)
{
    string s = "", r = "";

    if( N == 0 )
    {
        s += ch(x);
        return s;
    }

    s = sol(x, N-1);
    r = sol((x+1)%3, N-1);

    return min(s+r, r+s);
}

int main()
{
    freopen("A_big.in", "r", stdin);
    freopen("A_out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d %d %d %d", &N, &R, &P, &S);

        printf("Case #%d: ", Ti);

        for(int i = 0; i < 3; i++)
        {
            string s = sol(i, N);
            int _R = 0, _P = 0, _S = 0;

            for(int si = 0; si < s.size(); si++)
            {
                if( s[si] == 'R' ) _R++;
                else if( s[si] == 'P' ) _P++;
                else _S++;
            }

            if( _R == R && _P == P && _S == S )
            {
                printf("%s\n", s.c_str());
                goto flag;
            }
        }

        puts("IMPOSSIBLE");
        flag:;
    }
}
