#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

const int MAXN = 1001, INF = 1002;
char cake[MAXN];
int N, K;

void flip(int i) {
    for (int j = i; j < i+K; ++j) {
        cake[j] = (cake[j]=='+'?'-':'+');
    }
}

int calc() {
    int ret = 0;
    for (int i = 0; i < N; ++i) {
        if (cake[i]=='-') {
            if (i+K > N) {
                return INF;
            }
            flip(i);
            ++ret;
        }
    }
    return ret;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T = INPT_INT;
    for (int _case = 1; _case <= T; ++_case) {
        scanf("%s %d",cake,&K);
        N = strlen(cake);

        int res = calc();
        printf("Case #%d: ",_case);
        if (res==INF) {
            puts("IMPOSSIBLE");
        }
        else {
            printf("%d\n",res);
        }
    }
    return 0;
}
