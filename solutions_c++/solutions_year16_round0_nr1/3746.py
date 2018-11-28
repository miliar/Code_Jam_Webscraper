#include<bits/stdc++.h>

using namespace std;

long long int res;

long long int count_digit(long long int val, long long int *digit){

  while(val){
    if(digit[val%10] == 0){
      digit[val%10] = 1;
      res++;
    }
    val /= 10;
  }

}

int main(){

  long long int T, N, cases = 1;
  cin>>T;
  while(T--){

    map<long long int, long long int> values;
    long long int digit[10] = {0}, i = 1, proxy_N = 0;

    cin>>N;
    res = 0;
    proxy_N = N;
    while(values.find(proxy_N) == values.end() && res < 10){
      count_digit(proxy_N, digit);
      values[proxy_N] = 1;
      i++;
      proxy_N = N * i;
    }

    if(res == 10)
      cout<<"Case #"<<cases++<<": "<<proxy_N - N<<endl;
    else
      cout<<"Case #"<<cases++<<": INSOMNIA"<<endl;
  }

  return 0;
}
