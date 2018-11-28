#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
#include<cassert>
#include<map>

using namespace std;
const int MAXL = 10000;
enum Q { o, i, j, k, no, ni, nj, nk };
typedef pair<Q,Q> qq;

Q prod[MAXL+1];  // prod[i] = product of s[0..i]

map<qq, Q> M1
{
  {{o,o}, o},
  {{o,i}, i},
  {{o,j}, j},
  {{o,k}, k},
  {{i,o}, i},
  {{i,i}, no},
  {{i,j}, k},
  {{i,k}, nj},
  {{j,o}, j},
  {{j,i}, nk},
  {{j,j}, no},
  {{j,k}, i},
  {{k,o}, k},
  {{k,i}, j},
  {{k,j}, ni},
  {{k,k}, no}
};

Q inv(const Q& x) {
  if(x == o) return no;
  if(x == i) return ni;
  if(x == j) return nj;
  if(x == k) return nk;
  if(x == no) return o;
  if(x == ni) return i;
  if(x == nj) return j;
  if(x == nk) return k;
}

bool is_neg(const Q& x) {
  if(x == ni || x == nj || x == nk || x == no) {
    return true;
  }
  return false;
}

int main() {
  int T, l, x;
  string tmp, s;

  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> l >> x;
    cin >> tmp;
    s = tmp;
    for(int i = 1; i < x; ++i) {
      s += tmp;
    }

    assert(s.length() <= MAXL);

    string ans;

    if(s.length() <= 2) {
      ans = "NO";
    } else {
      if(s[0] == 'i') prod[0] = i;
      else if(s[0] == 'j') prod[0] = j;
      else prod[0] = k;

      for(int ii = 1; ii < s.length(); ++ii) {
        Q cur;
        if(s[ii] == 'i') cur = i;
        else if(s[ii] == 'j') cur = j;
        else if(s[ii] == 'k') cur = k;

        if(is_neg(prod[ii-1])) {
          prod[ii] = M1[qq{inv(prod[ii-1]), cur}];
          prod[ii] = inv(prod[ii]);
        } else {
          prod[ii] = M1[qq{prod[ii-1], cur}];
        }
      }

      ans = "NO";
      if(prod[s.length()-1] != no) {
        ans = "NO";
      } else {

        // [0..ii], [ii+1..jj], [jj+1..len-1]
        for(int ii = 0; ii <= s.length()-3; ++ii) {
          for(int jj = ii+1; jj <= s.length()-2; ++jj) {
            if(prod[ii] == i) {
              if(prod[jj] == k) {
                ans = "YES";
                break;
              }
              if(ans == "YES") break;
            }
          }
        }
      }
    }



    cout << "Case #" << t << ": " << ans;
    if(t < T) cout << "\n";
    //cout << l << " " << x;
    //cout << "\n" << s << "\n";
  }
  return 0;
}
