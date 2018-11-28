#include <iostream>
#include <fstream>

using namespace std;

int main(){
  int N; cin >> N;
  for(int i = 0; i < N; i++){
    string s; cin >> s;
    char l = s[0];
    int ct = 1;
    for(int i = 1; i < s.length(); i++){
      if(s[i] != l){
	ct ++;
	l = s[i];
      }
    }
    if(s[s.length()-1] == '+'){ct--;}
    cout << "Case #" << i+1 << ": ";
    cout << ct << endl;
  }
  return 0;
}
