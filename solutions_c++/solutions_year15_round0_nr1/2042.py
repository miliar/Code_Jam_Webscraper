#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdlib>
using namespace std;
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
int t;
string s;
int main() {
  if(fopen("A.in","r")) freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  cin >> t;
  for(int x, i = 1; i <= t; i++) {
    cin >> x;
    printf("Case #%d: ", i);
    cin >> s;
    int num = 0;
    int need = 0;
    for(int j = 0; j <= x; j++) {
      if(num < j) {
        need += j - num;
        num = j;
      }
      num += (s[j]-'0');
    }
    cout << need << endl;
  }
  return 0;
}