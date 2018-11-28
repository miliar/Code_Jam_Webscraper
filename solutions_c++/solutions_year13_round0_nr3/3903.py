#include <iostream>
#include <string>
#include <sstream>
#include <utility>
#include <climits>
#include <vector>
#include <iterator>
#include <cctype>
#include <stack>
#include <cmath>

using namespace std;
bool isPolyndrom(long n){
     std::stringstream ss;
     ss << n;
     string val = ss.str();
     for(int i =0; i < val.length(); ++i){
             if(val[i] != val[val.length() - 1 - i]) return false;
     }
     return true;
}
int main(){
	int T;
	cin >> T;
	for(int t = 0 ; t < T; ++t){
        cout << "Case #" << (t+1) << ": ";
        int a, b;
        cin >> a;
        cin >> b;
        int i = a;
        if(i > 2){
                double sqa = sqrt(a);
                i = (int)floor(sqa);
        }
        int ret = 0L;
        while(true){
          long cand = i*i;
          if(cand > b) break;
          if(cand >= a && isPolyndrom(i) && isPolyndrom(cand)) {
             ret++;
          }
          ++i;
        }
        cout << ret << endl;
	}
	
	return 0;
}
