#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)
#define debug false

using namespace std;

int isqrt(int x) {
    int y = (int)(round(sqrt(x)));
    if (y*y == x) return y;
    return -1;
}

bool palindrome(int x) {
    char s1[100];
    sprintf(s1,"%d",x);
    int n = strlen(s1);
    int i=0,j=n-1;
    while (i<j) {
        if (s1[i]!=s1[j]) return false;
        i++;j--;
    }
    return true;
}

bool isCool(int x) {
    if (!palindrome(x)) return false;
    int y = isqrt(x);
    if (y==-1) return false;
    return palindrome(y);
}

int ncools[1005];

int main() {
    ncools[0]=0;
    int ac=0,tc;
    repf(i,1,1000) {
        ac += (isCool(i)) ? 1 : 0;
        if (debug) printf("%d %d\n",i,ac);
        ncools[i] = ac;
    }
    cin >> tc;
    rep(i,tc) {
        int a,b;
        cin >> a >> b;
        printf("Case #%d: %d\n",i+1,ncools[b]-ncools[a-1]);
    }
}
