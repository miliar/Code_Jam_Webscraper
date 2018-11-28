#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define _f(i,x,n) for(int i=x;i<n;i++)
#define _if(i,x,n) for(int i=(n);i>=x;i++)
#define _fv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _d(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dv(v) cout<<"L"<<__LINE__<<": "<<#v<<": "; di((v).begin(),(v).end());
#define _dvf(v) cout<<"L"<<__LINE__<<": "<<#v<<": "; di((v).begin(),(v).end()); *************************
template<typename it> void di(it i,it f) { cout<<"[ "; while(i!=f) cout<<*(i++)<<" "; cout<<"]"<<endl; }
template<typename it> void dif(it i,it f,string ) { cout<<"[ "; while(i!=f) cout<<*(i++)<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

int lawn[100][100];
int N,M;

const char * validatePattern(){
  _f(i,0,N)
    _f(j,0,M){
      //validate row
      bool row = false;
      for(int k=0; k<M && !row; k++)
        if(lawn[i][j] < lawn[i][k])
          row = true;
      //validate column
      bool col = false;
      for(int k=0; k<N && !col; k++)
        if(lawn[i][j] < lawn[k][j])
          col = true;

      //is value valid
      if(col && row) return "NO";
    }
    return "YES";
}

int main(){
    int T;
    cin>>T;
    _f(tt,1,T+1){
        cin>>N>>M;
        _f(i,0,N)
          _f(j,0,M)
            cin>>lawn[i][j];
        cout<<"Case #"<<tt<<": "<<validatePattern()<<endl;
    }
    return 0;
}
