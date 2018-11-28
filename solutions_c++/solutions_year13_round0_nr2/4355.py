#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int N,M;

int grid[100][100];


int row_maxes[100];
int col_maxes[100];

void solve(){
    for(int i=0;i<100;i++){
        row_maxes[i] = 0;
        col_maxes[i] = 0;
    }
    for(int r=0;r<N;r++){
        for(int c=0;c<M;c++){
            row_maxes[r] = max(row_maxes[r],grid[r][c]);
            col_maxes[c] = max(col_maxes[c],grid[r][c]);
        }
    }
    for(int r=0;r<N;r++){
        for(int c=0;c<M;c++){
            if(grid[r][c]<row_maxes[r] && grid[r][c]<col_maxes[c]){
                //impossible config
                printf("NO\n");
                return;
            }
        }
    }
    printf("YES\n");
    return;
}

int main(){
    int T;
    cin >> T;
    for(int k=0;k<T;k++){
        cin >> N >> M;
        for(int r=0;r<N;r++){
            for(int c=0;c<M;c++){
                cin >> grid[r][c];
            }
        }
        printf("Case #%d: ",k+1);
        solve();
    }
}
