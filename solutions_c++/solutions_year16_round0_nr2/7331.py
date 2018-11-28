#include <iostream>
#include <vector>
#include <string>
using namespace std;
void solve() {
	string inp;
	cin >> inp;
	vector<int>input;
	for (string::iterator it=inp.begin(); it!=inp.end(); ++it) {
    if(*it=='+') input.push_back(1);
    if(*it=='-') input.push_back(0);
  }
  int result = 0;
  int i = 0;
  while (input.size()>1) {
    if (input[i]!=input[i+1]) {
      int tmp=input[i+1];
      input[i]=tmp;
      result++;
    } 
    if(input[i]==input[i+1]) {
      input.erase(input.begin());
    }
  }

  
  if(input[0]==0){
    result++;
  }
  cout << result << endl;
}

int main() {
  int tn;
  cin>>tn;
  for(int t = 0;t<tn;t++){
    cout<<"Case #"<<t+1<<": ";
    solve();
  }
  return 0;
}