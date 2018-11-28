#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for (int i = a; i < b; i++)
#define fre(i,a,b) for (int i = a; i <= b; i++)
#define cle(a,b) memset (a, b, sizeof(a))
#define pb push_back
#define fst first
#define snd second

bool V[10];

int main () {
    int T;
    scanf ("%d", &T);
    fre(i,1,T) {
        cle(V,0);
        int N, cont = 10, j = 0, res;
        scanf ("%d", &N);
        while (cont && N) {
            j++;
            res = N*j;
            while (res > 0) {
                int r = res%10;
                res = (res-res%10)/10;
                if (!V[r]) {V[r] = 1; cont--;}
            }
        }
        if (!N) printf ("Case #%d: INSOMNIA\n", i);
        else {
            printf ("Case #%d: %d\n", i, N*j);
        }
    }
    return 0;
}
