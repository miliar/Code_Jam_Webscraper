#include <iostream>
#include <vector>
#include <string>

#define FOR(i,C) for(int i=0; i<C; i++)
#define FOR_REV(i,C) for(int i=C-1; i>=0; i--)

typedef long long ll_t;

using namespace std;

string ans(vector<vector<int> >& a, int N, int M);

int main(int argc, char* argv[]){
  int T;

  cin >> T;

  // read input
  ll_t c = 0;
  while( cin ){
    if( ++c > T ) return -1;

    int N,M;

    cin >> N >> M;
    vector<vector<int> > a;

    FOR(i,N){
      int tmp;
      vector<int> v_tmp;

      FOR(j,M){
        cin >> tmp;
        v_tmp.push_back(tmp);
      }

      a.push_back(v_tmp);
    }

    // output answer
    cout << "Case #" << c << ": " << ans(a,N,M) << endl;
  }
}

string ans(vector<vector<int> >& a, int N, int M){

  vector<vector<int> > b;

  FOR(i,N){
    vector<int> v_tmp(M,100);
    b.push_back(v_tmp);
  }

  FOR(i,N){
    int max = 0;
    // search max height in row
    FOR(j,M){
      if( a[i][j] > max ){ max = a[i][j]; }
    }
    // cut b
    FOR(j,M){
      if( b[i][j] > max ){ b[i][j] = max; }
    }
  }

  FOR(j,M){
    int max = 0;
    // search max height in column
    FOR(i,N){
      if( a[i][j] > max ){ max = a[i][j]; }
    }
    // cut b
    FOR(i,N){
      if( b[i][j] > max ){ b[i][j] = max; }
    }
  }

  // check YES/NO
  FOR(i,N){
    FOR(j,M){
      if( a[i][j] != b[i][j] ){
        return "NO";
      }
    }
  }

  return "YES";
}
