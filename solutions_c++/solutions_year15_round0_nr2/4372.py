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

bool decr(int i, int j) {
    return i>j;
}
int solve() {
    int i, j, k;
    int cust;
    vi pk;
    vi sols;
    cin>>cust;
    fi(cust) {
        cin>>j;
        pk.pb(j);
    }
    int mins = 0;
    sort(pk.begin(), pk.end(), decr);
    sols.pb(pk[0]);
    if(TEST) { fi(pk.size()) cout<<pk[i]<<" "; cout<<endl; }
    while(true) {
        if(pk[0] <= 2) break;
        int tmp = pk[0];

        int i=1;
        while(i<pk.size() && pk[i]==tmp) i++;

        int tmp2 = tmp%2 + tmp/2;
        if((tmp == 9) && (i == 1)) tmp2 = 6;
        if(i<pk.size() && pk[i]>tmp2) tmp2 = pk[i];


        if(TEST) cout<<"chkval: "<<mins + i + tmp2<<" - "<<mins + pk[0]<<" i: "<<i<<endl;
        //if((mins + i + tmp2) > (mins + pk[0])) break;
        sols.pb(mins + i + tmp2);

        mins += i;
        int nxt = i;
        printTest("tmp: ", tmp, " i: ", i, " tmp2: ", tmp2, "nxt: ", pk[nxt]);
        while(i--) {
            if((tmp==9) && (tmp2 == 6)) {
                pk[i]=6;
                pk.pb(3);
            } else {
                pk[i]=tmp%2 + tmp/2;
                pk.pb(tmp/2);
                //cout<<"here";
            }
        }
        sort(pk.begin(), pk.end(), decr);
        if(TEST) { fj(pk.size()) cout<<pk[j]<<" "; cout<<endl; }
    }
    /*
    while(true) {
        if((pk[0] <=2)) break;
        int tmp = pk[0];
        i=1;
        while(i<pk.size() && tmp==pk[i]) i++;

        vi pk2;
        fj(pk.size()) {
            while(i--) {
                pk2.pb(pk[i]%2 + pk[i]/2);
                pk2.pb(pk[i]/2);
                j++;
            }
            pk2.pb(pk[j]);
        }
        sort(pk2.begin(); pk2.end());
        fj(pk2.size()) cout<<pk2[j]<<" ";
        //printTest("tmp:", tmp, " i:", i);
        j=0;
        while(i<pk2.size() && pk2[0]==pk2[j]) j++;

        printTest("chkval: ", (mins+i+j + tmp));

        if((mins+ct + tmp) >= (mins + pk[0])) break;
        mins += i;

        tmp =  pk[0];
        while(i--) {
        pk[i] = tmp%2 + tmp/2;
        pk.pb(tmp/2);
        }
        sort(pk.begin(), pk.end(), decr);
        fi(pk.size()) cout<<pk[i]<<" "; cout<<endl;
    }
    */
    sort(sols.begin(), sols.end(), decr);

    mins += pk[0];
    return sols.back();

}
int main() {


    int i, j, k, tt, cases;
    freopen("B-small-attempt9.in", "r", stdin);
    //freopen("A-test.in", "r", stdin);
    freopen("b-small-sol9.out", "w", stdout);

    cin>>tt;

    fr(cases, 1, tt+1) {
        int sol = solve();
        cout<<"Case #"<<cases<<": "<<sol<<endl;
    }
}
