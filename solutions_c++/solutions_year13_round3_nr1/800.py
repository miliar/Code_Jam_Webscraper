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
#define dbg true

using namespace std;

char buf[1000005];
int n,m;
//int iimg[1000005];
int indices[1000005];
int L;

typedef long long int LL;

const char* vow = "aeiou";

bool isvow(char c) {
    rep(i,5) if(vow[i]==c) return true;
    return false;
}

void cmpRun() {
    int count=0;
    rep(i,L) {
        if (isvow(buf[i])) {
            count=0;
        } else {
            count++;
        }
        if (count >= n) {
            indices[m++]=i;
        }
        //if (dbg) printf("%d ",iimg[i]);
    }
    //repf(i,1,L-1) {
    //    iimg[i] += iimg[i-1];
    //}
}

/*int bsearch(int x, int a, int b) {
    if (a==b) return a;
    int m = (a+b)/2;
    if (iimg[m] == x) {
        return bsearch(x,a,m);
    } else if (x < iimg[m]) {
        return bsearch(x,a,m-1);
    } else {
        return bsearch(x,m+1,b);
    }
}*/

LL cntSubs() {
    LL ans=0;
    if (m==0) return 0;
    //int mval = iimg[L-1];
    int mix = 0;
    int fix = indices[mix];
    int six = fix-n+1;
    rep(i,L) {
        if (six < i) {
            mix++;
            if (mix == m) break;
            fix = indices[mix];
            six = fix-n+1;
        }
        ans += L-fix;
    }
    return ans;
}

int main() {
    int tc;
    cin >> tc;
    rep(i,tc) {
        cin >> buf;
        cin >> n;
        m=0;
        L = strlen(buf);
        cmpRun();
        LL ans = cntSubs();
        printf("Case #%d: %lld\n",i+1,ans);
    }
}
