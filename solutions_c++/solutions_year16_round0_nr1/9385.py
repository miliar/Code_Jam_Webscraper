#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{
  long long t,n;
  string s;
  
  cin >> t;
  for(int i=0; i<t; ++i){
    cin >> n;
    if(n==0){
      cout << "Case #" << i+1 << ": INSOMNIA\n";
      continue;
    }

    vector<bool> v(10);
    int m = 1, checked = 0;
    stringstream ss;
    int init = n;
    while(checked<10){
      n = init * m;
      ss << n;
      s = ss.str();
      for(int j=0; j<s.size(); ++j){
	if(v[s[j]-'0'] == false){
	  v[s[j]-'0'] = true;
	  checked++;
	}
      }
      ++m;
    }
    
    cout << "Case #" << i+1 << ": " << n << '\n';
  }
  
  return 0;
}
