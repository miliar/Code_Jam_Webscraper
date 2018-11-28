#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=0; t<T; t++){
    int smax;
    string s;
    cin >> smax >> s;
    int stand = 0;
    int ans = 0;
    for(int i=0; i<smax+1; i++){
      stringstream ss;
      int n;
      ss << s[i];
      ss >> n;
      if(i>stand){
	ans += (i-stand);
	n += (i-stand);
      }
      stand += n;
    }
    cout << "Case #" << t+1 << ": " << ans << endl;
  }
}

