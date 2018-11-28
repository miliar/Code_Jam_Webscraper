#include <bits/stdc++.h>
using namespace std;
int T, N, M, K, Q, f[1005];
string str;
void ini(void){
  cin>>str>>K;
  N = str.length();
}

void sol(void){
  int sum = 0, ans = 0, tmp;
  for(int i = 0; i + K <= N; i++){
    tmp = (str[i] == '-')? 1: 0;
    if((tmp + sum) & 1){
      f[i] = 1;
      ans++;
    }else f[i] = 0;
    sum += f[i];
    //printf("f[%d] = %d, sum = %d\n", i, f[i], sum);
    if(i - K + 1 >= 0){
      sum -= f[i - K + 1];
    }
  }
  for(int i = N - K + 1; i < N; i++){
    tmp = (str[i] == '-')? 1: 0;
    if((tmp + sum) & 1){
      cout<<"IMPOSSIBLE"<<endl;
      return;
    }
    if(i - K + 1 >= 0){
      sum -= f[i - K + 1];
    }
  }
  cout<<ans<<endl;
}

int main(void){
  int i;
  cin>>T;
  for(i = 1; i <= T; i++){
    ini();
    cout<<"Case #"<<i<<": ";
    sol();
  }
}
