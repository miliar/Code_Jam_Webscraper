#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}



int main(){
  int cases;
  cin >> cases;
  for(int casenumber = 1; casenumber <= cases; casenumber++){
    int X,R,C;
    cin >> X;
    cin >> R;
    cin >> C;
    int ans = 0;
    if(X==1){
      ans = 1;
    }
    if(X==2){
      if((R*C)%2 == 0){
	ans = 1;
      }
    }
    if(X==3){
      int ma = max(R,C);
      int mi = min(R,C);
   
      if(ma == 3 && mi == 2){
	ans = 1;
      }
      if( ma == 3 && mi == 3){
	ans = 1;
      }
      if(ma == 4 && mi == 3){
	ans = 1;
      }
     
    }
  
    
    if(X==4){
      int ma = max(R,C);
      int mi = min(R,C);

      if(ma == 4 && mi == 3){
	ans =1;
      }
      if(ma == 4 && mi == 4){
	ans = 1;
      }
    }
    
    if(ans == 1){
      cout << "Case #" << casenumber << ": GABRIEL" << endl;
    }
    if(ans == 0){
      cout << "Case #" << casenumber << ": RICHARD" << endl;
    }

  }
  
}

