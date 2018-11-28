#include <iostream>
#include <fstream>
using namespace std;

int main(int argc , char ** argv){
  ifstream fi(argv[1]);
  int T;
  int N,M;
  string line;
  int m[100][100];
  int max_row[100];
  int max_col[100];

  fi >> T;
  for(int i=0;i<T;++i){
    fi >> N >> M ;
    for(int j=0;j<N;j++){
      for(int k=0;k<M;k++)
	fi >> m[j][k];
    }
    bool possible = true;
    for(int j=0;j<N;j++){
      int max = 0;
      for(int k=1;k<M;k++)
	if(m[j][k] > m[j][max])
	  max =k;
      max_row[j] = m[j][max];
    }

    for(int j=0;j<M;j++){
      int max = 0;
      for(int k=1;k<N;k++)
        if(m[k][j] > m[max][j])
          max =k;
      max_col[j] = m[max][j];
    }

    for(int j=0;j<N && possible;j++){
      for(int k=0;k<M && possible ;k++)
	if(m[j][k] < max_row[j] && m[j][k] < max_col[k])
	  possible = false;
    }

    if(possible)
      cout << "Case #" << i+1 << ": YES" << endl;
    else
      cout << "Case #" << i+1 << ": NO" << endl;    
  }
  
  fi.close();
}
