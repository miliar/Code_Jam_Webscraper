#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int INF = 1000000000;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define rep(i,n) REP(i, 0, n)
map<vector<int>, int> ans;
int main(){
    ifstream ifs("B-large.in");
    ofstream ofs("op_b2.txt");
    vector<int> temp; temp.push_back(0);
    ans[temp] = 1;
    rep(i, 100){
        int num = temp[i];
        num ^= 1;
        temp.push_back(num);
        int ts = temp.size();
        ans[temp] = ts % 2 ? ts : ts - 1;
    }
    temp.clear(); temp.push_back(1);
    ans[temp] = 0;
    rep(i, 100){
        int num = temp[i];
        num ^= 1;
        temp.push_back(num);
        int ts = temp.size();
        ans[temp] = ts % 2 ? ts - 1 : ts;
    }
    int test; ifs >> test;
    rep(casenum, test){
        vector<int> cake;
        string s; ifs >> s;
        int n = s.length();
        cake.push_back((s[0] == '+')? 1 : 0);
        rep(i, n - 1){
            int num = cake[cake.size() - 1]; num ^= 1;
            if(s[i + 1] != s[i]) cake.push_back(num);
        }
        ofs << "Case #" << casenum + 1
            << ": " << ans[cake] << endl;
    }
    return 0;
}