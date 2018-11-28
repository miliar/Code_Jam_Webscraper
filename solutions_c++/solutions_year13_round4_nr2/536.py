#include <cstdio>
#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <stack>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
#define REP(i,n) for(int64 i=0; i<(int64)n; i++)
typedef long long int64;

int64 calc(int64 n, int64 p) {
    int64 es=0, di=(1LL<<n);
    while (di>es) {
        int64 me=(es+di+1LL)/2;

        int64 i, m, pos=(1LL<<n)-1LL;
        for (i=0, m=me; i<n && m>=2; i++, m/=2) {}

        for (;i<n;i++)
            pos-=(1LL<<(n-i-1LL));

        if (pos<=p) es=me;
        else di=me-1LL;
    }
    return es-1LL;
}

int64 calc2(int64 n, int64 p) {
    int64 es=0, di=(1LL<<n);
    while (di>es) {
        int64 me=(es+di+1LL)/2;

        int64 i, m, pos=0;
        for (i=0, m=(1LL<<n)-me+1LL; i<n && m>=2; i++, m/=2) {}

        for (;i<n;i++)
            pos+=(1LL<<(n-i-1LL));

        if (pos<=p) es=me;
        else di=me-1LL;
    }
    return es-1LL;
}

int main() {
    int64 nt,n,p;

    scanf("%lld",&nt);
    REP(ct,nt) {
        scanf("%lld %lld",&n,&p);
        p--;
        
        printf("Case #%lld: %lld %lld\n",ct+1LL,calc(n,p),calc2(n,p));
    }
    return 0;
}

