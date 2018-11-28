#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <climits>

#define all(c) (c).begin(), (c).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const int INF=100000000;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
using namespace std;
typedef pair<int ,int > P;
typedef long long ll;

int m[10004];
int func(int i,bool f) {
    int res=m[i];
    if(m[i]>m[i+1]) res=min(res,m[i]-m[i+1]);
    if(f&&m[i]<=m[i+1]) res=0;
    return res;
}
int func2(int i,int a) {
    int res=a;
    if(m[i]<a) res=m[i];
    return res;
}
int method1(int n) {
    int res=0;
    rep(i,n-1) {
        res+=func(i,true);
    }
    return res;
}
int method2(int n) {
    int res=0;
    int a=0;
    rep(i,n-1) a=max(a,func(i,true));
    rep(i,n-1) {
        res+=func2(i,a);
    }
    return res;
}
void solve() {
    int n;
    cin>>n;
    rep(i,n) cin>>m[i];
    cout<<method1(n)<<" "<<method2(n)<<endl;
}

int main() {
    int T;
    cin>>T;

    rep(i,T) {
        printf("Case #%d: ",i+1);
        solve();
    }

    return 0;
}

