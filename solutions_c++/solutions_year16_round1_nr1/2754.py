#include <iostream>
#include <algorithm>
#include <vector>

typedef unsigned long long ull;
typedef long long ll;
using namespace std;

int main(){

  int T;
  cin >> T;
  for(int i=0; i< T; i++){

    string s;
    cin >> s;
    string r = "";
    for(int j=0; j<s.size(); j++){
      if(r.size() == 0) r += s[j];
      else{
	if(r[0] > s[j]){
	  r += s[j];
	}
	else{
	  r = s[j] + r;
	}
      }
    }
    
    cout << "Case #" << (i+1) << ": " << r << endl;
    
  }

}
