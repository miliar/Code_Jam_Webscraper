#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <gmpxx.h>
#include <boost/lexical_cast.hpp>

using namespace std;

int solve(const string&, const string&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    string A, B;
    cin >> A >> B;
    int r = solve(A, B);
    cout << "Case #" << i+1 << ": " << r << endl;
  }
}

bool is_palindrome(const mpz_class& n) {
  string n_str = n.get_str();
  int size = n_str.size();
  for(int i = 0; i < size / 2; i++) {
    if(n_str[i] != n_str[size - i - 1]) return false;
  }
  return true;
}

int solve(const string& A, const string& B){
  int count = 0;
  mpz_class a(A), b(B);
  mpz_class sqrt_a = sqrt(a);
  mpz_class sqrt_b = sqrt(b);
  if (sqrt_a * sqrt_a < a) sqrt_a += 1;
  string sqrt_a_str = sqrt_a.get_str();
  string sqrt_b_str = sqrt_b.get_str();
  int sqrt_a_len = sqrt_a_str.size();
  int sqrt_b_len = sqrt_b_str.size();
  for(int len = sqrt_a_len; len <= sqrt_b_len; len++) {
    int halflen = len/2;
    bool is_odd;
    if(len % 2 == 0) is_odd = false; else is_odd = true;
    mpz_class lower;
    mpz_class upper;
    if(len == sqrt_a_len) {
      if(halflen != 0) {
	string lower_str = sqrt_a_str.substr(0,halflen);
	lower = lower_str;
      }
    } else {
      if(halflen != 0) lower = "1" + string('0',halflen-1);
    }
    if(len == sqrt_b_len) {
      if(halflen != 0) {
	string upper_str = sqrt_b_str.substr(0,halflen);
	upper = upper_str;
      }
    } else {
      if(halflen != 0) upper = string('9',halflen);
    }
    if(is_odd) {
      if(halflen == 0) { // len == 1
	//cout << "len: " << len << endl;
	//cout << "A, B: " << A << " " << B << endl;
	//cout << "sqrt A, B: " << sqrt_a_str << " " << sqrt_b_str << endl;
	//cout << "lower, upper: " << lower << " " << upper << endl;
	for(int mid = 0; mid < 9; mid++) {
	  mpz_class to_check = mid;
	  if(to_check >= sqrt_a && to_check <= sqrt_b &&
	     is_palindrome(to_check * to_check)) {
	    count++;
	  }
	}
	//cout << "count: " << count << endl;
      } else { // len > 1
	//cout << "len: " << len << endl;
	//cout << "A, B " << A << " " << B << endl;
	//cout << "sqrt A, B " << sqrt_a_str << " " << sqrt_b_str << endl;
	//cout << "lower, upper " << lower << " " << upper << endl;
	for(int mid = 0; mid < 9; mid++) {
	  for(mpz_class i = lower; i < upper; i++) {
	    string s = i.get_str();
	    string s2 = s;
	    reverse(s2.begin(), s2.end());
	    string mid_str = boost::lexical_cast<string>(mid);
	    mpz_class to_check(s + mid_str + s2);
	    if(to_check >= sqrt_a && to_check <= sqrt_b &&
	       is_palindrome(to_check * to_check)) {
	      count++;
	    }
	  }
	}
	//cout << "count: " << count << endl;
      }
    } else { // even
      //cout << "len: " << len << endl;
      //cout << "A, B: " << A << " " << B << endl;
      //cout << "sqrt A, B: " << sqrt_a_str << " " << sqrt_b_str << endl;
      //cout << "lower, upper: " << lower << " " << upper << endl;
      for(mpz_class i = lower; i <= upper; i++) {
	string s = i.get_str();
	string s2 = s;
	reverse(s2.begin(), s2.end());
	mpz_class to_check(s + s2);
	if(to_check >= sqrt_a && to_check <= sqrt_b &&
	   is_palindrome(to_check * to_check)) {
	  count++;
	}
      }
      //cout << "count: " << count << endl;
    }
  }
  return count;
}
