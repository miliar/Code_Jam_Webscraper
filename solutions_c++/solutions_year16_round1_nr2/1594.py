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
#define Set(data,value) memset(data,value,sizeof(data));

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

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    //std::ios::sync_with_stdio(false);
    int T,n,x;
    int ans[2505];
    scanf("%d",&T);
    rep (t,1,T) {
        scanf("%d",&n);
        Set(ans,0);
        rep (i,1,n*2-1) {
            rep (j,1,n) {
                scanf("%d",&x);
                ans[x]++;
            }
        }
        printf("Case #%d:", t);
        rep (i,1,2500) {
            if (ans[i]%2!=0) printf(" %d", i);
        }
        printf("\n");
    }
    return 0;
}
