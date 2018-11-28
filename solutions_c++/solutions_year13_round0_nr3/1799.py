#include <iostream>
#include <vector>

using namespace std;

//#define LIMIT 32
#define LIMIT 10000000

typedef unsigned long long ull;

vector<ull> nums;

ull reverse(ull x) {
  ull r = 0;
  while (x > 0) {
    r *= 10;
    r += x % 10;
    x /= 10;
  }
  return r;
}

int countle(ull x) {
  int n = nums.size();
  //cerr << "n=" << n << " x=" << x << endl;
  
  int l = 0;
  int r = n-1;
  
  while (l <= r) {
    int i = (l+r) / 2;
    ull v = nums[i];
    
    //cerr << "l/r " << l << " " << r << " " << i << "=" << v << endl;
    
    if (v == x)
      return i+1;
    if (v < x)
      l = i+1;
    else
      r = i-1;
  }

  //cerr << "l/r " << l << " " << r << " " << r << "=" << nums[r] << endl;
  
  return r+1;
}

int main() {
  //int c = 0;
  for (ull x = 1; x <= LIMIT; x++) {
    if (x != reverse(x))
      continue;
  
    ull sq = x*x;  
    if (sq != reverse(sq))
      continue;
 
    //cerr << sq << endl;
    nums.push_back(sq);
    //c++;
  }
  
  //cerr << c << endl;
  
  int tc; cin >> tc;
  for (int t = 1; t <= tc; t++) {
    ull a, b; cin >> a >> b;
    int res = countle(b) - countle(a-1);
    cout << "Case #" << t << ": " << res << endl;
  }
  
  return 0;
}
