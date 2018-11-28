#include<iostream>
#include<vector>

using namespace std;

void solve(int testcase){
    int N, M; cin >> N >> M;
    vector<vector<int> > board = vector<vector<int> >(N, vector<int>(M));
    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            cin >> board[i][j];
        }
    }
    vector<vector<int> > lawn = vector<vector<int> >(N, vector<int>(M,100));
    for(int i=0; i<N; ++i){
        int maxval = 0;
        for(int j=0; j<M; ++j){
            maxval = board[i][j]>maxval? board[i][j]: maxval;
        }
        for(int j=0; j<M; ++j){
            lawn[i][j] = maxval;
        }
    }
    for(int i=0; i<M; ++i){
        int maxval = 0;
        for(int j=0; j<N; ++j){
            maxval = board[j][i]>maxval? board[j][i]: maxval;
        }
        for(int j=0; j<N; ++j){
            lawn[j][i] = lawn[j][i]>maxval? maxval: lawn[j][i];
        }
    }

    bool possible = true;
    for(int i=0; i<N && possible; ++i){
        for(int j=0; j<M && possible; ++j){
            if(board[i][j] != lawn[i][j]){
                possible = false;
            }
        }
    }
    cout << "Case #"<<testcase<<": ";
    if(possible){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    return;
}

int main(){
    int T; cin >> T;
    for(int i=0; i<T; ++i){
        solve(i+1);
    }
    return 0;
}
