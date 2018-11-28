#include <bits/stdc++.h>
using namespace std;

const int MAX = 200;
int test, n, pos, res;
char s[MAX];

int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int ii = 1; ii <= test; ++ii){
        scanf("%s", s + 1);
        n = strlen(s + 1);
        res = 0;
        while (1){
            pos = 0;
            for (int i = n; i >= 1; --i)
            if (s[i] == '-'){
                pos = i;
                break;
            }
            if (pos == 0)
                break;

            if (s[1] == '+'){
                ++res;
                for (int i = 1; s[i] == '+'; ++i)
                    s[i] = '-';
            }

            ++res;
            reverse(s + 1, s + 1 + pos);
            for (int i = 1; i <= pos; ++i)
                s[i] = (s[i] == '-' ? '+' : '-');
        }

        printf("Case #%d: %d\n", ii, res);
    }
    return 0;
}


