#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <bitset>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define pb push_back
#define mp make_pair
#define EPS 1.0e-8
#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef long double ld;

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);

    int T;
    int x, r, c;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d%d%d", &x, &r, &c);
        printf("Case #%d: ", ncase);
        if ((r*c)%x!=0 || (x>r && x>c) || (x>2*min(r,c)) || x>6) puts("RICHARD");
        else if (x==4 && min(r,c)==2 && max(r,c)==4) puts("RICHARD");
        else if (x==5 && min(r,c)==2 && max(r,c)==5) puts("RICHARD");
        else puts("GABRIEL");
    }

    return 0;
}
