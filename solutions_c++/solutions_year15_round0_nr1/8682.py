#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>
#include <bitset>

#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef pair<ii, ii> iiii;
typedef pair<double, int> di;
typedef vector<int> vi;
typedef vector<di> vdi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;

char s[1010];

int main() {
    freopen("A-small.in","r",stdin);
    freopen("A-small.out", "w", stdout);

    int t, n, total, cnt, cur, kase=1;
    scanf("%d", &t);

    while(t--){
        scanf("%d %s", &n, s);

        cnt=0;
        total = s[0]-'0';
        n++;
        for(int i=1; i<n; i++){
            cur = s[i]-'0';
            if(cur>0 && i>total){
                cnt += i-total;
                total += i-total;
            }
            total += cur;
        }

        printf("Case #%d: %d\n", kase++, cnt);
    }
    return 0;

}
