#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <sstream>

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream SS;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) MAX(a,-(a))

#define SS(a) scanf("%d",&a)
#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define MOD 1000000007
#define INF (1<<31)

vector <LL> res;

bool check(LL n){
    LL i;
    for (i=1;n/i;i*=10);
    i/=10;
    for (LL k=1;i>k;k*=10,i/=10){
        if ((n/k)%10 != (n/i)%10) return false;
    }
    return true;
}

void preprocess(){

    for (LL i=1;i<=10000000;i++){
        if (check(i) && check(i*i)) res.PB(i*i);
    }

}

int main(){
    freopen("C-large-1.in","r",stdin);
    freopen("c2.out","w",stdout);
    preprocess();
    int t;
    cin>>t;
    FOR(tt,1,t){
        LL a,b;
        cin>>a>>b;
        int pos1 = (int)(lower_bound(res.begin(),res.end(),b) - res.begin());
        if (res[pos1] != b) pos1--;
        int pos2 = (int)(lower_bound(res.begin(),res.end(),a) - res.begin());
        printf("Case #%d: ",tt);
        cout<<pos1-pos2+1<<endl;
    }
    return 0;
}
