#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int num_of_case = 1;
void output(string str){
  cout << "Case #" << num_of_case << ": " << str << endl;
  num_of_case++;
}

void output(ll str){
  cout << "Case #" << num_of_case << ": " << str << endl;
  num_of_case++;
}

bool isUsedAll(vector<bool> &used){
  for(size_t i=0; i < used.size(); i++){
    if(used[i] == false){
      return false;
    }
  }
  return true;
}

int main(void){
  int NUM;
  cin >> NUM;
  while(NUM--){
    int N; cin >> N;
    vector<bool> used(10, false);
    if( N == 0 ){
      output("INSOMNIA");
      continue;
    }

    ll mul = 1;
    ll ans;
    while(!isUsedAll(used)){
      ll tmp = N * mul;
      ans = tmp;
      while(tmp != 0){
        used[ tmp%10 ] = true;
        tmp /= 10;
      }
      mul++;
    }
    output(ans);
  }
  return 0;
}
