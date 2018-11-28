#include <iostream>
#include <vector>

using namespace std;

int solve(int n){
  if(n==0) return 0;
  vector<bool> cnted(10, false);
  int cnt = 0, num = 0;
  while(cnt < 10){
    num += n;
    int tmp = num;
    while(tmp > 0){
      int c = tmp % 10;
      if(!cnted[c]){
        cnted[c] = true;
        cnt++;
      }
      tmp /= 10;
    }
  }
  return num;
}
int main(){
  int kase;
  cin >> kase;
  int k = 0;
  while(k < kase){
    int n, res;
    cin >> n;
    res = solve(n);
    if(res==0){
      cout<<"Case #"<<(k+1)<<": INSOMNIA"<<endl;
    }
    else{
      cout<<"Case #"<<(k+1)<<": "<<res<<endl;
    }
    k++;
  }
  return 0;
}
