#include <bits/stdc++.h>
using namespace std;
string to_string(int i)
{
    std::stringstream ss;
    ss << i;
    return ss.str();
}
int main(){
  int T;
  cin >> T;
  for(int C = 1; C <= T; C++){
    int cont = 0, lim = 0, No;
    long long N;
    bool vis[10];
    string str;
    memset(vis,false,sizeof vis);
    cin >> No;
    N = No;
    while(N != 0 && cont != 10 && lim < 1000000){
      str = to_string(N);
      for(int i = 0; i < str.size(); i++){
        if(!vis[str[i]-'0']){
          vis[str[i]-'0'] = true;
          cont++;
        }
      }
      N+=No;
      lim++;
    }
    printf("Case #%d: ",C);
    if(cont == 10) printf("%d\n",N-No);
    else printf("INSOMNIA\n");
  }
  return 0;
}