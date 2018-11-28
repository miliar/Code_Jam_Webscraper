#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int T;
    int S;
    char Si;
    scanf("%d\n",&T);
    for (int t=1;t<=T;t++) {
        int total = 0;
        int invitados = 0;
        scanf("%d%c", &S, &Si);
        for (int i=0; i<=S; i++) {
            scanf("%c", &Si);
            Si -= '0';
            if (total < i) {
                invitados += i - total;
                total = i;
            }
            total += Si;
        }
        scanf("%c", &Si);
        printf("Case #%d: %d\n", t, invitados);
    }
    return 0;
}
