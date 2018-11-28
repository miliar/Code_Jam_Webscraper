#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;

int main(){
  int n_case;
  cin >> n_case;
  int cnt[17];
  for( int loop = 0 ; loop < n_case ; loop++ ){
    memset(cnt,0,sizeof(cnt));
    int n;
    for( int question = 0 ; question < 2; question++ ){
      cin >> n;
      for( int row = 1; row <=4 ; row++ ){
        for( int col = 1 ; col <= 4 ; col++ ){
          int curnum;
          cin >>curnum;
          if( n == row ){
            cnt[curnum]++;
          }
        }
      }
    }
    vector<int> num;
    for( int i = 1; i <= 16 ; i++ ){
      if( cnt[i] == 2 ) num.push_back(i);
    }
    if( num.size() == 0 ){
      cout << "Case #" << loop+1 << ": " <<"Volunteer cheated!"<< endl;
    }
    else if( num.size() == 1 ){
      cout << "Case #" << loop+1 << ": " <<num[0]<< endl;
    }
    else{
      cout << "Case #" << loop+1 << ": " <<"Bad magician!"<< endl;
    }

  }
  return 0;
}
