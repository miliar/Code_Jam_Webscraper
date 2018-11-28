#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<climits>
#include<cfloat>
using namespace std;

const double PI = std::atan(1.0)*4;

int main(int argc, char *argv[]){
    int T;
    cin >>T;
    int lawn[100][100], rows[100],cols[100];
    for(int t=1;t<=T; ++t){
        cout << "Case #"<<t<<": ";
        int n,m;
        cin >> n >> m;
        /* read de lawn */
        for(int j=0;j<m;++j){
            cols[j] = INT_MIN;
        }
        for(int i=0;i<n;++i){
            rows[i] = INT_MIN;
            for(int j=0;j<m;++j){
                cin >> lawn[i][j];
                if(lawn[i][j] > rows[i])
                    rows[i] = lawn[i][j];
                if(lawn[i][j] > cols[j])
                    cols[j] = lawn[i][j];
            }
        }

        bool possible = true;
        for(int i=0;i<n && possible;++i){
            for(int j=0;j<m && possible;++j){
                if(!(lawn[i][j] == rows[i] || lawn[i][j] == cols[j])){
                    possible = false;
                    cout << "NO" <<endl;
                }
            }
        }
        if(possible)
            cout << "YES" << endl;

     }
    return EXIT_SUCCESS;    
}

