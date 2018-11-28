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

int main()
{
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("D-small-attempt0.out","w",stdout);
    //std::ios::sync_with_stdio(false);
    int T,k,c,s;
    scanf("%d",&T);
    rep (i,1,T) {
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:", i);
        rep (j,1,s) printf(" %d", j);
        printf("\n");
    }
    return 0;
}

