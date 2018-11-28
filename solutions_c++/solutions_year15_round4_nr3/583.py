#include <cstdio>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <complex>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector<vector<int> > graph;
const int INF = 1000000000;
const ll MOD = 1000000009;
#define FILEIN "C.in"
#define FILEOUT "C.out"



int main(){
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_){
    	
        
        int N;
        cin >> N;
        string tmp;
        getline(cin, tmp);
        string s[N];
        vector<vector<string> > strs(N);


        for (int i = 0; i < N; ++i) {
            getline(cin, s[i]);
            string ss = "";
            for (int j =0; j < s[i].length(); ++j) {
                if (s[i][j] == ' ') {
                    if (!ss.empty())
                        strs[i].push_back(ss);
                    ss = "";
                } else {
                    ss += s[i][j];
                }
                
            }
            if (!ss.empty()) {
                    strs[i].push_back(ss);
                }
        }

        map<string, int> caches;
        vector<vector<int> > nums(N);
        int l = 0;
        for (int i = 0; i < strs.size(); ++i) {
            for (int j =0; j < strs[i].size(); ++j) {
                if (caches.find(strs[i][j]) != caches.end()) {
                    nums[i].pb(caches[strs[i][j]]);
                } else {
                    l++;
                    nums[i].pb(l);
                    caches[strs[i][j]] = l;
                }
            }
        }
        int mincommon = 1000000000;
        int com = 0;
        set<int> s1;
        set<int> s2;
        

        for (int i = 0; i < nums[0].size(); ++i) {
                s1.insert(nums[0][i]);
            }
            for (int i =0; i < nums[1].size(); ++i) {
                s2.insert(nums[1][i]);
            }
        for (set<int>::iterator it = s1.begin(); it != s1.end(); ++it) {

                if (s2.find(*it) != s2.end()) {
                    ++com;
                }
            }
        for (int mask = 0; mask < (1<<(N-2)); ++mask) {
            // cout << mask << endl;
            int m[N-2];
            int tmp = mask;
            for(int j = 0; j < N-2; ++j) {
                m[j] = tmp % 2;
                tmp >>= 1;
            }
            set<int> w1;
            set<int> w2;
            
            for (int i = 0; i < N-2; ++i) {
                // cout << N -2 << endl;
                if (m[i] == 0) {
                    for (int j = 0; j < nums[i+2].size(); ++j) {
                        if (s1.find(nums[i+2][j]) == s1.end()) {


                           w1.insert(nums[i+2][j]);
                        }
                        // cout << strs[i+2][j] << endl;
                    }
                } else {
                    for (int j = 0; j < nums[i+2].size(); ++j) {
                        if (s2.find(nums[i+2][j]) == s2.end()) {


                           w2.insert(nums[i+2][j]);
                        }
                        // cout << strs[i+2][j] << endl;
                    }
                }
            }
            int cnt = 0;
            // cout << mask << endl;
            for (set<int>::iterator it = w1.begin(); it != w1.end(); ++it) {

                if (w2.find(*it) != w2.end() || s2.find(*it) != s2.end()) {
                    ++cnt;
                }
            }
            for (set<int>::iterator it = w2.begin(); it != w2.end(); ++it) {
                if (s1.find(*it) != s1.end()) {
                    ++cnt;
                }
            }
            
            mincommon = min(cnt + com, mincommon);
        }


        cout << "Case #" << _ << ": ";
        //Output answer 
        cout << mincommon;
        // cout << mincommon - com << endl;
        
        cout << endl;
    }
    return 0;
}