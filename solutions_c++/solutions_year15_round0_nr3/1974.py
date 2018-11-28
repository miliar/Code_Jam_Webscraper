#include <iostream>
#include <string>
#include <cassert>

using namespace std;

#define CONV(a) ((a)=='i'?QI:(a)=='j'?QJ:QK)
#define QI 2
#define QJ 3
#define QK 4
#define INCR(x) ((x)==QK?QI:(x)+1)

int mul(int a, int b){
  if(a == 0) return b;
  if(abs(a) == 1 || abs(b) == 1) return a*b;
  int s = (a == abs(a) ? 1 : -1) * (b == abs(b) ? 1 : -1);
  if(abs(a) == abs(b)) return -1*s;
  if(INCR(abs(a)) == abs(b)) return s*INCR(abs(b));
  if(INCR(INCR(abs(a))) == abs(b)) return -s*INCR(abs(a));
  assert(false);
}

int main(void){
  int t, l, x;
  cin >> t;
  for(int k = 0; k < t ; ++k){
    cin >> l >> x;
    string s, ss;
    cin >> s;
    for(int i = 0; i < x; ++i)
      ss += s;

    // cout << ss << endl;

    bool res = false;
    int ch1, ch2, ch3;
    for(int i = 0, ch1=0; i < ss.size(); ++i){
      ch1 = mul(ch1, CONV(ss[i]));
      // cout << i << " : " << ch1 << endl;
      if(ch1 == QI){
        for(int j = i+1, ch2=0; j < ss.size(); ++j){
          ch2 = mul(ch2, CONV(ss[j]));
          // cout << "  " << j << " : " << ch2 << endl;
          if(ch2 == QJ){
            for(int k = j+1, ch3=0; k < ss.size(); ++k){
              ch3 = mul(ch3, CONV(ss[k]));
              // cout << "    " << k << " : " << ch3 << endl;
              if(ch3 == QK && k == ss.size()-1){
                res = true;
                goto end;
              }
            }
          }
        }
      }
    }
  end:

    cout << "Case #" << k+1 << ": " << (res ? "YES" : "NO") << endl;
  }
  return 0;
}
