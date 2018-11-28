#include <bits/stdc++.h>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  ifstream ifs("B-large.in");
  ofstream ofs("B-large_output.txt");
  int t, tcase = 1;
  //cin >> t;
  ifs >> t;

  while(t--){
    string s;
    //cin >> s;
    ifs >> s;
    s += "0";
    int cont = 0;
    int size = s.size();

    for(int i = 0; i < size;){
      if(s[i] == '-'){
        while(i < size and s[i] == '-') ++i;
        while(i < size and s[i] == '+') ++i;
        cont += 1;
      }
      else{
        bool flag = 0;
        while(i < size and s[i] == '+') ++i;
        while(i < size and s[i] == '-') ++i, flag = 1;
        if(flag) cont += 2;
        s[i-1] = '+';
      }
      if(s[i] == '0') break;
      --i;
    }

    //cout << "Case #" << tcase++ << ": " << cont << "\n";
    ofs << "Case #" << tcase++ << ": "  << cont << "\n";
  }
  return 0;
}
