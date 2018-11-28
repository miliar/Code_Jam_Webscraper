#include<iostream>
#include<assert.h>
#include<vector>
using namespace std;
int f(int a, int b ){
  return a/b - (a % b == 0);
}


int calc( int d, vector<int> p ){
  int res = 1000;
  for( int i = 1; i <= 1000; i++){
    int tmp = 0;

    for(int j = 0; j < p.size(); j++){
      tmp += f( p[j], i );
    }
    res = min( res, tmp+i );
  }
  return res;
}
    
int main(void){
  int T;
  cin>>T;
  for(int case_count = 1; case_count <= T; case_count++){
    int d;
    vector<int> p;
    cin>>d;
    for( int i = 0; i < d; i++ ){
      int tmp;
      cin>>tmp;
      p.push_back(tmp);
    }
    int res = calc(d, p );
      
    
    cout << "Case #" << case_count << ": " << res <<endl;
  }
  return 0;
}
