#include <cstdio>
#include <cmath>
#include <map>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>
using namespace std;
const int M = 1000005;
struct node{
    int val;
    int step;
}Q[M];
map<int, int>mp;
int head = 0, tail = 0, st = 0, ed = 0;
int all = 0;
int revert(int val, int i, int j) {
    int t1 = val&(1<<i);
    int t2 = val&(1<<j);
    if (t1 == 0 && t2 == 0) {
        return val;
    } else if(t1 != 0 && t2 != 0) {
        return val;
    } else {
        return val ^ (1<<i) ^ (1<<j);
    }
}

char s[105];
int main(void) {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("a1.out","w",stdout);
    int n;
    scanf("%d", &n);gets(s);
    for (int cas = 0; cas < n; ++cas) {
        head = tail = st = ed = 0;
        mp.clear();
        gets(s);//puts(s);
        int len = strlen(s);
        for (int i = 0; i < len; ++i) {
            ed += (1<<i);
            if (s[i] == '+') {
                st += (1<<i);
            }
        }
        //printf("st=%d, ed=%d\n", st, ed);
        struct node t;
        t.val = st;
        t.step = 0;
        mp[st] = 1;
        Q[head++] = t;
        int res = 0;
        while (head != tail) {
            struct node now = Q[tail++];
            tail%=M;
            if (now.val == ed) {
                res = now.step;
                break;
            }
            for (int cc = 0; cc < len; cc++) {
                int v = now.val;
                for (int i = 0; i <= cc; i++) {
                    v ^= (1<<i);
                }
                for (int i = 0, j = cc; i < j; i++, j--) {
                    v = revert(v, i, j);
                }
                if (mp[v] == 1) continue;
                mp[v] = 1;
                struct node tt;
                tt.val = v;
                tt.step = now.step + 1;
                //printf("now.val = %d, cc = %d, %d %d\n", now.val, cc, tt.val, tt.step);
                if (tt.val == ed) {
                    res = tt.step;
                    break;
                }
                Q[head++] = tt;
                head %= M;
            }
            if (res != 0) break;
        }
        printf("Case #%d: %d\n", cas+1, res);
    }
}
