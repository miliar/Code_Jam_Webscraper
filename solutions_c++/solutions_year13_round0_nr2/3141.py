#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> frow, fcol;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int t;
    int grid[100][100];
    scanf("%d", &t);
    for ( int i = 0; i < t; i++ ) {
        int a, b;
        scanf("%d%d", &a, &b);
        for ( int j = 0; j < a; j++ ) {
            for ( int k = 0; k < b; k++ ) {
                scanf("%d", &grid[j][k]);
                //printf("%d ", grid[j][k]);
            }
            //printf("\n");
        }
        for ( int l = 1; l <= 100; l++ ) {
            frow.clear();
            fcol.clear();
            for ( int j = 0; j < a; j++ ) {
                bool filled = true;
                for ( int k = 0; k < b; k++ ) {
                    if ( grid[j][k] > l ) {
                       filled = false;
                    }
                }
                if ( filled ) frow.push_back(j);
            }
            for ( int k = 0; k < b; k++ ) {
                bool filled = true;
                for ( int j = 0; j < a; j++ ) {
                    if ( grid[j][k] > l ) filled = false;
                }
                if ( filled ) fcol.push_back(k);
            }
            frow.push_back(1000000);
            fcol.push_back(1000000);
            //for ( int j = 0; j < frow.size(); j++ ) printf("%d\n", frow[j]);
            //for ( int j = 0; j < fcol.size(); j++ ) printf("%d\n", fcol[j]);
            for ( int j = 0; j < a; j++ ) {
                for ( int k = 0; k < b; k++ ) {
                    if ( grid[j][k] <= l && *(lower_bound(frow.begin(), frow.end(), j)) != j && *(lower_bound(fcol.begin(), fcol.end(), k)) != k ) {
                       printf("Case #%d: NO\n", i+1);
                       goto restart;
                    }      
                }
            }
        }
        printf("Case #%d: YES\n", i+1);
        restart:
                continue;
    }
    return 0;
}
