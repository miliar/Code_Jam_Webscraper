//no comment needed
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <string.h>
#include <strings.h>
#include <math.h>
#include <time.h>
#include <map>
#include <climits>
using namespace std;

//Two of the most frequently used typical of long names, make life easier
typedef vector<int> VI;
typedef long long LL;

/* HEADERS */

/* Loops */
// FOR - loop increasing 'x' from 'b' to 'e' inclusive
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
// FORD - loop decreasing 'x' from 'b' to 'e' inclusive
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
// REP - loop increasing 'x' from '0' to 'n'. Used to search and build DS
#define REP(x, n) for(int x = 0; x < (n); ++x)
// Clone long type of 'n'
#define VAR(v, n) __typeof(n) v = (n)
// ALL(c) represents the pair of iterators, indicating begin-end elements in the STL DS
#define ALL(c) (c).begin(), (c).end()
//Macro to get size of STL DS, used to avoid compilation warrning with int and uint comp
#define SIZE(x) ((int)(x).size())
// Very profitable macro aimed to iterate through all elements of STL DS
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)

/* Shortcuts for vectors most common use cases*/
#define PB push_back
#define POP pop_back
#define ST first
#define ND second
#define RM( v, x )  v.erase(v.begin() + x)
#define PF( v, x )  v.insert(v.begin(), x);
#define FIND(v, x)  find(v.begin(), v.end(), x)
#define Vit         std::vector<int>::iterator

/* some other usefull methods */
#define INF     INT_MAX/2-256
#define _il     inline
#define _ili    inline int
#define _ilv    inline void

#define IN      "in"
#define OUT     "out"
#define ERR     "err"

_ilv sol(int tc, int N);
//debug print
void print_v(VI v){
fprintf(stderr, "vec:: ");
    FOREACH(it, v)
        fprintf(stderr, "%d, ", *it);
fprintf(stderr, "\n");
}


int A [29];
const int OF = 65;
string ZE = "ZERO";
string ONE =  "ONE";
string TWO = "TWO";
string THREE = "THREE";
string FOUR = "FOUR";
string FIVE = "FIVE";
string SIX = "SIX";
string SEVEN = "SEVEN";
string EIGHT = "EIGHT";
string NINE = "NINE";

int main(){
    //sample
//    freopen(IN,  "r", stdin);
//    freopen(OUT, "w", stdout);
//    freopen(ERR, "w", stderr);

    int TT; cin >> TT;

FOR(i,0,3)ZE[i]-=OF;
FOR(i,0,2)ONE[i]-=OF;
FOR(i,0,2)TWO[i]-=OF;
FOR(i,0,4)THREE[i]-=OF;
FOR(i,0,3)FOUR[i]-=OF;
FOR(i,0,3)FIVE[i]-=OF;
FOR(i,0,2)SIX[i]-=OF;
FOR(i,0,4)SEVEN[i]-=OF;
FOR(i,0,4)EIGHT[i]-=OF;
FOR(i,0,3)NINE[i]-=OF;

    REP(tt, TT){
        int N=0;// and more

        sol(tt+1, N); //run sol
    }

    return 0;
}


_ilv sol(int tc, int N )
{
    //do work
    string s; cin >> s;

    FOR(i,0,25)
        A[i] = 0;

    for(int i=0; i<s.size(); i++)
        A[s[i]-OF] ++;

printf("Case #%d: ", tc);
VI vc;

    while(A[ZE[0]]>0 && A[ZE[1]]>0 && A[ZE[2]]>0 && A[ZE[3]]>0 ){
        A[ZE[0]]--; A[ZE[1]]--; A[ZE[2]]--; A[ZE[3]]-- ;
vc.PB(0);
    }

while(A[SIX[0]]>0 && A[SIX[1]]>0 && A[SIX[2]]>0 ){
        A[SIX[0]]--; A[SIX[1]]--; A[SIX[2]]--;
vc.PB(6);
    }

while(A[SEVEN[0]]>0 && A[SEVEN[1]]>1 && A[SEVEN[2]]>0 && A[SEVEN[3]]>1 && A[SEVEN[4]]>0 ){
        A[SEVEN[0]]--; A[SEVEN[1]]--; A[SEVEN[2]]--;A[SEVEN[3]]--; A[SEVEN[4]]--;
vc.PB(7);
    }

while(A[FIVE[0]]>0 && A[FIVE[1]]>0 && A[FIVE[2]]>0  && A[FIVE[3]]>0 ){
        A[FIVE[0]]--; A[FIVE[1]]--; A[FIVE[2]]--;A[FIVE[3]]--;
vc.PB(5);
    }

while(A[FOUR[0]]>0 && A[FOUR[1]]>0 && A[FOUR[2]]>0 && A[FOUR[3]]>0) {
        A[FOUR[0]]--; A[FOUR[1]]--; A[FOUR[2]]--; A[FOUR[3]]--;
vc.PB(4);
    }

while(A[EIGHT[0]]>0  && A[EIGHT[1]]>0 && A[EIGHT[2]]>0 && A[EIGHT[3]]>0 && A[EIGHT[4]]>0 ){
        A[EIGHT[0]]--; A[EIGHT[1]]--; A[EIGHT[2]]--;A[EIGHT[3]]--; A[EIGHT[4]]--;
vc.PB(8);
    }

    while(A[THREE[0]]>0 && A[THREE[1]]>0 && A[THREE[2]]>0 && A[THREE[3]]>1 && A[THREE[4]]>1) {
        A[THREE[0]]--; A[THREE[1]]--; A[THREE[2]]--; A[THREE[3]]--; A[THREE[4]]--;
vc.PB(3);
}

    while(A[TWO[0]]>0 && A[TWO[1]]>0 && A[TWO[2]]>0 ){
        A[TWO[0]]--; A[TWO[1]]--; A[TWO[2]]--;
vc.PB(2);
    }

    while(A[ONE[0]]>0 && A[ONE[1]]>0 && A[ONE[2]]>0 ){
        A[ONE[0]]--; A[ONE[1]]--; A[ONE[2]]--;
vc.PB(1);
    }

    while(A[NINE[0]]>1 && A[NINE[1]]>0 && A[NINE[2]]>1 && A[NINE[3]]>0 ){
        A[NINE[0]]--; A[NINE[1]]--; A[NINE[2]]--; A[NINE[3]]--;
vc.PB(9);
    }

std::sort (vc.begin(), vc.end() );

FOREACH(it, vc)
    printf("%d", *it);

printf("\n");
}
