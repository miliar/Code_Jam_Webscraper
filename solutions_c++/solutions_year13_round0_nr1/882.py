#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<ll> vll;
typedef pair<int,int> pint;

#define DE 1
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ALL(s) (s).begin(),(s).end()
#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define EACH(i,s) for (typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define COUT(x) cout<<#x<<" = "<<(x)<<" (L"<<__LINE__<<")"<<endl

template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T1, class T2> ostream& operator<<(ostream &s, map<T1,T2> P) {s<<"{ ";for(typeof(P.begin()) it=P.begin();it!=P.end();++it){if(it!=P.begin())s<<", ";s<<'<'<<it->first<<"->"<<it->second<<'>';}return s<<" }"<<endl;}



int main() {
    freopen( "/Users/macuser/Documents/Programming/Contest/A-large.in", "r", stdin );
    freopen( "/Users/macuser/Documents/Programming/Contest/AL.txt", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        vector<string> ini(4);
        string str;
        for (int i = 0; i < 4; ++i) {
            cin >> str; ini[i] = str;
        }
        
        bool isend = true, isX = false, isO = false, excX, excO;
        for (int i = 0; i < 4; ++i) 
            for (int j = 0; j < 4; ++j) 
                if (ini[i][j] == '.') isend = false;

        for (int i = 0; i < 4; ++i) {
            excX = false, excO = false;
            for (int j = 0; j < 4; ++j) {
                if (ini[i][j] != 'X' && ini[i][j] != 'T') excX = true;
                if (ini[i][j] != 'O' && ini[i][j] != 'T') excO = true;
            }
            if (!excX) isX = true;
            if (!excO) isO = true;
            
            excX = false, excO = false;
            for (int j = 0; j < 4; ++j) {
                if (ini[j][i] != 'X' && ini[j][i] != 'T') excX = true;
                if (ini[j][i] != 'O' && ini[j][i] != 'T') excO = true;
            }
            if (!excX) isX = true;
            if (!excO) isO = true;
        }
        
        excX = false, excO = false;
        for (int i = 0; i < 4; ++i) {
            if (ini[i][i] != 'X' && ini[i][i] != 'T') excX = true;
            if (ini[i][i] != 'O' && ini[i][i] != 'T') excO = true;
        }
        if (!excX) isX = true;
        if (!excO) isO = true;
            
        excX = false, excO = false;
        for (int i = 0; i < 4; ++i) {
            if (ini[i][3-i] != 'X' && ini[i][3-i] != 'T') excX = true;
            if (ini[i][3-i] != 'O' && ini[i][3-i] != 'T') excO = true;
        }
        if (!excX) isX = true;
        if (!excO) isO = true;
        
        
        printf("Case #%d: ", id);
        
        if (isX) printf("X won");
        else if (isO) printf("O won");
        else if (isend) printf("Draw");
        else printf("Game has not completed");
        
        printf("\n");
    }
    
    return 0;
}




