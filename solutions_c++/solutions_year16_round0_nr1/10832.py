/* #######################
 * ###   This page by  ###
 * ###  YuRa__Sultonov ###
 * #######################
 */
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <cstdio>
#include <stdlib.h>
#include <queue>
#include <vector>
#include <string>
#include <string.h>
#define scani(a)    scanf("%d",&a);
#define scanl(a)    scanf("%I64d",&a);
#define scand(a)    scanf("%lf",&a);
#define printi(a)    printf("%d ",a);
#define printl(a)    printf("%I64d ",a);
#define el  printf('\n');
#define FOR(i,b)    for(int i = 1; i <= b; ++i)
#define ROF(i,n)    for(int i = n; i >= 1; --i)
#define REP(i,a,b)  for(int i = a; i <= b; ++i)
#define PER(i,a,b)  for(int i = b; i <= a; --i)
#define get(a, n)   for(int i = 1; i <= n; ++i) cin >> a[i];
#define int long long
#define getm(a, n, m) for (int i = 1; i <= n; ++i) for (int j = 1; j <= m; ++j) cin >> a[i][j];
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define sz(x) ((int)(x).size())
#define maxn 1000001
#define INF 1000000000
#define inf -1000000000
#define ll long long
#define db double
#define pi M_PI
#define EPS -1e9
#define file "in_file"
using namespace std;
ll gcd(ll a,ll b);
ll lcm(ll a,ll b);
ll binary_power(ll a,ll n);
db alfa(db a, db b, db c);
ll phi (ll n);
ll inversePrime(ll a, ll m);
ll inverseCoprimes(ll a, ll m);
ll inverse(ll a, ll m);
void blah_blah(){
    int n;
    cin >> n;
    for(int test = 1; test <= n; test ++ ){
        int x;
        cin >> x;
        bool used[10];
        for(int k = 0; k < 10; k++)
            used[k] = 0;
        bool okay = 1;
        if(x == 0){
            cout << "Case #" << test << ": INSOMNIA\n";
            continue;
        }
        for(int k = 1; k <= 1e6; k++){
            int t = k * x;
            while(t > 0){
                used[t % 10] = 1;
                t /= 10;
            }
            okay = 1;
            for(int h = 0; h < 10; h++){
                okay &= used[h];
            }
            if(okay){
                cout << "Case #" << test << ": " << k * x << "\n";
                break;
            }
        }
        if(!okay){
            cout << "Case #" << test << ": INSOMNIA\n";
            continue;
        }
    }
}
/*
int dx[]={-1,-1,-1,0,1,1,1,0};
int dy[]={-1,0,1,1,1,0,-1,-1};
*/
main(){
    freopen(file".in", "r", stdin); freopen(file".out", "w", stdout);
    ios::sync_with_stdio(false);
    int t = 1;
    while(t --){
        blah_blah();
    }
    return 0;
}
ll gcd(ll a,ll b){
    return b == 0 ? a : gcd(b, a % b);
}
ll lcm(ll a,ll b){
    return a / gcd(a, b) * b;
}
ll binary_power(ll a,ll n){
    ll res = 1;
    while(n){
        if(n & 1)   -- n, res = res * a;
        else a = a * a, n >>= 1;
    }
    return res;
}
db alfa(db a, db b, db c){
    return acos((a * a - b * b + c * c) / (2 * a * c));
}
ll phi (ll n) {
	ll result = n;
	for (ll i = 2; i * i <= n; ++i)
		if (n % i == 0) {
			while (n % i == 0)
				n /= i;
			result -= result / i;
		}
	if (n > 1)
		result -= result / n;
	return result;
}
ll inversePrime(ll a, ll m){
    return binary_power(a, m - 2) % m;
}
ll inverseCoprimes(ll a, ll m){
    return binary_power(a, phi(m) - 1) % m;
}
ll inverse(ll a, ll m){
    if(gcd(a, m) == 1) {
        return inverseCoprimes(a, m);
    } else {
        return -1;
    }
}
