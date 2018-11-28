#include <iostream>
#include <stack>
#include <queue>
#include <bitset>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
using namespace std;

/*
 
 */

map<map<int, int>, int > h;


int dfs(map<int, int> mp) {
    map<int, int> ::iterator it ;
    bool canret = true;
    for (it = mp.begin(); it != mp.end(); it++) {
        if (it->second != 0) {
            canret = false;
            break;
        }
    }
    if (mp.empty() || canret) return 0;
    else {
        if (h.find(mp) != h.end()) return h[mp];
        int minstep = INT_MAX;
        map<int, int> newmp;
        for (it = mp.begin(); it != mp.end(); it++) {
            if (it->first < 2) continue;
            newmp[it->first - 1] = it->second;
        }
        
        if (h.find(newmp) == h.end()) {
            h[newmp] = dfs(newmp);
        }
//        cout << "-------------------------------------" << endl;
//        for (it = newmp.begin(); it != newmp.end(); it++) {
//            cout << it->first << " " << it->second << " ";
//        }
//        cout <<endl;
//        cout << h[newmp] << endl;
//        cout << "-------------------------------------" << endl;
        
        minstep = min(h[newmp], minstep);
        
        // lift
        // if exist mp[2...] > 1 lift
        bool exist = 0;

        for (it = mp.begin(); it != mp.end(); it++) {
            if (it->first >= 2) {
                exist = 1;
                break;
            }
        }
        if (!exist) return 1;
        
        for (it = mp.begin(); it != mp.end(); it++) {
            if (it->first < 2 || it->second < 1) continue;
            // lift it->first to a, b
            for (int i = 1; i < it->first; i++) {
                int a = i, b = it->first - i;
                it->second--;
                mp[a]++;
                mp[b]++;
                if (h.find(mp) == h.end()){
                    h[mp] = dfs(mp);
                }
                minstep = min(h[mp], minstep);

                mp[a]--;
                mp[b]--;
                it->second++;
            }
        }
        
        return minstep + 1;
    }
}



int run() {
    int d;
    cin >> d;
    vector<int> v;
    map<int, int> m;
    for (int i = 0; i < d; i++) {
        int t;
        cin >> t;
        m[t]++;
    }
    
    return dfs(m);
}

int main(int argc, char *argv[]) {
    	freopen("B-small-attempt2.in","r",stdin);
    	freopen("2.out","w",stdout);
    int t;
    cin >> t;
    int k = 0;
    while (t--) {
        cout << "Case #" << ++k << ": " << run() << endl;
    }
    return 0;
}

/*
 1 6
 5 5 5 9 9 9
 */