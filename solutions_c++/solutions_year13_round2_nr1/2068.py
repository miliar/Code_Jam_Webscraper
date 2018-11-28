#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <utility>
#define EPSI 1e-9

using namespace std;

typedef long long ll;
int a[1000010];
bool check(int A, int id, int k) {
    for(int i = id; i < k; i++) {
        if(A <= a[id]) return false;
    }
    return true;
}
int solve(int A, int id, int k) {
    for(; id < k; id++) {
        if(A > a[id]) A += a[id];
        else break;
    }
    if(k < id) return 0;
    if(check(A,id,k)) return 0;
    if(A == 1) return k-id;
    int ans = min(solve(A+A-1,id,k),solve(A,id,k-1));
    return ans + 1;
}
int main() {
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small.out","w",stdout);
    int t, A, n;
    scanf("%d", &t);
    for(int TEST = 1; TEST <= t; TEST++) {
        int id = -1;
        scanf("%d%d", &A, &n);
        for(int i = 0; i < n; i++) scanf("%d", &a[i]);
        sort(&a[0],&a[n]);
        for(int i = 0; i < n; i++) {
            if(a[i] < A) A += a[i];
            else {
                id = i;
                break;
            }
        }
        if(id == -1) printf("Case #%d: 0\n", TEST);
        else printf("Case #%d: %d\n", TEST, solve(A,id,n));
    }
    //system("pause");
    return 0;
}
