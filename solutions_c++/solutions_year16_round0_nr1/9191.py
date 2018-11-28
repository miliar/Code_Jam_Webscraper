// 1861_MonkeyBananaProblem2.cpp

#include <iostream>
#include <vector>
#include <iomanip>
#include <queue>
#include <string>
#include <math.h>
#include <functional>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <cstdio>
#include <bitset>
#include <algorithm>    

using namespace std;

//Shortcuts for "common" data types in contests
typedef long long int ll;
typedef pair<int, int > pii;
typedef vector<int > vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

//  ans = a ? b : c;                    //To simplify: if(a) ans = b; else ans = c
//  ans += val;                         //To simplify: ans = ans + val;
//  index = (index + 1)%n;          
//  index = (index + n - 1)%n;
//  int ans = (int)((double)d + 0.5);   //For rounding to the nearest integer
//  ans = min(ans, new_computation);    //min/max shortcut

#define INF 1000000000
#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d%d", &x, &y)
#define S3(x, y, z) scanf("%d%d%d", &x, &y, &z)
#define P(x) printf("%d\n", x)
#define all(v) v.begin(), v.end()
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

set<int> digits;

void getDigInSet(unsigned long long int m){

    while(m > 0){

        digits.insert(m%10);
        m /= 10;
    }
}

int getAns(int n){

    int counter = 1;

    unsigned long long int m = n*counter;

    while(digits.size() < 10){

        m = n*counter;
       // cout<<"m = "<<m<<endl;
        getDigInSet(m);
        counter++;
    }

    counter--;

    //printf("\n");
    return counter;
}

int main() {

    int cases;
    S(cases);

    unsigned long long int n;

    for1(i, cases){

        scanf("%lld", &n);

        if(!n)
            printf("Case #%d: INSOMNIA\n", i);

        else{

            digits.clear();
            unsigned long long int ans = getAns(n)*n;
            printf("Case #%d: %lld\n", i, ans);
        }
    }
    
    return 0;
}