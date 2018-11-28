#include<iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    
    for(int i=0; i<T; i++){
        int N, M;
        cin >> N >> M;
        
        float board[100][100];
        int minrow[100]; 
        int mincol[100];
        for(int j=0; j<N; j++){
            minrow[j] = 0; 
        }
        for(int k=0; k<M; k++){
            mincol[k] = 0;
        }       
        for(int j=0; j<N; j++){
            for(int k=0; k<M; k++){
                cin >> board[j][k];
                
                if (board[j][k] >= minrow[j]){
                    minrow[j] = board[j][k];
                }                
                if (board[j][k] >= mincol[k]){
                    mincol[k] = board[j][k];
                }
            }       
        } 

        int success = 1;        
        for(int j=0; j<N; j++){
            for(int k=0; k<M; k++){
                int min = (minrow[j] < mincol[k])? minrow[j] : mincol[k];
                if (board[j][k] != min){
                    success = 0;
                    break;
                }
            }
            if(success==0) break;
        }
        if(success==0) cout << "Case #" << i+1 << ": " << "NO" << endl;
        else cout << "Case #" << i+1 << ": " << "YES" << endl;
    }
}
