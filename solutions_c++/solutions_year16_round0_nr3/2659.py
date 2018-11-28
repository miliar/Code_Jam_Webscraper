#include <iostream>

using namespace std;

long long int to2(long long int x){
  long long int res = 0;
  while(x > 0){
    res *= 10;
    res += (x % 2);
    x /= 2;
  }
  return res;
}

long long int to10(long long int x , int i){
  long long int res = 0 , j = 1;
  while(x > 0){
    res += ((x % 10) * j);
    x /= 10;
    j *= i;
  }
  return res;
}

bool isPrime(long long int a){
  for(long long int i = 2 ; i * i <= a ; i++)
    if(a % i == 0)
      return false;
  return true;
}

bool check(long long int *a){
  for(int i = 2 ; i < 11 ; i++)
    if(isPrime(a[i]))
      return false;
  return true;
}

long long int find(long long int a){
  for(long long int i = 2 ; i * i <= a ; i++)
    if(a % i == 0)
      return i;
  return 0;
}

int main(){
  int t , n , m;
  cin >> t;
  cin >> n >> m;
  cout << "Case #1:" << endl;
  for(long long int i = (1 << (n-1)) + 1 ; i < (1 << n) && m > 0 ; i += 2){
    if(!isPrime(i)){
      long long int x = to2(i);
      long long int a[11];
      for(int j = 2 ; j < 11 ; j++)
	a[j] = to10(x , j);
      if(check(a)){
	cout << x << " ";
	for(int j = 2 ; j < 11 ; j++)
	  cout << find(a[j]) << " ";
	cout << endl;
	m--;
      }
    }
  }
  return 0;
}
