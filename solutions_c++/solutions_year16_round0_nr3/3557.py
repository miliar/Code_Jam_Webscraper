/// in the name of ALLAH

//#include <bits\stdc++.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <stdio.h>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <deque>
#include <sstream>
#include <string>
#include <fstream>

#define bits(a) __builtin_popcount(a)
#define ll long long
int dx[] = {1 , -1 , 0 , 0 };
int dy[] = {0 ,  0 , 1 , -1};
const int mod = (int)1e9 + 7;
const int oo = 1<<30;
const ll loo = (ll)1<<60;
const double pi = 3.14159265359;
const int N = (int) 1e2 + 5;

using namespace std;

int n , j , fooo = 0;
map<int  , vector<ll> > ma;

int prime(ll num) {
    int sq = sqrt(num) + 1;
    for(int i = 2; i <= sq; i ++) {
        if(num % i == 0){
            return i;
        }
    }
    return 0;
}
vector<ll> checkbases(int s) {
    vector<ll> res , a;
    a.push_back(-1);
    for(int i = 2; i <= 10; i ++) {
        ll sum = 0 , foo = 1;
        for(int j = n-1; j >= 0; j -- , foo *= i) {
            if((s & (1 << j))) {
                sum += foo;
            }
        }
        int get = prime(sum);
        if(get > 0) {
           res.push_back(get);
        } else
            return a;
    }
    fooo++;
    return res;
}
bool memo[20][1<<17];
void foo(int idx , int s) {
    if(fooo >= 50)
        return;
    if(idx == n){
        vector<ll> v = checkbases(s);
        if(v[0] != -1)
            ma[s] = v;
        return;
    }
    if(memo[idx][s])
        return;
    if(idx == 0 || idx == n-1)
        foo(idx + 1 , (1<<idx | s));
    else {
        foo(idx + 1 , (1<<idx | s));
        foo(idx + 1 , s);
    }
    memo[idx][s] = 1;
}
bool b;
ll tobits(int num) {
    ll s = 0;
    for(int i = 0; i < n; i ++) {
        if((1<<i) &num)
            s = s * 10 + 1;
        else
            s = s*10 ;
    }
    return s;
}

//#define in cin
//#define out cout
int main() {
    fstream in("C-small-attempt4.in" , ios::in);
    fstream out("out.out" , ios::out);
    int t;
    in >> t;
    in >> n >> j;
    foo(0 , 0);
    out << "Case #1:\n";
    for(map<int , vector<ll> > :: iterator it = ma.begin(); it != ma.end() && j--; it ++) {
         out << tobits(it->first);
         for(int i = 0; i < 9; i ++)
            out << ' ' << (it->second)[i];
         out << '\n';
    }
}


