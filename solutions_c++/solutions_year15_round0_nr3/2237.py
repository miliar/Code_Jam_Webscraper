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

// i - 2, j - 3, k - 4

const int MAXN = 1e6;
const int LIM = 10;

int mul[6][6];
char s[MAXN];
int pref[MAXN],suf[MAXN];

int m(int a,int b){
    int fl = (a * b < 0 ? -1 : 1);
    if(a < 0) a *= -1;
    if(b < 0) b *= -1;
    return mul[a][b] * fl;
}

int code(char c){
    if(c == 'i') return 2;
    if(c == 'j') return 3;
    if(c == 'k') return 4;
}

int binpow(int a,ll st){
    int ans = 1;
    for(;st;st >>= 1){
        if(st & 1) ans = m(ans,a);
        a = m(a,a);
    }
    return ans;
}

void solve(){
    int n;
    ll x;
    scanf("%d%I64d",&n,&x);
    scanf("%s",s);
    for(int i = 0;i < n;i++){
        s[i] = code(s[i]);
        if(i){
            pref[i] = m(pref[i - 1],s[i]);
        }
        else pref[0] = s[i];
        //cerr << pref[i] << " ";
    }
    //cerr << endl;
    for(int i = n - 1;i >= 0;i--){
        if(i == n - 1){
            suf[i] = s[i];
        }
        else{
            suf[i] = m(s[i], suf[i + 1]);
        }
        //cerr << suf[i] << " ";
    }
    //cerr << endl;
    ll se;
    for(ll k1 = 0;k1 < LIM;k1++){
        if(k1 > x) break;
        ll fi2 = binpow(pref[n - 1],k1);
        for(ll k3 = 0;k3 < LIM;k3++){
            if(k1 + k3 > x) break;
            ll th2 = binpow(pref[n - 1],k3);
            for(int i = 0;i < n;i++){
                ll fi = m(fi2,pref[i]);
                if(fi != 2) continue;
                for(int j = 0;j < n;j++){
                    ll th = m(suf[j],th2);
                    if(th != 4) continue;
                    ll len = x * n - (k1 + k3) * n - (i + 1) - (n - j);
                    if(len <= 0) continue;
                    ll k2 = x - k1 - k3 - 1 - 1;
                    if(k2 < 0){
                        ll p1 = pref[i];
                        ll p2 = pref[j - 1];
                        for(int t = 1;t <= 4;t++){
                            if(m(p1,t) == p2){
                                se = t; break;
                            }
                        }
                    }
                    else{
                        se = binpow(pref[n - 1],k2);
                        if(i < n - 1) se = m(suf[i + 1],se);
                        if(j) se = m(se, pref[j - 1]);
                    }
                    if(se != 3) continue;
                    printf("YES\n");
                    return;
                }
            }
        }
    }
    printf("NO\n");
}

int main()
{
//	#ifndef ONLINE_JUDGE
//    assert(freopen("input.txt","r",stdin));
//    assert(freopen("output.txt","w",stdout));
//    #else
//    //assert(freopen(file".in","r",stdin)); assert(freopen(file".out","w",stdout));
//    #endif
    for(int i = 1;i <= 4;i++){
        mul[1][i] = i;
        mul[i][1] = i;
    }
    mul[2][2] = -1;
    mul[2][3] = 4;
    mul[2][4] = -3;
    mul[3][2] = -4;
    mul[3][3] = -1;
    mul[3][4] = 2;
    mul[4][2] = 3;
    mul[4][3] = -2;
    mul[4][4] = -1;
	int t = 1;
	scanf("%d",&t);
	int cs = 1;
	while(t--){
        printf("Case #%d: ",cs++);
		solve();
	}
	return 0;
}
