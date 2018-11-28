#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main ()
{
    
    int i, j, cont, t, max, caso=1, ok=0, tot;
    char sh[1005], c;

    scanf ("%d", &t);
    while (t--) {
        tot=cont=ok=0;
        scanf ("%d", &max);
        scanf (" %s", sh);
        cont+=(sh[0]-48);
        for (i=1; i<=max; i++) {
            if (i<=cont && sh[i]!='0') cont+=(sh[i]-48);
            else if (i>cont && sh[i]!='0'){
                ok+=(i-cont);
                cont+=(sh[i]-48);
                cont+=ok;
            }
        }
        printf ("Case #%d: %d\n", caso++, ok);
    }

    return 0;
}