//By Brickgao
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
#define LL long long
const int maxn = 1000010;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

LL ans;
int t, caseno = 1, l;
int c[maxn][2];
char s[maxn];

int main() {
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    scanf("%d", &t);
    while(t --) {
        memset(c, 0, sizeof(c));
        scanf("%s", s);
        scanf("%d", &l);
        int len = strlen(s);
        ans = 0;
        for(int i = 0; i < len; i ++) {
            for(int j = i; j < len; j ++) {
                int tmp = 0;
                int maxtmp = -1;
                for(int k = i; k <= j; k ++) {
                    if(s[k] == 'a' || s[k] == 'e' || s[k] == 'i' || s[k] == 'o' || s[k] == 'u') {
                        tmp = 0;
                    }
                    else {
                        tmp ++;
                        maxtmp = max(maxtmp, tmp);
                    }
                }
                if(maxtmp >= l) {
                    ans ++;
                }
            } 
        }
        printf("Case #%d: %I64d\n", caseno ++, ans);
    }
    return 0;
}

