// vudduu - codejam 2016 qualification round
// Problem C
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

LL toDecimal(string n, int b) {
    LL result=0;
    LL multiplier = 1, j = n.S - 1;
    while (j >= 0) {
        result += multiplier * LL(n[j]-'0');
        multiplier *= b;
        j--;
    }
    return result;
}

vector<LL> primes;
const int MAXP = 66000;
bool criba[MAXP+2];

void generatePrimes() {
    memset(criba, false, sizeof(criba));
    criba[0] = criba[1] = true;
    int raiz = (int)sqrt(MAXP);
    for (int i=3; i<=raiz; i+=2) {
        if (!criba[i])
            for (int j=i*i; j<=MAXP; j += i)
                criba[j] = true;
    }
    primes.PB(2);
    primes.PB(3);
    for (int i=5, j=7; i<=MAXP; i+=6, j+=6){
        if (!criba[i])
            primes.PB(i);
        if (!criba[j])
            primes.PB(j);
    }
}

LL check(LL n) {
    LL raiz = (LL)sqrt(n);
    for (LL i=2; primes[i] <= raiz && i<primes.S; ++i) {
        if (n % primes[i] == 0)
            return primes[i];
    }
    return -1LL;
}

set<LL> conj;
LL getDivisor(LL n) {
    LL raiz = (LL)sqrt(n);
    for (LL i=2; primes[i] <= raiz && i<primes.S; ++i) {
        if (n % primes[i] == 0) {
            LL a = primes[i];
            LL b = n / primes[i];
            if(conj.find(a) == conj.end()) {
                conj.insert(a);
                return a;
            }
            if(conj.find(b) == conj.end()) {
                conj.insert(b);
                return b;
            }
        }
    }
    return 0;
}

int N, J;
string num;

bool isValid(string x) {
    vector<LL> v;
    conj.clear();
    FOR(i, 2, 11) {
        LL y = toDecimal(x, i);
        LL divi = check(y);
        if(divi == -1) {
            return false;
        }
        divi = getDivisor(y);
        v.PB(divi);
    }
    cout << x;
    F(i, v.S) {
        cout << " " << v[i];
    }
    cout << endl;
    return true;
}

void nextNum(string& x) {
    int it = x.S-1;
    while(it > 0) {
        if(x[it] == '0') {
            x[it] = '1';
            return;
        }
        x[it--] = '0';
    }
}

void solve() {
    cin >> N >> J;
    int genN = N-1;
    string num(genN, '0');
    num[0] = '1';
    F(i, J) {
        while(!isValid(num+'1')) {
            nextNum(num);
        }
        nextNum(num);
    }
}

int main() {
    generatePrimes();
	freopen("in.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d:\n", cas);
        solve();
    }
}
