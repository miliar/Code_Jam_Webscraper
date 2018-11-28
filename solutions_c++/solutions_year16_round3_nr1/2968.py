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
#define _if(i,x,n) for(int i=(n);i>=x;i--)
#define _fv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _dv(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dav(i,f) cout<<"L"<<__LINE__<<": "<<#i<<"-"<<#f<<": "; dav(i,f);
template<typename it> void dav(it i,it f)
	{ cout<<"[ "; while(i!=f) cout<<*(i++)	<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

pair<int,char> senators[26];

bool orderSenators(pair<int,char> s1, pair<int,char> s2){
  return s1.first > s2.first;
}

bool checkMayority(int N, int total){
  _f(i, 0, N)
    if(senators[i].first > floor(total / 2))
      return false;
  return true;
}

int main(){
  int T, N, P, s;
  
  cin>>T;
  _f(tt,1,T+1){
    cin>>N;
    s = 0;
    //read senators
    _f(i, 0, N){
      cin>>P;
      senators[i] = make_pair(P, 'A' + i);
      s += P;
    }
    
    cout<<"Case #"<<tt<<":";
    
    while(s > 0){
      //order senators
      sort(senators, senators + N, orderSenators);
      /*_ln
      _f(i, 0, N)
        cout<<senators[i].first<<senators[i].second<<" ";
      cout<<endl;*/
      
      //remove sentaros
      
      //2 first senatros
      senators[0] = make_pair(senators[0].first - 2, senators[0].second);
      if(checkMayority(N, s - 2)){
        cout<<" "<<senators[0].second<<senators[0].second;
        s -= 2;
        continue;
      }
      else
        senators[0] = make_pair(senators[0].first + 2, senators[0].second);
      
      //1 first senator and 1 second senator
      if(N > 1 && senators[1].first > 0){
        senators[0] = make_pair(senators[0].first - 1, senators[0].second);
        senators[1] = make_pair(senators[1].first - 1, senators[1].second);
        if(checkMayority(N, s - 2)){
          cout<<" "<<senators[0].second<<senators[1].second;
          s -= 2;
          continue;
        }
        else{
          senators[0] = make_pair(senators[0].first + 1, senators[0].second);
          senators[1] = make_pair(senators[1].first + 1, senators[1].second);
        }
      }
      
      //1 first senator
      senators[0] = make_pair(senators[0].first - 1, senators[0].second);
      cout<<" "<<senators[0].second;
      s -= 1;
    }//while
    
    cout<<endl;
  }
  
  return 0;
}

