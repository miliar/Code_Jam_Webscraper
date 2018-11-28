#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;


void get_digits(int x, set<int> &digits){
  do{
    int a = x % 10;
    digits.insert(a);
    x = x/10;
  } while(x > 0);
}



int main(){

  int total_tests;
  cin >> total_tests;
  int s,q;
  for(int i = 1; i <= total_tests; i++){
    long long n; //
    set<int> digits;

    cin >> n;
    int count = 1;
    long long last = 0;
    while(digits.size() < 10 && n != 0 ){
      last = n * count++;
      get_digits(last,digits);

    }

    if(n == 0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    else cout<<"Case #"<<i<<": "<<last<<endl;


   
  }


  return 0;
}