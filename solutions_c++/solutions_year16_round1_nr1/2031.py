#include <bits/stdc++.h>
using namespace std;

const int N = 1e3+1;
int t, T, k[N], id[N], i, j, l;
char s[N], f;

bool cp(int i, int j) {return k[i] < k[j];}

int main() {
    scanf("%d", &T);
    while(t++ <T) {
        scanf(" %s", s);
        i = j = id[0] = 0;
        f = s[0];

        for(l=1; s[l]; ++l) {
            id[l] = l;
            if (s[l] >= f) k[l] = --i, f = s[l];
            else k[l] = ++j;

        }
        sort(id, id+l, cp);
        printf("Case #%d: ", t);
        for(int i=0; i<l; ++i) printf("%c", s[id[i]]);
        printf("\n");
    }
    return 0;
}
