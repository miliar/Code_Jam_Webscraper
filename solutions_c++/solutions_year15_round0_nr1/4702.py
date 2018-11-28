/***********************************************\
 |Author: YMC
 |Created Time: 2015/4/11 9:09:04
 |File Name: a.cpp
 |Description: 
\***********************************************/
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#define L(rt) (rt<<1)
#define R(rt) (rt<<1|1)
#define mset(l,n) memset(l,n,sizeof(l))
#define rep(i,n) for(int i=0;i<n;++i)
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
#define srep(i,n) for(int i = 1;i <= n;i ++)
#define MP make_pair
const int inf=0x3f3f3f3f ;
const double eps=1e-8 ;
const double pi=acos (-1.0);
typedef long long ll;

using namespace std;
int n;
char s[1005];
int main() {
	//freopen("A-large.in","r",stdin); 
	//freopen("A-large.out","w",stdout); 
    int T;
    scanf("%d",&T);
    int cas = 1;
    while(T--) {
        scanf("%d",&n);
        scanf("%s",s);
        int now = 0;
        int ans = 0;
        rep(i,n+1) {
            if(now < i) {
                ans += i - now;
                now = i;
            }
            now += s[i] - '0';
        }
        printf("Case #%d: %d\n",cas ++, ans);
    }
	return 0;
}

