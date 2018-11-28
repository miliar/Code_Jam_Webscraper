#include <iostream>
#include <vector>
using namespace std;
#include <cstdio>

typedef long long int ll;

void flip(string &str, int l, int r){
  for(int i = 0; i < (r - l + 1) / 2; i++){
    int x = i + l, y = r - i - 1;
    swap(str[x], str[y]);
    if(str[x] == '+') str[x] = '-';
    else str[x] = '+';
    if(x == y) continue;
    if(str[y] == '+') str[y] = '-';
    else str[y] = '+';
  }
  //cout << str << endl;
}

int main(void){
  int t;
  cin >> t;
  for(int ll = 0; ll < t; ll++){
    long long int ans = 0;
    string str;
    cin >> str;

    int left = 0, right = str.size() - 1;
    while(right >= 0 && str[right] == '+') right--;
    while(right >= left){
      int ll = left;
      while(ll < str.size() && str[ll] == '+') ll++;
      if(ll != left){
        flip(str, left, ll);
        ans++;
      }
      if(left <= right){
        flip(str, left, right + 1);
        ans++;
      }
      while(right >= 0 && str[right] == '+') right--;
    }
    cout << "Case #" << ll + 1 << ": " << ans << endl;
  }
}
