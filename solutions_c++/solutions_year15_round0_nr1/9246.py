#include <fstream>
int T;


int main(){
  std::fstream cin("a.in", std::fstream::in);
  std::fstream cout("a.out", std::fstream::out);
  cin >> T;
  for (int i=0; i<T; ++i){
    int a; std::string g;
    cin >> a >> g;
    cout << "Case #" << (i+1) << ": ";
    int m=0; int ans=0;
    for (int i=0;i<g.size(); ++i){ int j=g[i]-'0';
      if (m<i){++ans; ++m;}
      m+=j;
    }
    cout <<ans<< "\n";
  }
}