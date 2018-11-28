#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define ri(X) scanf("%d", &(X))
#define pi(X) printf("%d", (X))
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define lint long long
#define pii pair<int,int>
#define inf 1e9
#define linf 1e18
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define uni(X) X.erase(unique(X.begin(), X.end()), X.end());


void pv(vector<int> ve){
  reverse(all(ve));
  
  for(int i = 0; i < ve.size(); i++){
    printf("%d", ve[i]);
  }cout << endl;
}


vector<int> tovi(int n){
  vector<int> ve;
  while(n != 0){
    ve.pb(n%10);
    n/=10;
  }
  return ve;
}

// MAX 72 iterations n <= 1e6
int f(int n){
  vector<int> ve, vi;
  if(n <= 0) return -1;
  set<int> se;
  
  ve = vi = tovi(n);
  
  for(int i = 0; i < ve.size(); i++){
     se.insert(ve[i]);
  }
  
  int result = 1;
  while(se.size() < 10){
    assert(tovi(result*n) == ve); 
    
    //pv(ve);
    for(int i = 0; i < vi.size(); i++){
      ve[i] += vi[i];
      
      for(int k = 0; ; k++){
        
        if(ve[i+k] < 10){
          break;
        }
        ve[i+k] -= 10;
       
        if(ve.size() <= i+k+1) ve.pb(0);
        ve[i+k+1] +=1;
      }
    }
    
    
    for(int i = 0; i < ve.size(); i++){
       se.insert(ve[i]);
    }
    
    result++;
  }
  
  
  
  return result;
}



int main(){
  int T, n;
  ri(T);
  
  for(int t = 0; t < T; t++){
    ri(n);
    int res = f(n); 
    if(res <= 0){
      printf("Case #%d: INSOMNIA\n", t+1);  
    }else{
      printf("Case #%d: %d\n", t+1, res*n);
    }
  }
  
  
  return 0;
}

