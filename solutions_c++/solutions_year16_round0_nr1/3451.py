#include <iostream>

using namespace std;

bool seen[10];

bool check(){
  for(int i = 0; i < 10; i++){
    if(!seen[i]){return false;}
  }
  return true;
}

int test(int n){
  int c = 0;
  while(!check()){
    c++;
    int a = c*n;
    while(a != 0){
      seen[(a%10)] = true;
      a /= 10;
    }
  }
  return c;
}

int main(){
  int N; cin >> N;
  for(int i = 0; i < N; i++){
    int b; cin >> b;
    cout << "Case #" << i+1 << ": ";
    if(b == 0){cout << "INSOMNIA" << endl;}
    else{cout << b*test(b) << endl;}
    for(int j = 0; j < 10; j++){seen[j] = false;}
  }
  return 0;
}
