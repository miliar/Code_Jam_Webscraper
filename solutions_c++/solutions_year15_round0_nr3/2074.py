// Problem C. Dijkstra
// Para mi esposa Susana, en una semana me caso ^_^
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

map<pair<char,char>, pair<char,bool> > mapa;
int L, X;
string s;

bool XOR(bool a, bool b) {return (a+b)%2;}

void generate() {
    mapa[MP('1','1')] = MP('1', false);
    mapa[MP('1','i')] = MP('i', false);
    mapa[MP('1','j')] = MP('j', false);
    mapa[MP('1','k')] = MP('k', false);
    mapa[MP('i','1')] = MP('i', false);
    mapa[MP('i','i')] = MP('1', true);
    mapa[MP('i','j')] = MP('k', false);
    mapa[MP('i','k')] = MP('j', true);
    mapa[MP('j','1')] = MP('j', false);
    mapa[MP('j','i')] = MP('k', true);
    mapa[MP('j','j')] = MP('1', true);
    mapa[MP('j','k')] = MP('i', false);
    mapa[MP('k','1')] = MP('k', false);
    mapa[MP('k','i')] = MP('j', false);
    mapa[MP('k','j')] = MP('i', true);
    mapa[MP('k','k')] = MP('1', true);
}

void multi(char&a, bool&negativo, int i) {
    char b = s[i];
    pair<char,bool> p = mapa[MP(a,b)];
    negativo = XOR(negativo, p.second);
    a = p.first;
}

bool visK[10005];
bool getK(int it) {
    if(visK[it]) return false;
    visK[it] = true;
    bool negativo = false;
    char a = s[it];
    if(a == 'k' && it == s.S-1) return true;
    FOR(i, it+1, s.S) {
        multi(a, negativo, i);
    }
    return (!negativo) && (a == 'k');
}

bool getJK(int it) {
    bool negativo = false;
    char a = s[it];
    if(a == 'j')
        if(getK(it+1))
            return true;
    FOR(i, it+1, s.S) {
        multi(a, negativo, i);
        if((!negativo) && (a == 'j')) {
            if(getK(i+1))
                return true;
        }
    }
    return false;
}

bool getIJK() {
    bool negativo = false;
    char a = s[0];
    if(a == 'i')
        if(getJK(1))
            return true;
    FOR(i, 1, s.S) {
        multi(a, negativo, i);
        if(!negativo && a == 'i') {
            if(getJK(i+1))
                return true;
        }
    }
    return false;
}

void solve(int ca) {
    cin >> L >> X;
    cin >> s;
    string aux = s;
    memset(visK, 0, sizeof(visK));
    F(i, X-1) {
        F(j, aux.S)
            s.PB(aux[j]);
    }
    if(getIJK())
        printf("Case #%d: YES\n", ca);
    else
        printf("Case #%d: NO\n", ca);
}

int main(){
    // freopen("a.in.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);
    freopen("a.out.txt", "w", stdout);
    int T;
    generate();
    scanf("%d", &T);
    F(i, T){ solve(i+1); }
}

