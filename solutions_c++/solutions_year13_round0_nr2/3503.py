#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
using namespace std;
int main(int argc, char *argv[]){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test_count; cin >> test_count;
    for(int test = 0; test < test_count; ++test){
        int n, m; cin >> n >> m;
        //cout << "[" << n << "x" << m << "]" << endl;

        vector<vector<int> > a(n, vector<int>(m));
        vector<int> rowmax(n, 1), colmax(m, 1);
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                 cin >> a[i][j];
                 rowmax[i] = max(rowmax[i], a[i][j]);
                 colmax[j] = max(colmax[j], a[i][j]);
            }
        }
        bool fail = false;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                fail |= a[i][j] != rowmax[i] && a[i][j] != colmax[j];
            }
        }

        cout << "Case #" << (test + 1) << ": ";
        if(!fail){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
    return 0;
}