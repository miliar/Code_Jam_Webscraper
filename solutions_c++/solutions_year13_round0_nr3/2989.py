#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

typedef unsigned long long LL;

LL dv[500000];
int top;

bool isPalindrome(LL x) {
    char s[100];
    sprintf(s, "%llu", x);
    for (int i=0, j=strlen(s)-1; i<j; ++i, --j)
        if (s[i] != s[j])
            return false;
    return true;
}

void init() {
    int limit=1300;
    top = 0;
    
    char s1[100], s2[100];
    for (int i=1; i<limit; ++i) {
        sprintf(s1, "%d", i);
        int len = strlen(s1);
        strcpy(s2, s1);
        
        s1[len*2] = 0;
        for (int i=len-1,j=len; i>=0; --i, ++j)
            s1[j] = s1[i];
        
        s2[len*2-1] = 0;
        for (int i=len-2,j=len; i>=0; --i, ++j)
            s2[j] = s2[i];
        
        // printf("%s\n%s\n", s1, s2);
        int d1, d2;
        sscanf(s1, "%d", &d1);
        sscanf(s2, "%d", &d2);

        LL dd1, dd2;
        dd1 = d1 * (LL) d1;
        dd2 = d2 * (LL) d2;

        if (isPalindrome(dd1))
            dv[top++] = dd1;
        if (isPalindrome(dd2))
            dv[top++] = dd2;
    }

    sort(dv, dv+top);

    // cout << top << endl;
    // for (int i=0; i<top; ++i)
    //     printf("%llu\n", dv[i]);
}

int Count(LL n) {
    for (int i=0; i<top; ++i)
        if (dv[i] > n)
            return i;
}

int main () {
    // freopen("out.txt", "w", stdout);
    
    init();
    int t;
    scanf("%d", &t);
    for (int cs=1; cs<=t; ++cs) {
        LL A, B;
        scanf("%llu%llu", &A, &B);
        printf("Case #%d: ", cs);
        printf("%d\n", Count(B) - Count(A-1));
    }
    return 0;
}
