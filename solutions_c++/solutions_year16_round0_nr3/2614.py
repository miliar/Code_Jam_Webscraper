#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
 
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define _D(p) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p)<<std::endl;
#define _D2(p,q) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p) << ", " #q " = "<<(q)<<std::endl;
#define _DN(v) std::cout<<"L"<<__LINE__<<" : " #v " = ["; rep(i,(v).size()) {std::cout<<v[i]<<(i==v.size()-1?"":", ");}std::cout<<"]"<<std::endl;
#define _DNN(v) std::cout<<"L"<<__LINE__<<" : " #v " = [" << std::endl; rep(i,(v).size()) {std::cout<<"    [";rep(j,(v)[0].size()){std::cout<<v[i][j]<<(j==v[0].size()-1?"":", ");}std::cout<<"],"<<std::endl;}std::cout<<"]"<<std::endl;
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

string base2(long long int i) {
    string ret = "";
    while(i > 0) {
        ret += (i & 1) ? "1" : "0";
        i >>= 1;
    }
    reverse(all(ret));
    return ret;
}


long long int nontrivial(long long int N) {
    if (!(N & 1)) return 2;
    for (long long int i = 3; i * i <= N; i += 2) {
        if (N % i == 0) {
            return i;
        }
    }
    return -1;
}

vector<long long int> checkJam(string s) {
    vector<long long int> ans;
    //cout << "check: " << s << endl;
    for (int b = 2; b <= 10; ++b) {
        long long int N = 0;
        long long int nowb = 1;
        for (int j = s.size() - 1; j >= 0; --j) {
            if (s[j] == '1') {
                N += nowb;
            }
            nowb *= b;
        }
        //cout << "debug" << b << ": " << N << endl;
        long long int d = nontrivial(N);
        //cout << "ret : " << d << endl;
        if (d == -1) {
            vector<long long int> pr;
            pr.push_back(-1);
            return pr;
        }
        ans.push_back(d);
    }
    return ans;
}

int main(int argc, char const *argv[]) {
    int T;
    cin >> T;
    long long int N, J;
    cin >> N >> J;
    long long int count = 0;
    cout << "Case #1:" << endl;
    for(long long int i = (((long long int)1) << (N - 1)) + 1; i < ((long long int)1) << N; i+=2) {
        string s = base2(i);
        //cout << s << endl;
        vector<long long int> ret = checkJam(s);
        if (ret[0] == -1) continue;
        
        cout << s << " ";
        for(int j = 0; j < ret.size(); j++) {
            cout << ret[j];
            if (j != ret.size() - 1) {
                cout << " ";
            }
        }
        cout << endl;

        count++;
        if (count >= J) break;
    }
    return 0;
}