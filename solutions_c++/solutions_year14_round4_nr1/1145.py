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
#define REP(i,n) for(int i=0; i<n; i++)
typedef long long int64;

#define N 100100
int s[N];

int main() {
    int nt;

    scanf("%d",&nt);
    REP(ct,nt) {
        int n,t;
        scanf("%d%d",&n,&t);
        REP(i,n)
            scanf("%d",&s[i]);

        sort(s,s+n);

        int qp=0;
        for (int i=0, j=n-1; i<j; ) {
            if (s[i]+s[j]<=t) {
                qp++;
                i++; j--;
            }
            else j--;
        }

        printf("Case #%d: %d\n",ct+1,n-qp);
    }
    return 0;
}
