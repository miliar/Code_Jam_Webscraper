#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define in "in.txt"
#define out "out.txt"

bool check_lawn(vector< vector<int> > &lawn,
                vector< int > &l_mins,
                vector< int > &l_maxs,
                vector< int > &c_mins,
                vector< int > &c_maxs) {
    int n = lawn.size();
    int m = lawn[0].size();

    for(int i=0; i<n; i++) {
        if(l_mins[i]!=l_maxs[i])
        for(int j=0; j<m; j++) {
            if(lawn[i][j]==l_mins[i]) {
                if(lawn[i][j] < c_maxs[j])
                    return false;
            }
        }
    }
    return true;
}

int main() {
    int cases;
    int n;
    int m;
    freopen(in, "r", stdin);
    freopen(out, "w", stdout);
    cin >> cases;
    vector< vector<int> > lawn;
    vector< int > line_mins, line_maxs, cols_mins, cols_maxs;
    for(int case_number=1; case_number<=cases; case_number++) {
        cout << "Case #" << case_number << ": ";

        cin >> n >> m;
        lawn.resize(n, vector<int>(m, 0));
        line_mins.resize(n, 100);
        cols_mins.resize(m, 100);
        line_maxs.resize(n, 0);
        cols_maxs.resize(m, 0);
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++){
                cin >> lawn[i][j];
                cols_mins[j] = min(lawn[i][j], cols_mins[j]);
                cols_maxs[j] = max(lawn[i][j], cols_maxs[j]);
            }
            line_mins[i] = *min_element(lawn[i].begin(), lawn[i].end());
            line_maxs[i] = *max_element(lawn[i].begin(), lawn[i].end());
        }
        if(check_lawn(lawn, line_mins, line_maxs, cols_mins, cols_maxs))
            cout << "YES\n";
        else
            cout << "NO\n";

        lawn.clear(); 
        line_mins.clear(); 
        line_maxs.clear(); 
        cols_mins.clear(); 
        cols_maxs.clear();
    }

    return 0;
}