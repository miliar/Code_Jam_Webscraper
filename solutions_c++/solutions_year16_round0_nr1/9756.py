/* 
Google codejam template
Author: Michael Yitayew
Email: myitayew@princeton.edu
LANG: C++
*/

#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath> 
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <unordered_map>

using namespace std;

int main() {

  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    cin >> n;
    int a[10];
    memset(&a, 0x00, sizeof(int)*10);
    int count = 0;
    int i = 1;
    if (n == 0) 
      cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
    else {
      while (true) {
	int current = i*n;
	do {
	  int j = current%10;
	  current/=10;
	  if (a[j] == 0) {
	    a[j] = 1;
	    count++;
	  }
	} while (current > 0);
	if (count == 10) {
	  cout<<"Case #"<<t<<": "<<i*n<<endl;
	  break;
	}
	i++;
      }
    }
  }

  return 0;
}


