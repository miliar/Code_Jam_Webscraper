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

void output(int testcase, long long int N) {
    cout << "Case #" << testcase << ": ";
    if (N == -1) {
        cout << "INSOMNIA" << endl;
        return;
    }
    cout << N << endl;
}

int main(int argc, char const *argv[]) {
    int T;
    cin >> T;
    for (int testcase = 0; testcase < T; ++testcase) {
        long long int N;
        cin >> N;
        if (N == 0) {
            output(testcase + 1, -1);
            continue;
        }
        bool digits[10];
        for (int i = 0; i < 10; ++i) {
            digits[i] = false;
        }
        int count = 0;
        long long int now = N;
        while(count != 10) {
            string s = to_string(now);
            for(int j = 0; j < s.size(); j++) {
                if (!digits[s[j] - '0']) {
                    count++;
                    digits[s[j] - '0'] = true;
                }
            }
            now += N;
        }
        output(testcase + 1, now - N);
    }
    return 0;
}