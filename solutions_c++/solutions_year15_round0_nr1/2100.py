#include <algorithm>
#include <assert.h>
#include <climits> 
#include <cmath>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define pb push_back
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second 
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c)) 

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> VI; 

int main(int argc, char const *argv[]) {

    #ifndef ONLINE_JUDGE
    freopen("input.txt","r", stdin);
    freopen("output_large.txt","w",stdout);
    #endif

    int T; cin>>T;

    REP(t,T) {
        int n; string s;
        cin>>n>>s;
        int total = 0, added = 0;
        REP(i,s.size()) {
            if (total<i) {
                added += i-total;
                total = i;
            }
            total += int(s[i]) - int('0');
        }
        cout<<"Case #"<<t+1<<": "<<added<<endl;
    }

    return 0;
}