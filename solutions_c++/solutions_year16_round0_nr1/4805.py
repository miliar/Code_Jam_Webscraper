#include <iostream>

using namespace std;

int allpresent(int (&p)[10], int n){
  while(n > 0){
    p[n % 10] = 1;
    n /= 10;
  }
  for(int i = 0; i < 10; i++){
    if(!p[i]){
      return 0;
    }
  }
  return 1;
}

int main(){
  ios::sync_with_stdio(false);
  int t;
  long long n;
  cin >> t;
  for(int q = 1; q <= t; q++){
    cin >> n;
    if(n == 0){
      cout << "Case #" << q << ": INSOMNIA" << endl;
      continue;
    }
    int p[10] = {0};
    int num = n;
    int i = 2;
    while(!allpresent(p, num)){
      num = n * i;
      i++;
    }
    cout << "Case #" << q << ": " << num << endl;
  }
  return 0;
}