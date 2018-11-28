#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int a[100][100];
int max_row[100];
int max_col[100];
int M, N;
void init(int m, int n){
    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++){
            cin >> a[i][j];
        }
}

bool process(){
    for(int i = 0; i < M; i++)
        for(int j = 0; j < N; j++)
            if(a[i][j] < 0 || a[i][j] > 100)
                return false;

    for(int i = 0; i < M; i++){
        max_row[i] = 0;
        for(int j = 0; j  < N ; j++){
            max_row[i] = max(max_row[i], a[i][j]);
        }
    }


    for(int j = 0; j < N; j++){
        max_col[j] = 0;
        for(int i = 0; i < M; i++){
            max_col[j] = max(max_col[j], a[i][j]);
        }
    }

    for(int i = 0; i < M; i++)
        for(int j = 0; j < N; j++){
            if(a[i][j] < min(max_row[i], max_col[j]))
                return false;
        }
    return true;
}

int main(){
    int T;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    for(int ti = 0; ti < T; ti++){
        cin >> M >> N;
        init(M, N);
        bool res = process();
        if(res == true)
            cout << "Case #" << ti +1 << ": YES" << endl;
        else
            cout << "Case #" << ti +1 << ": NO" << endl;
    }
    return 0;
}
