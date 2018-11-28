#include<iostream>
#include<algorithm>

using namespace std;

string solve(int a[][110], int N, int M){
  bool det[110][110]={{0,},};
  while(true){
    int maxi = -1;
    for(int i = 0; i < N; ++i){
      for(int j = 0; j < M; ++j){
        if( !det[i][j] ){
          maxi = max( maxi, a[i][j] );
        }
      }
    }

    if( maxi == -1 ) break;

    for(int i = 0; i < N; ++i){
      for(int j = 0; j < M; ++j){
        if( a[i][j] == maxi ) det[i][j] = true;
      }
    }
    
    for(int i = 0; i < N; ++i){
      for(int j = 0; j < M;++j){
        if( !det[i][j] ){
          bool ng_col = false, ng_row = false;
          
          for(int k = 0; k < N; ++k){
            if( det[i][k] ) ng_row = true;
            if( det[k][j] ) ng_col = true;
          }

          if( ng_col && ng_row ) return "NO";
        }
      }
    }
  }
  return "YES";
}

int main()
{
  int T;
  cin >> T;
  
  for(int tc=1;tc<=T;++tc){
    int N,M;
    cin >> N >> M;
    int a[110][110]={{0,},};

    for(int i = 0; i < N; ++i){
      for(int j = 0; j < M; ++j){
        cin >> a[i][j];
      }
    }

    string status = solve(a,N,M);

    cout << "Case #" << tc <<": "<<status << endl;
  }

  return 0;
}

