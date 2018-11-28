//	__R0b__
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t; cin>>t;
  for (int q=1;q<=t;q++){
	  printf("Case #%d: ",q);
	  int maxshyness; cin>> maxshyness;
	  string s; cin>>s;
	  int len= s.length(),add=0,people=s[0]-'0';//people = (int)(s[0]-'0');
	 // if (s[0]=='0') add++;
	  for (int i=1;i<len;i++){
		  if (people >= i){

		  } else {
			  add++;
			  people++;
		  }
		  people += s[i]-'0';
	  }

	  cout << add << endl;
  }
  return 0;
}
