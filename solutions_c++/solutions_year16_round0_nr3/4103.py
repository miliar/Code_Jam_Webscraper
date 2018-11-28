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

const int MAXN = 20;

ll dv[MAXN];
int n, J;

ll isPrime(ll a){
    for(ll i = 2; i * i <= a; i++){
        if(a % i == 0){
            return i;
        }
    }
    return -1;
}

bool good(string mask){
    for(int b = 2; b <= 10; b++){
        ll cur = 0;
        for(int i = 0; i < n; i++){
            cur *= b;
            if(mask[i] == '1'){
                cur++;
            }
        }
        ll ans = isPrime(cur);
        if(ans == -1) return 0;
        dv[b] = ans;
    }
    return 1;
}


void rec_sol(int cur, string mask){
    if(!J) return;
    if(cur == n){
       if(good(mask)){
            J--;
            cout << mask;
            printf(" ");
            for(int b = 2; b <= 10; b++){
                printf("%I64d ", dv[b]);
            }
            printf("\n");
        }
        return;
    }
    rec_sol(cur + 1, mask + '1');
    if(cur && cur < n - 1) rec_sol(cur + 1, mask + '0');
}

void solve(){
    cin >> n >> J;
    rec_sol(0, "");
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
	while(t--){
        printf("Case #%d:\n", cs++);
		solve();
	}
	return 0;
}
