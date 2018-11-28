#include <bits/stdc++.h>
#define MAX 19
using namespace std;

int main(){
  freopen("A-small-input.txt", "r", stdin);
  freopen("A-small-output.txt", "w", stdout);
  int tc, ct = 0;
  cin >> tc;
  while (tc--){
    int n, standing = 0, invited = 0;
    string str;
    cin >> n >> str;
    standing = (str[0] - '0');
    for (int i = 1; i < str.size(); i++){
      if (str[i] == '0')
        continue;
      else if (i > standing)
        invited += (i - standing), standing += ((str[i] - '0') + i - standing);
      else if(standing >= i)
        standing += (str[i] - '0');
      //cout << standing << endl;
    }
    cout << "Case #" << ++ct << ": " << invited << endl;
  }
}
