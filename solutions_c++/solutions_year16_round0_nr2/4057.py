#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>

using namespace std;

#define gettime printf("\nTime : %0.3lf\n",clock()*1.0/CLOCKS_PER_SEC);
#define PB push_back
#define MP make_pair
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define repp(i,a,b) for(int i=a;i>=b;i--)
#define Set(x,a) memset(x,a,sizeof(x));

#define vs vector<string>
#define vi vector<int>
#define ll long long
#define ff first
#define ss second

struct comp {
       bool operator() (int a,int b) {
            return a>b;
       }
};

char data[105];

void SetData(int a, int b, char x) {
    rep (i,a,b) data[i] = x;
}

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    //std::ios::sync_with_stdio(false);
    int T,n,ans;
    scanf("%d",&T);
    rep (i,1,T) {
        scanf("%s",&data);
        n = strlen(data);
        ans = 0;
        rep (i,1,n-1) {
            if (data[i-1] != data[i]) {
                SetData(0, i-1, data[i]);
                ans++;
            }
        }
        if (data[0] == '-') ans++;
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
