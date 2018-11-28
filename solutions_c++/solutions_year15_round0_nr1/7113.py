#include <iostream>
#include <string>

#define debug(x) cout<<#x<<" = "<<x<<endl;

using namespace std;

int main() {

  int sum, ans = 0;
  string s;

  int t;
  cin>>t;

  for(int j = 1; j <= t; j++) {

    int smax;
    cin>>smax;
    cin>>s;
    ans = 0;
    sum = s[0] - '0';
    
    for(int i = 1; i <= smax; i++) {
      if(sum < i and s[i] != '0') {
	ans = ans + i - sum;
	sum = sum + i - sum + s[i] - '0';
      }
      
      else if(s[i] != '0') {
	sum = sum + s[i] - '0';
      }
    }
    cout<<"Case #"<<j<<": "<<ans<<endl;
  }

    return 0;
}

   
	
