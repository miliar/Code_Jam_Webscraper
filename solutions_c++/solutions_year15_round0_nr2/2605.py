#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctype.h>




#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FORD(i,a,b) for (int i=((int)(a))-1; i>=(b); --i)
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define ALL(u) (u).begin(),(u).end()


#define st first
#define nd second   
#define inf 2000000000
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define N (1<<20)
#define milion 1000000
#define oneoneone ios_base::sync_with_stdio(false)



using namespace std;

const int rozmiar_kubelka = 356;

typedef long long ll;
typedef double K;
typedef pair<int, int > pii;
typedef pair<ll, ll> pll;
typedef unsigned long long ull;
typedef pair<ll, int > pli;
typedef pair<int, ll > pil;

void dodajElement(int a, ll b, vector< ll> &S) {
    a+=S.size()/2;
    while(a>0) {
        S[a]+=b;
        a/=2;
    }
}
ll sumaOdAdoB(int a, int b, vector< ll > &S) {
    a+=S.size()/2;
    b+=S.size()/2;
    ll wynik = 0;
    while(a<=b) {
        if(a&1) {
            wynik+=S[a];
            a++;
        }
        if(!(b&1)) {
            wynik+=S[b];
            b--;
        }
        a/=2;
        b/=2;
    }
    return wynik;
}

int solve(vector<int > a ) {
    pii maxi = mp(0,0);
    for(int i = 0; i < a.size(); i++) {
        maxi = max(maxi, mp(a[i], i));
    }
    int myRes = 100000;
    if(maxi.x > 2) {
        vector<int > b;
        for(int i = 0; i < a.size(); i++) {
            if(a[i] > 1) {
                b.pb(a[i]-1);
            }
        }
        myRes = solve(b);
        a.erase(a.begin() + maxi.y);
        for(int i = 2, j = maxi.x -2; i <= j ; ) {
            b= a;
            b.pb(i);
            b.pb(j);
            myRes = min(myRes, solve(b));
            i++;
            j--;
        }
    }
    return min(maxi.x, myRes+1);       
}

void testCase(int T) {
    int D;
    scanf("%d", &D);
    std::vector<int> res;
    REP(i,D) {
        int a;
        scanf("%d", &a);
        res.pb(a);        
    }
    int result = solve(res);
    printf("Case #%d: %d\n", T, result);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i =1 ; i <= T; i++) {
        testCase(i);
    }
    return 0;
}
