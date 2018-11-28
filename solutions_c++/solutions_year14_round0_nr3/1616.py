#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>
#include <complex>
#include <cmath>
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<int> vec;
typedef vector<vec> mat;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

const int MAX = 100;
int field[MAX][MAX];
char m[MAX][MAX];
int R,C,M;

const int DEBUG = 0;

void init(){
  for(int i=0;i<MAX;++i){
    for(int j=0;j<MAX;++j){
      field[i][j] = 0;
      m[i][j] = '#';
    }
  }
  for(int i=1;i<=R;++i){
    for(int j=1;j<=C;++j){
      m[i][j] = '.';
    }
  }
}

void show(){
  for(int i=1;i<=R;++i){
    for(int j=1;j<=C;++j){
      cout << m[i][j];
    }cout << endl;
  }
}


int dx[] = {0,0,1,1,1,-1,-1,-1};
int dy[] = {1,-1,0,1,-1,0,1,-1};

void checking(int x,int y){
  if(field[y][x])return;
  field[y][x] = 1;
  bool flag = true;
  for(int i=0;i<8;++i){
    int mx = x + dx[i];
    int my = y + dy[i];
    if(m[my][mx] == '*' ){
      flag = false;
      break;
    }
  }
  if(flag){
    for(int i=0;i<8;++i){
      int mx = x + dx[i];
      int my = y + dy[i];
      if(m[my][mx] == '.')checking(mx,my);
    }
  }
}

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;++t){
    cout << "Case #" << t << ":" << endl;;

    cin >> R >> C >> M;
    if(DEBUG)cout << R << " " << C << " " << M << endl;
    init();


    int cnt = 0;
    int lim;
    if(R < C){
      lim = M / R;

      lim = min(lim,max(C-2,1) );
      for(int j=1;j<=lim && cnt < M ;++j){
	for(int i=1;i<=R && cnt < M;++i){
	  m[i][j] = '*';
	  cnt++;
	}
      }
      if( C - lim > M - cnt){
	for(int j=lim+1;j<=C-2 && cnt < M;++j){
	  for(int i=1;i<=R-2 && cnt < M;++i){
	    m[i][j] = '*';
	    cnt++;
	  }
	}
      }

      if(M > cnt){
	for(int i=1;i<=R && cnt < M;++i){
	    for(int j=lim+1;j<=C && cnt < M;++j){
	    if(m[i][j]!='*'){
	      m[i][j] = '*';
	      cnt++;
	    }
	  }
	}

      }
    }
    else {
      lim = M / C;
      if(DEBUG)cout << "lim : " << lim << endl;
      lim = min(lim,max(R-2,1));
      for(int i=1;i<=lim && cnt < M;++i){
	for(int j=1;j<=C && cnt < M ;++j){
	  m[i][j] = '*';
	  cnt++;
	}
      }
      if(DEBUG)cout << cnt << endl;
      if( R - lim > M - cnt){
	for(int i=lim+1;i<=R-2 && cnt < M;++i){
	  for(int j=1;j<=C-2 && cnt < M;++j){
	    m[i][j] = '*';
	    cnt++;
	  }
	}
      }

      if(DEBUG)cout << cnt << endl;
      if(M > cnt){
	for(int j=1;j<=C && cnt < M;++j){
	  for(int i=lim+1;i<=R && cnt < M;++i){
	    if(m[i][j]!='*'){
	      m[i][j] = '*';
	      cnt++;
	    }
	  }
	}
      }
    }

    m[R][C] = 'c';

    bool flag = true;

    if(flag)checking(C,R);
    for(int i=1;i<=R;++i){
      for(int j=1;j<=C;++j){
	if( field[i][j] == 0 && m[i][j]=='.' )flag = false;
      }
    }

    if(DEBUG){
      for(int i=1;i<=R;++i){
	for(int j=1;j<=C;++j){
	  cout << field[i][j];
	}cout << endl;
      }
      show();
      if(flag==false)cout << "Impossible" << endl;
    } else {
      if(flag)
        show();
      else {
      	// 再チェック
      	init();
	cnt =0;
      	if(R < C){
      	  lim = M / R;
      	  //if(R!=1 && lim >= C-2 && M&1){cout << "Impossible" << endl;continue;}

      	  lim = min(lim,max(C-3,1) );
      	  for(int j=1;j<=lim && cnt < M ;++j){
      	    for(int i=1;i<=R && cnt < M;++i){
      	      m[i][j] = '*';
      	      cnt++;
      	    }
      	  }
      	  //cout << cnt  << endl;
      	  if( C - lim > M - cnt){
      	    for(int j=lim+1;j<=C-2 && cnt < M;++j){
      	      for(int i=1;i<=R-2 && cnt < M;++i){
      		m[i][j] = '*';
      		cnt++;
      	      }
      	    }
      	  }

      	  //cout << cnt << endl;
      	  if(M > cnt){
      	    for(int i=1;i<=R && cnt < M;++i){
      	      for(int j=lim+1;j<=C && cnt < M;++j){
      		if(m[i][j]!='*'){
      		  m[i][j] = '*';
      		  cnt++;
      		}
      	      }
      	    }

      	  }
      	}
      	else {
      	  lim = M / C;

      	  //if(C!=1 && lim >= R-2 && M&1){cout << "Impossible" << endl;continue;}
      	  if(DEBUG)cout << "lim : " << lim << endl;
      	  lim = min(lim,max(R-3,1));
      	  for(int i=1;i<=lim && cnt < M;++i){
      	    for(int j=1;j<=C && cnt < M ;++j){
      	      m[i][j] = '*';
      	      cnt++;
      	    }
      	  }
      	  if(DEBUG)cout << cnt << endl;
      	  if( R - lim > M - cnt){
      	    for(int i=lim+1;i<=R-2 && cnt < M;++i){
      	      for(int j=1;j<=C-2 && cnt < M;++j){
      		m[i][j] = '*';
      		cnt++;
      	      }
      	    }
      	  }

      	  if(DEBUG)cout << cnt << endl;
      	  if(M > cnt){
      	    for(int j=1;j<=C && cnt < M;++j){
      	      for(int i=lim+1;i<=R && cnt < M;++i){
      		if(m[i][j]!='*'){
      		  m[i][j] = '*';
      		  cnt++;
      		}
      	      }
      	    }
      	  }
      	}

      	m[R][C] = 'c';
      	flag = true;
      	if(flag)checking(C,R);
      	for(int i=1;i<=R;++i){
      	  for(int j=1;j<=C;++j){
      	    if( field[i][j] == 0 && m[i][j]=='.' )flag = false;
      	  }
      	}

      	if(flag) show();
      	else cout << "Impossible" << endl;
      }
    }
    //if(!flag)show();
  }
}
