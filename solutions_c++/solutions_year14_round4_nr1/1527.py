#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <bitset>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <limits.h>
#include <limits>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <string.h>
#include <assert.h>
#include <numeric>
using namespace std;

#define MOD 1000000007
#define mp make_pair
#define pb push_back
typedef long long LL;
int a[1000002];

char s1[222222];
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int casen;
    scanf("%d",&casen);
    for (int casei=0;casei<casen;casei++){
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a,a+n);
        int lx=0,rx=n-1,ans=0;
        while (rx>=lx){
            if (a[lx]+a[rx]<=m) {ans++;lx++;rx--;}else{ans++;rx--;}
        }
        printf("Case #%d: %d\n",casei+1,ans);

    }
}
