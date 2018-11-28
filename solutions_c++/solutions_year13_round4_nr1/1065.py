#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

i64 mod = 1000002013, res = 0, tot = 0;
struct str{
    int o, e;
    bool operator() (struct str a, struct str b){
        if (a.o == b.o) {
            return a.e < b.e;
        }
        return a.o < b.o;
    }
}myo;
vector< struct str > vs;
int N, M;
void cal(int o, int e){
    int k = 0, t = 0;
    for (int i = o; i < e; i++) {
        t += N - k;
        k++;
    }
    res += t;
}
void main2()
{
    vs.clear();
    scanf("%d%d", &N, &M);
    res = 0;
    for (int i = 0; i < M; i++) {
        int o, e, p;
        scanf("%d%d%d", &o, &e, &p);
        for (int j = 0; j < p; j++) {
            struct str temp = {o, e};
            vs.push_back(temp);
        }
    }
    sort(vs.begin(), vs.end(), myo);
    for (int i = 0; i < vs.size(); i++) {
        cal(vs[i].o, vs[i].e);
    }
    tot = res;
    res = 0;
    for (int i = 0; i < vs.size(); i++) {
        for (int j = i + 1; j < vs.size(); j++) {
            if (vs[i].e >= vs[j].o && vs[j].e >= vs[i].e) {
                int t = vs[j].e;
                vs[j].e = vs[i].e;
                vs[i].e = t;
            }
        }
        cal(vs[i].o, vs[i].e);
    }
    printf("%lld\n", tot - res);
}
int main()
{
    int T;
    scanf("%d", &T);
    int casenum = 1;
    while (T--) {
        printf("Case #%d: ", casenum++);
        main2();
    }
    return 0;
}
