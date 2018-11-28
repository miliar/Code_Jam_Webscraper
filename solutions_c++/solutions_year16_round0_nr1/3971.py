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

int totalNumberExist;
bool isNumberExist[10]={};

void SetNumberExist(int x) {
    if (isNumberExist[x] == false) {
        isNumberExist[x] = true;
        totalNumberExist++;
    }
}

void CheckNumber(ll n) {
    if (n == 0) {
        SetNumberExist(0);
    }
    while (n > 0) {
        SetNumberExist(n % 10);
        n /= 10;
    }
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    //std::ios::sync_with_stdio(false);
    int T, n;
    ll x;
    scanf("%d", &T);
    rep (i,1,T) {
        scanf("%d",&n);
        totalNumberExist = 0;
        Set(isNumberExist, false);
        printf("Case #%d: ", i);
        if (n == 0) printf("INSOMNIA\n");
        else {
            x = 0;
            while (totalNumberExist != 10) {
                x += n;
                CheckNumber(x);
            }
            printf("%I64d\n", x);
        }
    }
    return 0;
}
