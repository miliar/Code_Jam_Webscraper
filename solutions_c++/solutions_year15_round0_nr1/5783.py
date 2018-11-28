#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

#define INF (1<<29)

int main(){
  int Tc,S;
  string s;
  cin >> Tc;
  for(int T = 0 ; T < Tc ; T++){
    cin >> S >> s;
    int sum = s[0]-'0',res = 0;
    for(int i = 1 ; i < (int)s.size() ; i++){
      int x = s[i]-'0';
      if(i > sum){
	res++;
	sum++;
      }
      sum += x;
    }
    cout << "Case #" << T+1 << ": " << res << endl;
  }
  return 0;
}
