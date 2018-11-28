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
    int smax;
    cin >> smax;
    string s;
    cin >> s;
    vector<int> v;
for(int i = 0; i < (int)s.size(); ++i){
  v.push_back(int(s[i])-48);
}


    int total = 0;
    int ans = 0;
    vector<int> :: iterator it;
    it = v.begin();
    total = *it;
    for(int i = 1; i<=smax; i++){
      it++;
      if(total >= i){
	total += *it;
      }else{
	ans += i-total;
	total =  i + *it;

	
      }
    }
    
 
    cout << "Case #" << casenumber << ": " << ans << endl;
  }
  
}
