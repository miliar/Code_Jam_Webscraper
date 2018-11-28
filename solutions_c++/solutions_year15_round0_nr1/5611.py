#include <iostream>
#include <string>

using namespace std;

int main(){
  int cn, ci;
  int a[1000], n;
  string s;
  int i;
  char c;
  int curr, x, add;

  cin >> cn;

  for(ci=1; ci<=cn; ++ci){
    cin >> n >> s;
    //cout << s << "\n";

    curr = add = 0;
    for(i=0; i<s.length(); ++i){
      x = s[i]-'0';
      //cout << x << " ";

      if(curr < i){
	add += i - curr;
	curr = i;
      }
      curr += x;
      	
    }
    cout << "Case #" << ci << ": ";

    cout << add;

    cout << "\n";
  }
    
  
  
  return 0;
}
