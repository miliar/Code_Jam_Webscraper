#include <iostream>

using namespace std;

bool a[10];

void init(){
  for(int i = 0 ; i < 10 ; i++)
    a[i] = false;
}

bool check(){
  for(long long int i = 0 ; i < 10 ; i++)
    if(!a[i])
      return false;
  return true;
}

void output(long long int x , long long int n){
  cout << "Case #" << x << ": ";
  if(n == 0)
    cout << "INSOMNIA";
  else{
    long long int b = n;
    init();
    while(!check()){
      long long int y = n;
      while(y > 0){
	a[y%10] = true;
	y /= 10;
      }
      if(check())
	break;
      n += b;
    }
    cout << n;
  }
  cout << endl;
}

int main(){
  long long int t , n;
  cin >> t;
  for(long long int i = 0 ; i < t ; i++){
    cin >> n;
    output(i+1 , n);
  }
  return 0;
}
