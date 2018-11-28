#include <stdio.h>
#include <iostream>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <complex>
#include <ctime>
#include <iomanip>
#include <cassert>
#include <sstream>
#include <iterator>

using namespace std;

#define file "file"
#define mp make_pair
#define pb push_back
#define xx real()
#define yy imag()
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef complex<double> point;

const int MAXN = 1e3 + 5;
const int INF = 1e9;

int ans;
map<multiset<int> ,int> list;

void rec_sol(vi &a,int step){
    if(ans < step) return;
    multiset<int> c(a.begin(),a.end());
    if(list.find(c) != list.end()){
        if(list[c] <= step) return;
    }
    list[c] = step;
    int sz = a.size();
    int fl = 0;
    for(int i = 0;i < sz;i++){
        if(a[i]){
            fl = 1; break;
        }
    }
    if(!fl){
        ans = min(ans,step);
        return;
    }
    vi b;
    for(int i = 0;i < sz;i++){
        if(a[i]) b.pb(a[i]);
    }
    vi a2 = b;
    sz = a2.size();
    for(int i = 0;i < sz;i++){
        if(b[i]) b[i]--;
    }
    rec_sol(b,step + 1);
    if(ans < step) return;
    b.pb(0);
    for(int i = 0;i < sz;i++){
        b[i]++;
    }
    for(int i = 0;i < sz;i++){
        for(int j = 1;j <= a2[i] / 2;j++){
            b[i] = j;
            b[sz] = a2[i] - j;
            rec_sol(b,step + 1);
            b[i] = a2[i];
        }
    }
}

void solve(){
    int n,v;
    scanf("%d",&n);
    ans = INF;
    vi a;
    list.clear();
    for(int i = 0;i < n;i++){
        scanf("%d",&v);
        a.pb(v);
    }
    rec_sol(a,0);
    printf("%d\n",ans);
}

int main()
{
//	#ifndef ONLINE_JUDGE
//    assert(freopen("input.txt","r",stdin));
//    assert(freopen("output.txt","w",stdout));
//    #else
//    //assert(freopen(file".in","r",stdin)); assert(freopen(file".out","w",stdout));
//    #endif
	int t = 1;
	int cs = 1;
	scanf("%d",&t);
	while(t--){
        printf("Case #%d: ",cs++);
		solve();
	}
	return 0;
}
