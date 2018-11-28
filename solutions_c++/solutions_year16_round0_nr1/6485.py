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

#define _dv(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dav(i,f) cout<<"L"<<__LINE__<<": "<<#i<<"-"<<#f<<": "; dav(i,f);
template<typename it> void dav(it i,it f)
	{ cout<<"[ "; while(i!=f) cout<<*(i++)	<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

int main(){
  int T, N, aux, d, j;
  cin>>T;
  _f(i, 1, T + 1){
    cin>>N;
    set<int> digits;
    if(0 == N)
      printf("Case #%d: INSOMNIA\n",i);
    else{
      j = 1;
      while(10 > digits.size()){
        aux = j*N;
        j++;
        while(0 < aux && 10 > digits.size()){
          d = aux % 10;
          aux /= 10;
          digits.insert(d);
        }
      }
      printf("Case #%d: %d\n",i,N*(j-1));
    }
  }

  return 0;
}


