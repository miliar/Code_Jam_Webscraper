#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string res1;
string res2;
int diff;

int conv(string c) {
  int res = 0;
  for(int i = 0; i<(int)c.size();i++) {
    res *= 10;
    res += c[i]-'0';    
  }
  return res;
}

void run(string &c, string &j, int ind) {
  if(ind >= c.size()) {
    int one = conv(c);
    int two = conv(j);
    int r1 = conv(res1);
    int r2 = conv(res2);
    int cd = abs(one-two);
    //    cout << one << " " << two << endl;
    //   if(one == two) cout << "hi" << " " << cd << " " << diff << endl;
    if(res1.size() == 0 || cd < diff) {
      res1 = c;
      res2 = j;
      diff = cd;
    } else if (cd == diff && (one < r1 || (one==r1&&two<r2))) {
      res1 = c;
      res2 = j;
      diff = cd;
    }
    return;
  }
  if(c[ind] != '?' && j[ind] != '?') {
    run(c, j, ind+1);
  } else if (c[ind] == '?' && j[ind] != '?'){
    for(int i = 0; i < 10; i++) {
      c[ind] = i+'0';
      run(c,j,ind+1);
    }
    c[ind] = '?';
  } else if (c[ind] != '?' && j[ind] == '?') {
    for(int i =0 ; i < 10; i++) {
      j[ind] = i+'0';
      run(c,j,ind+1);
    }
    j[ind] = '?';
  } else {
    for(int i1 = 0; i1 < 10; i1++) {
      for(int i2 = 0; i2 < 10; i2++) {
	c[ind] = i1+'0';
	j[ind] = i2+'0';
	run(c,j,ind+1);
      }
    }
    c[ind]=j[ind]='?';
  }
}

int main() {
  int total_cases;
  cin >> total_cases;

  for(int caseno = 1; caseno <= total_cases; caseno++) {
    string c, j;
    cin >> c >> j;
    res1 = "";
    res2 = "";
    diff = 1<<30;

    run(c,j,0);
    cout << "Case #" << caseno << ": " << res1 << " " << res2 << endl;
  }
  return 0;
}
