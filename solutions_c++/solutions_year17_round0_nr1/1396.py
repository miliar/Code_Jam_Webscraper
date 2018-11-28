#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()

#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;

int mod1 = int(1e9) + 7;

int main(){

    int t;
    ri(t);

    char s[1010];

    for(int cas=1; cas<=t; cas++) {

        memset(s,0,sizeof(s));
        scanf("%s", s);

        int k;
        ri(k);

        int len = strlen(s);

        int ans = 0;
        for(int i=0; i<len; i++) {
            if(s[i]=='-') {
                if(i+k-1>=len) {
                    ans = -1;
                    break;
                }
                ans++;
                for(int j=i; j<i+k; j++) {
                    s[j] = s[j]=='-' ? '+' : '-';
                }
            }
        }

        printf("Case #%d: ", cas);
        if(ans==-1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }

    return 0;
}
