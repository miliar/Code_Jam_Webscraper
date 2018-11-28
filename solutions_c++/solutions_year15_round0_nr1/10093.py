#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

char s[1000000];
int main(){

  long long  c ,j=1;
  cin >> c;
  while(c > 0){
    long long max_shy, sum = 0, ans = 0;
    cin >> max_shy >> s;
    for(long long i = 0; i <= max_shy; i++){
      char tmp = s[i];
      if(sum < i){
	ans += i - sum;
	sum += i - sum;
      }
      sum += atoi(&tmp);
    }
    cout << "Case #"<< j <<": " << ans ;
    if(c != 1)cout << endl;
    c--;
    j++;
  } 
 return 0;
}
