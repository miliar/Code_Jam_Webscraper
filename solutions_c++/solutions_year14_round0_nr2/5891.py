#include <iostream>
#include <sstream>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <climits>

using namespace std;

#define FOR(i, b, e)    for(int i = (b), d((e) < (b) ? -1 : 1), n((e) < (b) ? (e) - 1 : (e) + 1); i != n; i += d)
#define REP(i, n)       for(int i = 0; i < (n); i++)
#define DV(v)           for(auto e : (v)){cout << e << " ";} cout << endl
#define PB(e)           push_back((e))
#define CS(v)           cout << "Case #" << (case_num++) << ": " << (v) << endl
#define ALL(e)          (e).begin(), (e).end()
#define SZ              size()

typedef stringstream        SS;
typedef vector<int>         VI;
typedef pair<int, int>      PII;
typedef vector<string>      VS;
typedef map<string, int>    MSI;

template <class T>
inline string toStr(const T& i){
    ostringstream os("");
    os << i; 
    return os.str(); 
}

int case_num = 1;

void main_(){
    double C, F, X, best, cur_t, cur_f;
    cin >> C >> F >> X;
    best = X / 2.0;
    cur_f = 2.0;
    cur_t = 0.0;
    for(int i = 0; ; i++){
        double ov;
        cur_t += C / cur_f;
        cur_f += F;
        if(cur_t + X / cur_f < best) best = cur_t + X / cur_f;
        else break;
    }
    printf("Case #%d: %.7lf\n", case_num++, best);
}

int main(int argc, char *argv[]){
    int T;
    cin >> T;
    REP(t, T) main_();
    return 0;
}
