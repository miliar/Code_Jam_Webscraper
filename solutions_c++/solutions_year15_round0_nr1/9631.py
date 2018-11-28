#include <bits/stdc++.h>
using namespace std;

int main() {
  int T, count, ans, garbage;
  string S;
  cin >> T;
  
  for(int i=0; i<T; i++){
  	count=0;
  	ans=0;
  	cin >> garbage;
  	cin >> S;
  	for(int j=0; j<S.length(); j++){
  	  if(count>=j){
  	  	count+=S[j]-'0';
  	  }
  	  else{
  	  	ans+=j-count;
  	  	count=j;
  	  	count+=S[j]-'0';
  	  }
  	}
  	cout << "Case #" << i+1 << ": " << ans << endl;
  }
}