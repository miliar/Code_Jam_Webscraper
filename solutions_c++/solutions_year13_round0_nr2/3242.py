#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define SAFE 1
#define UNSAFE 0

int main(){
    int N, M;
    int num_case;
    cin >> num_case;
    for(int n = 1; n <= num_case;n++){
      cin >> N >> M;

      int board[N][M];
      int temp[N][M];

      for(int i=0; i<N; i++){
	for(int j=0; j< M;j++){
	  temp[i][j] = UNSAFE;
	}
      }
    
        
      int data;
      for(int i=0; i<N; i++){
	for(int j=0; j<M; j++){
	  cin >> data;
	  board[i][j] = data;
	}
      }

      int value = 101;
      for(int i=0; i<N;i++){
	for(int j=0; j <M; j++){
	  if(board[i][j] < value)
	    value  = board[i][j];
	}
      }
    
      bool pV, pH, check_fail;
      bool done=0;
      while(!done){
	done = 1;
	check_fail = 1;
	pV = pH = 1;
	for(int i=0; i<M; i++){
	  if(board[0][i] == value){
	    // check the entire col
	    for(int j=0; j<N; j++){
	      if(board[j][i]!=value){
		pV = 0; break;
	      }
	    }
	    
	    if(pV){
	      check_fail = 0;
	      for(int k=0; k < N;k++){
		temp[k][i] = SAFE;
	      }
	    }
	  }
	  pV = 1;
	}
	// done with vertical

	for(int i=0; i<N;i++){
	  if(board[i][0]==value){
	    for(int j=0; j < M;j++){
	      if(board[i][j] != value){
		pH = 0; break;
	      }
	    }
	    
	    if(pH){
	      check_fail = 0;
	      for(int k=0;k<M;k++){
		temp[i][k]=SAFE;
	      }
	    }
	  }
	  pH = 1;
	}
	int new_min;
	if(check_fail) {
	  done = 1;
	}
	else{
	  // find the second last value;
	  int max = 101;
	  for(int i=0; i<N;i++){
	    for(int j=0; j < M; j++){
	      if(board[i][j] < max && board[i][j]!=value){
		done = 0;
		max = board[i][j];
	      }
	    }
	  }
	  new_min = max;
	  //update all min to new min;
	  for(int i=0; i < N; i++){
	    for(int j=0; j < M; j++){
	      if(temp[i][j] == SAFE){
		board[i][j] = new_min;
	      }
	    }
	  }
    
	}
	// double check
	for(int i=0; i<N; i++){
	  for(int j=0; j<M;j++){
	    if(board[i][j]==value){
	      check_fail = 1;
	      done = 1;
	    }
	  }
	}
	value = new_min;
	
    
      }
      cout << "Case #"<<n<<": ";
      if(check_fail) cout << "NO" << endl;
      else cout << "YES" << endl;
    }
}
