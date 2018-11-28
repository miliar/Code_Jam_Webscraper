#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <string.h>
#include <strings.h>
#include <math.h>

//#include <ctime.h>
#include <time.h>

using namespace std;

//Two of the most frequently used typical of long names, make life easier
typedef vector<int> VI;
typedef long long LL;

/* HEADERS */
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
/* Shortcuts */
#define PB push_back
#define ST first()
#define ND second()
#define LT back()

//int count_standing(string ovations);
int fast_sol(int total, string s);

int main() {

    int TT; cin >> TT;

    REP(t, TT){
        cout << "Case #" << t+1 << ": " ;
        int n; cin>>n;
        string s;
        cin >> s;
        int r = fast_sol(n, s);

        cout << r << endl;

    }



}

int fast_sol(int total, string s){
    int result = 0, cnt=0;

    for(int i=0; i<s.size()-1; i++){
        int n_i = s[i]-48;

        if(n_i+cnt > i){
            cnt+=n_i;
        } else {
            cnt++;
            result++;
        }
    }

    return result;
}


