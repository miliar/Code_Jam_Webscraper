#include <iostream>
#include <string>
#include <assert.h>
#include <sstream>
#include <stdio.h>

using namespace std;

struct Number {
  
  long long n;

  Number(): n(0) { }

  Number(const string& s) {
    istringstream ss(s);
    ss >> n;
  }
  
  Number(const Number& that): n(that.n) { }

  void FromInt(long long nn) {
    n = nn;
  }
  
  Number& operator=(const Number& that) {
    n = that.n;
    return *this;
  }
  
  Number& operator++() {  // prefix++
    n++;
    return *this;
  }
  Number operator++(int) { // postfix++
    Number result(*this);
    ++(*this);
    return result;
  }

  bool operator<=(const Number& that) {
    return n <= that.n;
  }

  bool IsFair() {
    stringstream ss;
    ss << n;
    const char* s = ss.str().c_str();
    int i ,j;
    for(i = 0, j = ss.str().size()-1; i < j; i++,j--)
      if (s[i] != s[j])
        return false;
    return true;
  }

  bool IsSquare(Number* root) {
    long long low,high,mid;

    low = 0;
    high = n;

    while(low <= high) {
      mid = (low + high)/2;
      long long mid2 = mid * mid;
      if (mid2 == n) {
        root->FromInt(mid);
        return true;
      } else if (mid2 < n) {
        low = mid+1;
      } else {
        high = mid-1;
      }
    }
    return false;
  }
};

int main()
{

  int n;
  cin >> n;

  for(int k = 1; k <= n; k++) {
    string l,h;
    cin >> l >> h;
    Number low(l),high(h),x,root;
    int r = 0;
    for(x = low; x <= high; ++x) {
      if (x.IsFair() && x.IsSquare(&root) && root.IsFair()) {
        ++r;
      }
    }
    printf("Case #%d: %d\n",k,r);
  }
  return 0;
}
    
    

    
    



