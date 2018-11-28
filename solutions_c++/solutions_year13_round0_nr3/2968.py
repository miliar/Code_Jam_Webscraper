#include <iostream>
#include <cmath>
#include <climits>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;


string convertInt(int num){
  stringstream ss;
  ss << num;
  return ss.str();
}

bool check_palindrome(int num){
  string s = convertInt(num);
  return equal(s.begin(), s.begin()+s.length()/2, s.rbegin());
}

int main(){
  int num_case;
  int a,b;
  cin >> num_case;
  for(int n = 1; n<=num_case; n++){
    int count =0;
    cin >> a >> b;
    int d = floor(sqrt(b));
    int c = ceil(sqrt(a));
    for(int i = c; i <= d; i++){
      if(check_palindrome(i)){
	int sq = i*i;
	if(sq >= c){
	  if(check_palindrome(sq)){
	    count ++;
	  }
	}
      }
    }
    cout << "Case "<< n << ": "  <<  count << endl;
  }
  return 0;
}
