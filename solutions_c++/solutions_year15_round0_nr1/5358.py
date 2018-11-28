#include <iostream>

using namespace std;

int main(){

freopen("A-large.in","r",stdin);
freopen("A1.out","w",stdout);

 int T;
cin>>T;

for(int t=0;t<T;t++){
  int n;
  cin >> n;
  string s;
  cin >> s;
  int total = 0;
  int x = 0;
  for(int i=0;i<=n;i++){
    int y = s[i]-'0';
    if(x < i){
      total++;
      x++;
    }
    x+= y;
  }
  printf("Case #%d: %d\n", t+1, total);
}

}
