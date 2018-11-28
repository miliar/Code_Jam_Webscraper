#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h> 
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

const int N=1e6+100;

long long calc(long long p,long long k,int c) {
    long long o=p;
    for (int i=2;i<=c;i++) {
        p=(p-1)*k+o;
    }
    return p;
}
int main () {
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        int k,c,s;
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:",cas);
        for (int i=1;i<=k;i++) {
            long long now=calc(i,k,c);
            printf(" %lld",now);
        }
        puts("");
    }
    return 0;
}
