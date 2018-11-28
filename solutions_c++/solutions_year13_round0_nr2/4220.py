#include <iostream>
#include <string>
#include <sstream>
#include <utility>
#include <climits>
#include <vector>
#include <iterator>
#include <cctype>
#include <stack>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 0 ; t < T; ++t){
        cout << "Case #" << (t+1) << ": ";
        int N, M;
        cin >> N;
        cin >> M;
        
        vector<vector<int> > lawn(N, vector<int>(M, 0));
        
        for(int i = 0; i < N; ++i){
                for(int j = 0; j < M; ++j){
                        cin >> lawn[i][j];
                }
        } 
        vector<vector<int> > processed(N, vector<int>(M, 100));
        int max;
        for(int i = 0; i < N; ++i){
                max = lawn[i][0];        
                for(int j = 1; j < M; ++j){                   
                        if(max < lawn[i][j]) {
                               max = lawn[i][j];
                        }
                }                
                for(int j = 0; j < M; ++j){
                  if(processed[i][j] > max) processed[i][j] = max;
                }
        }
        for(int i = 0; i < M; ++i){                 
                max = lawn[0][i];        
                for(int j = 1; j < N; ++j){                   
                        if(max < lawn[j][i]) {
                              max = lawn[j][i];
                        }
                }               
                for(int j = 0; j < N; ++j){
                 if(processed[j][i] > max) processed[j][i] = max;
                }
                
        }
        bool isPossible = true;   
	    for(int i = 0; i < N; ++i){
                for(int j = 0; j < M; ++j){  
                        if(processed[i][j] != lawn[i][j]) {
                          isPossible = false;
                          break;
                        }                       
                }                
                if(!isPossible) break;
        }    
        if(isPossible) cout << "YES" << endl;
        else cout << "NO" << endl;
	}
	
	return 0;
}
