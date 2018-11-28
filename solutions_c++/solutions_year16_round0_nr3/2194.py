#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>
#include <queue>
#include <string>
#include <cmath>
#include <map>
#include <set>
#define MOD 1e9 + 7
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define sz(a) a.size()
#define loop(i, n) for(long long (i) = 0; (i) < (n) ; ++ (i))
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>  
typedef long long ll;
typedef long double ld;

using namespace std;


/*@Sergey_Miller*/

vector <ll> primes;

ll MAXX = 1e4;

void calc() {
    loop(i,MAXX) {
          if(i == 1 || i == 0) {
                continue;
            }
        bool f = 0;
        loop(j,sz(primes)) {
            if(i % primes[j] == 0) {
                f = 1;
                break;
            }
        }

        if(!f) {
            primes.pb(i);
        }
    }
    cout << sz(primes) << endl;
}

vector <vector <ll> > ans;
vector <string> str;

bool modd(vector <int>& bln, int base, ll pr) {
    ll sum_cost = 0;
    ll basecost = 1;
    //cout << "Ok1 " << endl;

    loop(i,sz(bln)) {
        sum_cost += (basecost * bln[i]);
        sum_cost %= pr;
        basecost *= base;
        basecost %= pr;
    }
    //cout << "Ok2" << endl;

    return !sum_cost;
}

ll check_pr(vector <int>& bln, int base) {
    //cout << "Ok" << endl;
    loop(i, sz(primes)) {
        if(modd(bln, base, primes[i])) {
            return primes[i];
        }
    }

    return -1;
}

bool check(ll n) {
    vector <int> bln(32,0);
    bln[0] = 1;
    bln[31] = 1;
    int pos = 1;
    ll k = n;
    while(k){
        bln[pos] = k % 2;
        ++pos;
        k /= 2;
    }

    //cout << "Ok" << endl;

    vector <ll> del;
    for (int b = 2; b <= 10; ++b) {
        ll cd = check_pr(bln,b);
        if(cd == -1) {
            return false;
        }
        del.pb(cd);
    }
    string s = "";
    loop(i,sz(bln)) {
        s += ('0' + bln[31 - i]);
    }
    str.pb(s);
    ans.pb(del);
    return true;
}

void solve() {
    int find = 0;

    loop(i,powl(2,30)) {
        cout << find << endl;
        if(find == 500) {
            break;
        }
        if(check(i)) {
            ++find;
        }
    }

    loop(i,sz(str)) {
        cout << str[i] << " ";
        loop(j,sz(ans[i])) {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }
}


int main () {
    ios::sync_with_stdio(false);
     // freopen("input.txt", "r", stdin);
     // freopen("output.txt", "w", stdout);
    calc();
    solve();
    return 0;
}

