#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <ostream>
using namespace std;

bool pal(string s){
    string r(s);
    reverse(s.begin(), s.end());
    return s == r;
}
const int LIMIT = 10 * 1000 * 10;

vector<long long> memo;
void precalc(){
    for(int i = 1; ; ++i){
        if (i % 1000 * 1000 == 0) cerr << 100 * i / LIMIT << " ";

        bool ok = false;
        ostringstream out;
        out << i;
        if ( pal(out.str())){
            long long sq = i;
            sq = sq * sq;
            ostringstream oss;
            oss << sq;
            if(pal(oss.str())){
                memo.push_back(sq);
                ok = true;
            }
        }
        if(i > LIMIT && ok) break;
    }
}
int main(int argc, char *argv[]){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    precalc();
    cerr << "go!!" << endl;

    int test_count; cin >> test_count;
    for(int test = 0; test < test_count; ++test){
        int A, B; cin >> A >> B;
        int ans = 0;
        for(int i  = 0; i < memo.size(); ++i)
            if(memo[i] >= A && memo[i] <= B) ++ans;
        //vector<long long>::iterator pa = lower_bound(memo.begin(), memo.end(), A),
        //    pb = lower_bound(memo.begin(), memo.end(), B);
        //if(*pb > B && pb > pa) --pb;
        cout << "Case #" << (test + 1) << ": ";
        cout << ans << endl;
        //if(pa == pb)
        //    cout << 0 << endl;
        //else
        //    cout << (pb - pa + 1) << endl;
    }
    return 0;
}