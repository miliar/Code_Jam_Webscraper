#include <iostream>
#include <deque>

using namespace std;

int main(){
  int cases = 1;
  string in;
  deque<char> result;
  int t;
  cin >> t;
  while(t--){
    cin >> in;
    result.clear();
    result.push_front(in[0]);
    
    for(int i = 1; i <= in.size(); ++i){
      if(in[i] >= result.at(0)){
	result.push_front(in[i]);
      }else
	result.push_back(in[i]);
    }

    cout << "Case #" << cases << ": ";
    for(int i = 0 ; i < result.size()-1;++i){
      cout << result.at(i);
    }
    cases++;
    cout << endl;
  }
}
