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

const int maxp = 1000 + 5;
int p[maxp];
int d;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        CLR(p,0);
        cin>>d;
        for (int i = 0; i < d; i++) {
            scanf("%d",&p[i]);
        }
        int ans = 1000;
        for (int i = 1000; i >= 1; i--) {
            int tmpans = 0;
            for (int j = 0; j < d; j++) {
                if (p[j] > i) tmpans += (p[j] - 1) / i;
            }
            tmpans += i;
            ans = min(ans,tmpans);
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
