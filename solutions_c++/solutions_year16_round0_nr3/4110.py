#include <bits/stdc++.h>

#define MAX 200000000

using namespace std;

int primes[MAX];
int prime[MAX];

int main(){
  ios::sync_with_stdio(false);
  //cin.tie(NULL);
  //cout.tie(NULL);

  long long int cnt = 0;
  for(long long int i=2;i<MAX;i++){
    if(prime[i] == 0){
      primes[cnt++] = i;
      for(int j=i+i;j<MAX;j+=i){
        prime[j] = 1;
      }
    }
  }

  int t,n,c;
  cin >> t >> n >> c;

  long long int val = (1 << n - 1 ) + 1,temp;
  int count = 0,flag;
  long long int a[9],b[9],expo;

  cout << "Case #1:\n";

  while(count < c){
    flag = 0;
    for(int i=2;i<=10;i++){
      b[i-2] = 0;
      a[i-2] = 0;
      expo = 1;
      temp = val;
      while(temp){
        a[i-2] += (temp%2)*expo;
        temp /= 2;
        expo *= i;
      }
      for(int j=0;j<cnt;j++){
        if(a[i-2] % primes[j] == 0 && a[i-2] != primes[j]){
          b[i-2] = primes[j];
          break;
        }
      }
      if(b[i-2] == 0)
        break;
    }
    for(int i=0;i<9;i++){
      if(b[i] == 0)
        flag = 1;
    }
    if(flag == 0){
      cout << bitset<16>(val) << ' ';
      for(int i=0;i<9;i++)
        cout << b[i] << ' ';
      cout << endl;
      count++;
    }
    val += 2;
  }
  return 0;
}
