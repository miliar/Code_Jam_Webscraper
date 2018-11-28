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
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<"";s<<P[i];}return s<<" }"<<endl;}
template<class T1, class T2> ostream& operator<<(ostream &s, map<T1,T2> P) {s<<"{ ";for(typeof(P.begin()) it=P.begin();it!=P.end();++it){if(it!=P.begin())s<<", ";s<<'<'<<it->first<<"->"<<it->second<<'>';}return s<<" }"<<endl;}



int main() {
    freopen( "/Users/macuser/Documents/Programming/Contest/B-large.in", "r", stdin );
    freopen( "/Users/macuser/Documents/Programming/Contest/BL.txt", "w", stdout );

    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        int N,M;
        cin >> N >> M;
        vector<vint> lawn(N, vint(M));
        for (int i = 0; i < N; ++i) for (int j = 0; j < M; ++j) cin >> lawn[i][j];
                
        //COUT(lawn);
        
        bool can = true;
        for (int h = 1; h <= 100; ++h) {
            vector<vector<bool> > field(N, vector<bool>(M, 0)), temp(N, vector<bool>(M, 0));
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < M; ++j) {
                    if (lawn[i][j] <= h) field[i][j] = 1;
                }
            }
            
            for (int i = 0; i < N; ++i) {
                bool comp = true;
                for (int j = 0; j < M; ++j) {
                    if (!field[i][j]) comp = false;
                }
                if (comp) {
                    for (int j = 0; j < M; ++j) temp[i][j] = 1;
                }
            }
            for (int j = 0; j < M; ++j) {
                bool comp = true;
                for (int i = 0; i < N; ++i) {
                    if (!field[i][j]) comp = false;
                }
                if (comp) {
                    for (int i = 0; i < N; ++i) temp[i][j] = 1;
                }
            }
            
//            if (h <= 1) {
//            cout << h << " : " << endl;
//            cout << field;
//            cout << temp;
//            }
            
            if (temp != field) {can = false; break;}
        }

        printf("Case #%d: ", id);
        
        if (can) printf("YES");
        else printf("NO");
        
        printf("\n");
    }
    
    return 0;
}




