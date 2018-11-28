//#pragma comment(linker,"/STACK:102400000,102400000")
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <stdexcept>
#include <functional>

using namespace std;

#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define BGN begin()
#define END end()
#define SZ size()
#define SORT(p) sort(p.BGN,p.ED)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define mabs(x) (x < 0 ? -x : x)
#define sqr(x) ((x)*(x))
#define ITE ::iterator
#define INF (1<<28)
typedef long long LL;
typedef pair<int, int> PII;
typedef vector <int> VI;
typedef set < int > SI;

char str[111][111];
int cut[111][111];
char lab[111][111];
int len[111];
int duan[111];
int n;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int Test;
    scanf("%d", &Test);
    for(int Case = 1; Case <= Test; Case++) {
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%s", &str[i][0] + 1);
            str[i][0] = '#';
            len[i] = strlen(str[i]);
            duan[i] = 0;
            for(int j = 1; j < len[i]; j++) {
                if(str[i][j] != str[i][j - 1]) {
                    duan[i]++;
                    lab[i][duan[i]] = str[i][j];
                    cut[i][duan[i]] = 1;
                }
                else {
                    cut[i][duan[i]]++;
                }
            }
        }
        int flag = 0;
        for(int i = 1; i < n; i++) {
            if(duan[i] != duan[i - 1]) {
                flag = 1;
                break;
            }
            for(int j = 1; j <= duan[i]; j++) {
                if(lab[i][j] != lab[i-1][j]) {
                    flag = 1;
                    break;
                }
            }
        }
        printf("Case #%d: ", Case);
        if(!flag) {
            int ans = 0;
            for(int i = 1; i <= duan[0]; i++) {
                int dmin = INF;
                for(int l = 1; l <= 100; l++) {
                    int temp = 0;
                    for(int k = 0; k < n; k++) {
                        temp += abs(l - cut[k][i]);
                    }
                    dmin = min(dmin, temp);
                }
                ans += dmin;
            }
            printf("%d\n", ans);
        }
        else {
            printf("Fegla Won\n");
        }
    }
    return 0;
}
