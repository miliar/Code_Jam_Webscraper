#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

const int N = 4e5 + 5;

string s;
string tmp;

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  int t;
  cin >> t;
  for(int cs = 1; cs <= t; cs++){
    cout << "Case #" << cs << ": ";
    cin >> s;
    tmp = "";
    tmp += s[0];
    char first = s[0];
    for(int i = 1; i < s.length(); i++){
      if(s[i] >= first){
        tmp = s[i] + tmp;
        first = s[i];
      }
      else{
        tmp = tmp + s[i];
      }
    }
    cout << tmp << endl;
  }
  return 0;
}
