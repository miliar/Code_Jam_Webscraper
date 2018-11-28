#include <iostream>
#include <string>

using namespace std;

int main(int argc, char**argv){
  int T;
  int debug=0;
  if(argc>1&&string(argv[1])=="debug")
    debug = 1;
  cin>>T;
  for(int i=0;i<T; i++){
    cout<<"Case #"<<i+1<<": ";
    int M, N;
    cin>>N>>M;
    int**heights = new int*[N];
    for(int i=0; i<N; i++){
      heights[i] = new int[M];
      for(int j=0; j<M; j++){
	cin>>heights[i][j];
      }
    }

    if(debug)
      for(int i=0; i<N; i++){
	cout<<endl;
	for(int j=0; j<M; j++){
	  cout<<heights[i][j]<<" ";
	}
      }

    int * rowmaxes = new int[N];
    for(int i=0; i<N; i++){
      rowmaxes[i]=heights[i][0];
      for(int j=1; j<M; j++){
	if(rowmaxes[i]<heights[i][j]){
	  rowmaxes[i]=heights[i][j];
	}
      }
      if(debug)
	cout<<"Rowmax "<<rowmaxes[i]<<endl;
    }

    int * colmaxes = new int[M];
    for(int i=0; i<M; i++){
      colmaxes[i]=heights[0][i];
      for(int j=1; j<N; j++){
	if(colmaxes[i]<heights[j][i]){
	  colmaxes[i]=heights[j][i];
	}
      }
      if(debug)
	cout<<"Colmax "<<colmaxes[i]<<endl;
    }

    int cuttable = 1;
    for(int i=0; i<N; i++){
      for(int j=0; j<M; j++){
	if(!(heights[i][j]>=rowmaxes[i]||heights[i][j]>=colmaxes[j]))
	  cuttable = 0;
      }
    }

    if(cuttable)
      cout<<"YES\n";
    else
      cout<<"NO\n";

    for(int i=0; i<N; i++)
      delete heights[i];
    delete[] heights;
    delete[] rowmaxes;
    delete[] colmaxes;
  }

}
