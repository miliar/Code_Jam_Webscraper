#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdio.h>
#include <cstdio>
#include <stdlib.h>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <climits>
#include <set>
#include <bitset>
#include <math.h>
#include <queue>
#include <map>

typedef long long ll;
typedef long double ld;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
typedef std::pair<double, double> pdd;

#define PI 3.1415926535897932384626433
#define INF ((1<<30)-1)*2+1
#define mp(a, b) make_pair((a), (b))
#define pb push_back
#define MOD 1000000007
#define MAX_N 100000
using namespace std;

map<ll, bool> primes;
int bits = 16;
bool small = true;

map<ll, pair<ll, vector<ll> > > A;

bool isPrime(ll x){
    //cout << "." <<  primes[x] << "." << endl;
    if(primes.find(x) != primes.end())
        return primes[x];
    if(x <= 1)
        return primes[x] = false;
    if(x == 2){
        return primes[x] = true;
    }
    for(ll i = 2; i * i <= x; i++){
        if(x%i == 0){
            return primes[x] = false;
        }
    }
    return primes[x] = true;
}

bool isJamCoin(ll i){
    vector<ll> t;
    ll bTen;
    for(ll base = 2; base <= 10; base++){
        ll tmp = i;
        ll mul = 1;
        ll ans = 0;
        while(tmp > 0){
            ans += mul*(tmp&1);
            mul *= base;
            tmp >>= 1;
        }
        //cout << ans << endl;
        if(base == 10)
            bTen = ans;
        if(isPrime(ans))
            return false;
        for(ll j = 2; j < ans; j++){
            if(ans%j == 0){
                t.pb(j);
                break;
            }
        }
    }
    A[i] = mp(bTen, t);
    return true;
}



int main()
{
    freopen("in.txt","r",stdin);
    freopen("output.txt", "w", stdout);
    int J = 50;
    small = true;
    if(small){
        bits = 16;
        cout << "Case #1:" << endl;
        for(ll i = USHRT_MAX; i >= 0 && J > 0; i--){
            if(i&1 && i&(1<<(bits-1)) && isJamCoin(i)){
                //cout << 51-J << ") " <<  i << " ";
                cout << A[i].first << " ";
                for(int j  = 0; j < A[i].second.size(); j++){
                    cout << A[i].second[j] << " ";
                }cout << endl;
                J--;
            }
        }
    }else{
        bits = 32;
        for(ll i = UINT_MAX; i >= 0 && J > 0; i--){
            if(i&1 && i&(1<<(bits-1)) && isJamCoin(i)){
                cout << 501-J << ") " << i << endl;
                J--;
            }
        }
    }
    /*map<ll, bool>::iterator it;
    for(it = primes.begin(); it != primes.end(); it++)
        cout << (*it).first << " " << (*it).second << endl;*/



    return 0;
}
