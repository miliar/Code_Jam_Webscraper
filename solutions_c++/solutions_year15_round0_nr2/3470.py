#include <iostream>
#include <map>
#include <string> 
#include <vector>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <queue>
#include <tuple>
#include <stack>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

using namespace std;

int cut_time[9][9] = {
    {0,  0,  0,  0,  0,  0,  0,  0,  0},
    {1,  0,  0,  0,  0,  0,  0,  0,  0}, // 2
    {2,  1,  0,  0,  0,  0,  0,  0,  0}, // 3
    {3,  1,  1,  0,  0,  0,  0,  0,  0}, // 4
    {4,  2,  1,  1,  0,  0,  0,  0,  0}, // 5
    {5,  2,  1,  1,  1,  0,  0,  0,  0}, // 6
    {6,  3,  2,  1,  1,  1,  0,  0,  0}, // 7
    {7,  3,  2,  1,  1,  1,  1,  0,  0}, // 8
    {8,  4,  2,  2,  1,  1,  1,  1,  0}, // 9


};

// int cut(vector<int> v) {
//     int minimum = v[v.size() - 1];
//     for (int i = 1; i <= 9; ++i) { //1-9にそろえる
//         int s = 0;
//         for (int vv = 0; vv < v.size(); ++vv) {
//             s += cut_time[v[vv] - 1][i - 1];
//         }
//         // cout << i << ": " << s << endl;
//         minimum = min(minimum, s + i);
//     }
//     return minimum;
// }

int cut(vector<int> v) {
    int minimum = v[v.size() - 1];
    for (int i = 1; i <= v[v.size() - 1]; ++i) { //1-9にそろえる
        int s = 0;
        for (int vv = 0; vv < v.size(); ++vv) {
            s += (v[vv] - 1) / i;
        }
        
        // cout << i << ": " << s << endl;
        minimum = min(minimum, s + i);
    }
    return minimum;
}

int main(int argc, const char * argv[]){
    int n, D;

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> D;
        vector<int> P(D);

        int tmp;
        int sum = 0;
        int maximum = 0;
        for (int j = 0; j < D; ++j) {
            cin >> tmp;
            P[j] = tmp;
            maximum = max(maximum, tmp);
        }
        sort(P.begin(), P.end());
        cout << "Case #" << i+1 << ": " << cut(P) << endl;
        // for (int i = 0; i < P.size(); ++i) {
        //     cout << P[i] << " ";
        // }cout << endl;

    }


    return 0;
}

