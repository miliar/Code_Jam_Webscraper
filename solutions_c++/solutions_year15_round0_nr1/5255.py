#include<iostream>
#include<conio.h>
#include<cstdlib>
#include<windows.h>
#include<stdio.h>
#include<cstdarg>
#include<stdint.h>
#include<vector>
#include<sstream>
#include<string.h>
#include<exception>
#include<math.h>
#include <algorithm>

#define frr(a, b, c) for(a = (b); (a)>=(c); (a)--)
#define frro(a, b)   frr(a, (b), 0);
#define frri(a)      frro(i, (a))
#define frrj(a)      frro(j, (a))
#define frrk(a)      frro(k, (a))

#define fr(a, b, c) for(a = (b); (a)<(c); (a)++)
#define fo(a, b)    fr(a, 0, (b))
#define fi(a)       fo(i, (a))
#define fj(a)       fo(j, (a))
#define fk(a)       fo(k, (a))

#define uint64 uint64_t
#define ss stringstream
#define vi vector<int64_t>
#define vl vector<long>
#define vs vector<string>
#define vvi vector<vi >
#define pb push_back
#define ppb pop_back
#define MAX 1000

#define FALSE false
#define TRUE  true

//#define TEST true
#define TEST false

#define printTest(...) if(TEST) {printThis(__VA_ARGS__);}

using namespace std;

void printThis() {
    cout<<endl;
}
int ct = 0;
template<typename First, typename ... Strings>
void printThis(First arg, const Strings&... rest) {
    cout<<arg;
    printThis(rest...);
}

int solve() {
    int i, j, k;
    int smax;
    vi seq;

    cin>>smax;
    j = 0; k = 0;
    char ch;
    fi(smax+1) {
        cin>>ch;
        j += (int)(ch-48);
        printTest(j, " ", i+1);
        if(j<(i+1)) {
            k += i-j+1;
            j += (i-j+1);
            printTest("k: ", k);
        }
    }
    return k;

}
int main() {

    int i, j, k, tt, cases;
    freopen("A-large.in", "r", stdin);
    //freopen("A-test.in", "r", stdin);
    freopen("a-large-sol.out", "w", stdout);

    cin>>tt;
    fr(cases, 1, tt+1) {
        int sol = solve();
        cout<<"Case #"<<cases<<": "<<sol<<endl;
    }
}
