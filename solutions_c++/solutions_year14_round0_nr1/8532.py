// Dark Side of Elephant
// Askar

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <cstring>
#include <algorithm>
#include <utility>
#include <tuple>
#include <complex>
#include <cmath>

using namespace std;

#define FOR(i, N) for(auto i=(N)-(N); i<(N); ++i)
#define FOR1(i, N) for(auto i=(N)-(N)+1; i<=(N); ++i)
#define FOREACH(it, a) for(auto it=(a).begin(); it!=(a).end(); ++it)
#define MAXIM(a,b) a=max(a, static_cast<__typeof__(a)>(b))
#define MINIM(a,b) a=min(a, static_cast<__typeof__(a)>(b))
#define beginend(a) (a).begin(), (a).end()
#define pf printf
#define sf scanf
#define mp make_pair
#define mt make_tuple
#define pass
#define sqr(x) (x)*(x)
typedef long long ll;
typedef pair<long long, long long> pll;
typedef pair<int, int> pii;
const long long INF = 1e9;
const double EPS = 1e-9;

#define dbg if(false)
#ifdef EBUG
    #undef dbg
    #define dbg if(true)
#endif

#define epf(...) fprintf(stderr, __VA_ARGS__)
#define dpf(...) dbg epf(__VA_ARGS__)
#define db(x) dbg cerr << #x << ":\t" << (x) << endl 
#define assert(x, ...) if(!(x)){                                \
epf("L: %i, F: %s: (%s) failed!\n", __LINE__, __FUNCTION__, #x);\
error_exit(__VA_ARGS__);                                        \
}
const int WA = 0;
const int EXC = 1;
const int TLE = 2;
void error_exit(const int exit_type=WA){
    switch(exit_type){
        case WA: epf("\nWe want WA!\n"); exit(0); break; 
        case EXC: exit(47); break;
        case TLE: while(true); break;
    }
}


int main(){
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; t++){
        int ans1, ans2;
        set<int> row1, row2;
        
        cin >> ans1;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                int x;
                cin >> x;
                if(i+1 == ans1){row1.insert(x);}
            }
        }
        
        cin >> ans2;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                int x;
                cin >> x;
                if(i+1 == ans2){row2.insert(x);}
            }
        }

        set<int> intersection;
        FOREACH(it, row1) if(row2.find(*it) != row2.end()) intersection.insert(*it);
        
        cout << "Case #" << t << ": ";
        if(intersection.size() == 1){
            cout << *intersection.begin();
        }
        else if(intersection.size() == 0){
            cout << "Volunteer cheated!";
        }
        else{
            cout << "Bad magician!";
        }

        cout << endl;
    }
}
