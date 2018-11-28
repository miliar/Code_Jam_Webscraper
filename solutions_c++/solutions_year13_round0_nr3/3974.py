#include <iostream>
#include <cmath>

using namespace std;

const int maxn = 20;

bool palindrome(long long x){
  int a[maxn];
  memset(a, 0, sizeof a);
  int i = 0;
  while(x){
    a[i++] = x % 10;
    x /= 10;
  }
  int n = i;
  for(int i=0, j = n - 1;i < j;i++, j--)
    if(a[i] != a[j])
      return false;
  return true;
}


int main(){
  int t;
  cin >> t;
  for(int i=1;i<=t;i++){
    long long a, b;
    cin >> a >> b;
    long long ax = sqrt(a);
    if(ax * ax < a)
      ax++;
    b = sqrt(b);
    a = ax;
    long long d = 0;
    for(long long j = a;j<=b;j++)
      if(palindrome(j) && palindrome(j * j))
	d++;
    cout << "Case #" << i << ": " << d << endl; 
  }
  return 0;
}
