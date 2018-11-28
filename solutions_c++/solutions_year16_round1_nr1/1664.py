#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(void)
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    int T, len;
    string S, last_S;

    scanf("%d", &T);
    for(int x = 1; x <= T; ++x) {
        cin >> S;
        len = S.length();
        last_S.clear();
        last_S += S[0];
        for(int i = 1; i < len; ++i) {
            if(S[i]>=last_S[0]) {
                last_S = S[i] + last_S;
            }
            else {
                last_S += S[i];
            }
        }

        printf("Case #%d: %s\n", x, last_S.c_str());
    }


    return 0;
}
