/*
 *Author:       Zhaofa Fang
 *Created time: 2015-04-11-11.45 ÐÇÆÚÁù
 */
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
#define DEBUG(x) cout<< #x << ':' << x << endl
#define FOR(i,s,t) for(int i = (s);i <= (t);i++)
#define FORD(i,s,t) for(int i = (s);i >= (t);i--)
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n-1);i>=0;i--)
#define PII pair<int,int>
#define PB push_back
#define ft first
#define sd second
#define lowbit(x) (x&(-x))
#define INF (1<<30)
#define eps (1e-8)

const int MAXN = 1011;
char str[MAXN];
int sum[MAXN];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        printf("Case #%d: ",cas);
        int n;
        scanf("%d",&n);
        scanf("%s",str);
        if(n>0)sum[0] = str[0]-'0';
        int inc = 0;
        for(int i=1;i<=n;i++){
            int d = str[i] - '0';
            int diff = i - sum[i-1] - inc;
            if(diff > 0){
                inc += diff;
            }
            sum[i] = sum[i-1] + d;
        }
        printf("%d\n",inc);
    }
    return 0;
}
