#include <bits/stdc++.h>
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

#define DEBUG 0
#define dout if(DEBUG) cout

bool was[10];
int need;

void update(ll a){
    while(a){
        int t = a % 10;
        a /= 10;
        if(!was[t]){
            need--;
            was[t] = 1;
        }
    }
}



void solve(ll n){
    if(!n){
        printf("INSOMNIA\n"); return;
    }
    for(int i = 0; i < 10; i++){
        was[i] = 0;
    }
    need = 10;
    ll cur = n;
    for(int i = 1; ; i++){
        update(cur);
        if(!need){
            printf("%I64d\n", cur); return;
        }
        cur += n;
    }
}

void precalc(){
    for(int i = 1; i <= 1000000; i++){
        solve(i);
    }
}

int main()
{
	#ifdef NASTYA
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    #else
    //assert(freopen(file".in","r",stdin)); assert(freopen(file".out","w",stdout));
    #endif
	int t = 1;
	cin >> t;
	int cs = 1;
	ll n;
	while(t--){
        printf("Case #%d: ", cs++);
        scanf("%I64d", &n);
		solve(n);
	}
	return 0;
}
