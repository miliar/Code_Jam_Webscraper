#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
using namespace std;
int dest[101][101], source[101][101];
int main() {
    int t;
    cin>>t;
    for(int Kases = 1 ; Kases <= t ; ++Kases) {
        cout<<"Case #" << Kases << ": ";
        int n, m;
        bool evaluated = false;
        cin>>n>>m;
        for(int i = 0 ; i < n ; i++) {
            for(int j = 0 ; j < m ; j++) {
                cin>>dest[i][j];
                source[i][j] = 100;
            }
        }
        int times = 0;
        while(times++ < 1000) {
            for(int i = 0 ; i < n ; i++) {
                int maxInRow = 0;
                for(int j = 0 ; j < m ; j++) {
                    maxInRow = max(maxInRow, dest[i][j]);
                }
                for(int j = 0 ; j < m ; j++) {
                    source[i][j] = min(maxInRow, source[i][j]);
                }
            }
            for(int i = 0 ; i < m ; i++) {
                int maxInColumn = 0;
                for(int j = 0 ; j < n ; j++) {
                    maxInColumn = max(maxInColumn, dest[j][i]);
                }
                for(int j = 0 ; j < n ; j++) {
                    source[j][i] = min(maxInColumn, source[j][i]);
                }
            }
        }
        for(int i = 0 ; !evaluated && i < n ; i++) {
            for(int j = 0 ; !evaluated && j < m ; j++) {
                if(source[i][j] != dest[i][j]) {
                    evaluated = true;
                    cout<<"NO\n";
                }
            }
        }
        if( !evaluated ) {
            cout<<"YES\n";
        }
    }
    return 0;
}
