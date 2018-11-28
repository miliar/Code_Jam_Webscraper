#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <tuple>
#include <cmath>
#include <climits>
using namespace std;

#define SORT(l) std::sort(l.begin(), l.end())
#define IS_ALPH(c) ((c>='a' && c<='z') || (c>='A' && c<='Z'))
#define IS_NUM(c) (c>='0' && c<='9')
#define FOR(a, min, max) for(int a=min; a<max; ++a)
#define FORS(a, str) for(int a=0; a<str.length(); ++a)
#define FORV(a, vec) for(int a=0; a<vec.size(); ++a)
#define MAX(a, b) ((a > b) ? (a) : (b))
#define MIN(a, b) ((a < b) ? (a) : (b))
#define COUTV(v) FORV(i,v) { cout << v[i]; if(i<v.size()-1) cout << ","; else cout << endl; }

int main() {
    
    int T;
    cin >> T;
    int cur_case=1;
    while(T--) {
        
        int smax;
        cin >> smax;

        string levels;
        cin >> levels;
        int cur_total=0;
        int num_added=0;
        for(int i=0; i<levels.length(); ++i) {
            if(i<=cur_total) {
                cur_total += levels[i]-'0';
            }else {
                num_added += i-cur_total;
                cur_total += (i-cur_total) + (levels[i]-'0');
            }
        }

        cout << "Case #" << cur_case++ << ": " << num_added << endl;
    }

    return 0;
}
