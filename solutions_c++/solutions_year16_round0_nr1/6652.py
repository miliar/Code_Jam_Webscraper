#include <iostream>

using namespace std;

typedef long long ll;
bool used[10];
void init(){
  for(int i=0;i<10;i++)used[i] = false;
}
void mark(ll n){
  if(n%10==0)used[0] = true;
  while(n>0){
    used[n%10] = true;
    n /=10;
  }
}
int main(){
  int t;
  ll n;
  cin >> t;
  for(int i=0;i<t;i++){
    cin >> n;
    init();
    cout << "Case #" << (i+1) << ": ";
    if(n==2*n){
      cout << "INSOMNIA" << endl;
    } else {
      int cnt = 1;
      while(true){
        bool f = true;
        for(int i=0;i<10;i++)f &= used[i];
        if(f)break;
        mark(n * cnt);
        cnt++;
      }
      cout << (n*(cnt-1)) << endl;
    }
  }
}
