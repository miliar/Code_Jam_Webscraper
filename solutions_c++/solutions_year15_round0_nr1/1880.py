#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

#pragma comment(linker, "/STACK:1024000000,1024000000")

#define     IT              iterator
#define     PB(x)           push_back(x)
#define     CLR(a,b)        memset(a,b,sizeof(a))

using namespace std;

typedef     long long               ll;
typedef     unsigned long long      ull;
typedef     vector<int>             vint;
typedef     vector<ll>              vll;
typedef     vector<ull>             vull;
typedef     set<int>                sint;
typedef     set<ull>                sull;

const int maxn = 1000 + 5;
char s[maxn];

int main() {
    //freopen("A-large.in","r",stdin);
    //freopen("ans.out","w",stdout);
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        int n;
        scanf("%d%s",&n,s);
        int tmp = s[0] - '0';
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (i <= tmp) tmp += s[i] - '0';
            else {
                ans += i - tmp;
                tmp = i + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
