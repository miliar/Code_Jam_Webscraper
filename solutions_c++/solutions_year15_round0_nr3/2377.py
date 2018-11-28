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


int result[16][16] = { {0,0,0,0,0}, {0,1,2,3,4}, {0,2, -1, 4, -3}, {0,3, - 4, - 1, 2}, {0,4, 3, -2, -1} };
int myMultiply(int a, int b) {
    int it = 1;
    it*=a*b;
    if(it > 0 ) return result[abs(a)][abs(b)];
    else return -result[abs(a)][abs(b)];
}


void testCase(int T) {
    string a;
    int X, L;
    cin>>L>>X;
    string b;
    cin>>b;
    REP(i,X) {
        a+=b;
    }


    vector<int > placesLeft, placesRight;
    vector<int > prefixMultiply;
    int curr = 1;
    for(int i = 0; i < a.size(); i++) {
        int myInt= 2;
        if(a[i] == 'k') {
            myInt = 4;

        }
        else if(a[i] == 'j') {
            myInt = 3;
        }
        curr = myMultiply(curr, myInt);
        if(curr == 2) {
            placesLeft.pb(i);
        }
        prefixMultiply.pb(curr);
    } 
    if(placesLeft.size() == 0 ) {
        cout<<"Case #"<<T<<": NO\n";
        return;
    }
    curr = 1;
    for(int i = a.size()-1; i>1; i--) {
        int myInt= 2;
        if(a[i] == 'k') {
            myInt = 4;

        }
        else if(a[i] == 'j') {
            myInt = 3;
        }
        curr = myMultiply(myInt, curr);
        if(curr != 4) {
            continue;
        }
        if(placesLeft[0] >= i -1 ) {
            cout<<"Case #"<<T<<": NO\n";
            return;
        }
        if(prefixMultiply[i-1] == 4 ) {
            cout<<"Case #"<<T<<": YES\n";
            return;
        }
    }
    cout<<"Case #"<<T<<": NO\n";
            return;
}

int main() {
    oneoneone;
    int T;
    cin>>T;
    for(int i = 1; i <= T; i++) {
        testCase(i);
    }
    return 0;
}
