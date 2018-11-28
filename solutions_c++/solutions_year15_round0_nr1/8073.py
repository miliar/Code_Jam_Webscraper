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

bool comp(int a,int b) {
     return (a>b);
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int n, t, ans, jumlah;
    char s[1005];
    scanf("%d",&t);
    rep (i,1,t) {
        ans=jumlah=0;
        scanf("%d %s",&n,&s);
        rep (j,0,n) {
            if (s[j]!=0) {
               if (jumlah<j) ans+=j-jumlah, jumlah=j;
               jumlah+=s[j]-'0';
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
