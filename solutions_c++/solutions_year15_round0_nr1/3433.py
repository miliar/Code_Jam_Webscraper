#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(void)
{
    //freopen("A-large.in", "r", stdin);

    //FILE *output = fopen("A-large.out", "w");
    int T, Smax, x=1, y, t, i;
    char S[1005];

    scanf("%d", &T);

    while(T--) {
        scanf("%d%s", &Smax, S);
        for(i=0, y=0, t=0; i<=Smax; ++i) {
            t += S[i]-'0';
            if(t<=i) { ++y; ++t; }
        }

        //fprintf(output, "Case #%d: %d\n", x, y);
        printf("Case #%d: %d\n", x++, y);
    }


    return 0;
}
