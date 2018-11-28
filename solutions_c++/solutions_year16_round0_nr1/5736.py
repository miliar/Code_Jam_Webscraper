#include <bits/stdc++.h>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  ifstream ifs("A-large.in");
  ofstream ofs("A-large_output.txt");
  int t, tcase = 1;
  ifs >> t;

  while(t--){
    long long n, aux;
    set<int> st;
    bool flag = 0;
    int index = 1;

    ifs >> n;
    if(n == 0) flag = 1;
    while(st.size() < 10 and !flag){
      aux = n*(index++);
      while(aux) st.insert(aux%10), aux /= 10;
      if(index > 1000) flag = 1;
    }

    ofs << "Case #" << tcase++ << ": ";
    if(flag) ofs << "INSOMNIA\n";
    else ofs << n*(index-1) << "\n";
  }
  return 0;
}
