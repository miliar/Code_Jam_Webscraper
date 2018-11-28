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

int min_minutes = INT_MAX;

void search(vector<int> &values, int cur_minute) {
    //for(int i=0; i<values.size(); ++i) {
    //    cout << values[i] << " ";
    //}
    //cout << endl;

    //cout << "current minute: " << cur_minute << endl;

    int max_index=0;
    for(int i=0; i<values.size(); ++i) {
        if(values[i]>values[max_index])
            max_index=i;
    }

    if(values[max_index]<=3) {
        min_minutes = min(min_minutes, cur_minute + values[max_index]);
        return;
    }

    //try removing 3+ items
    for(int i=2; i<=values[max_index]/2; ++i) {
        int cur = values[max_index];
        values[max_index]-=i;
        values.push_back(i);
        search(values, cur_minute+1);
        values.pop_back();
        values[max_index]=cur;
    }

    //try simply progressing
    for(int i=0; i<values.size(); ++i) {
        values[i]--;
    }
    search(values, cur_minute+1);
    for(int i=0; i<values.size(); ++i) {
        values[i]++;
    }
}

int main() {
    
    int T;
    cin >> T;
    int cur_case = 1;
    while(T--) { 
        
        int plates;
        cin >> plates;
        vector<int> food(plates);
        for(int i=0; i<plates; ++i) {
            cin >> food[i];
        }

        min_minutes = INT_MAX;
        search(food, 0);
        cout << "Case #" << cur_case++ << ": " << min_minutes << endl;
    }

    return 0;
}
