#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    int s;
    cin >> s;
    string str;
    cin >> str;
    FOR (ret, str.sz + 1) {
      bool done = true;
      int cnt = ret;
      FOR (i, str.sz + 1) {
        int a = str[i] - '0';
        if (a && cnt < i)
          done = false;
        cnt += a;
      }
      if (done) {
        cout << ret;
        break;
      }
    }
    cout << "\n";
  }
  return 0;
}
