#include <cstdio>
#include <algorithm>
using namespace std;

int N, R, P, S;
char str[5000];

int lR, lP, lS;
void ok(int l, int r, char win) {
    if( l==r ) {
        str[l] = win;
        if( win=='P' ) --lP;
        else if( win=='R' ) --lR;
        else --lS;
        return;
    }
    int mid = (l+r)/2;
    char lose;
    if( win=='R' ) lose = 'S';
    else if( win=='P' ) lose = 'R';
    else lose = 'P';
    if( lose < win ) {
        ok(l, mid, lose);
        ok(mid+1, r, win);
    }
    else {
        ok(l, mid, win);
        ok(mid+1, r, lose);   
    }
}
bool ok(char win) {
    lR = R;
    lP = P;
    lS = S;
    ok(0, (1<<N)-1, win);
    return lR==0 && lP==0 && lS==0;
}

int cmp(char *str1, char *str2, int n) {
    for(int i=0; i<n; ++i)
        if( str1[i]!=str2[i] )
            return (str1[i]<str2[i])? -1 : 1;
    return 0;
}
void mergeSort(int l, int r) {
    if( l==r ) return;
    int mid = (l+r)/2;
    int len = mid-l+1;
    mergeSort(l, mid);
    mergeSort(mid+1, r);
    bool needSwap = false;
    if( cmp(str+l, str+mid+1, len)>0 ) {
        for(int i=0; i<len; ++i)
            swap(str[l+i], str[mid+1+i]);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for(int NOWCASE=1; NOWCASE<=T; ++NOWCASE) {
        scanf("%d%d%d%d", &N, &R, &P, &S);
        bool possible = ok('P') || ok('R') || ok('S');
        printf("Case #%d: ", NOWCASE);
        if( !possible )
            puts("IMPOSSIBLE");
        else {
            mergeSort(0, (1<<N)-1);
            str[1<<N] = '\0';
            puts(str);
        }
    }
    return 0;
}
