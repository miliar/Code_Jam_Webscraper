#include <iostream>
#include <vector>
using namespace std;
#include <cstdio>

typedef long long int ll;

vector<int> eratosthenes (int n){
	vector<int> primes(n);
	primes[0] = primes[1] = 0;
	for (int i = 2; i < n; i++) primes[i] = i;
	for (int i = 2; i < n; i++)
		if (primes[i])
			for (int j = i<<1; j < n; j += i) primes[j] = 0;
	vector<int>::iterator it = remove(primes.begin(), primes.end(), 0);
	primes.erase(it, primes.end());
	return primes;
}

long long int isPrime(ll x){
  for(long long int i = 2; i * i <= x; i++){
    if((x % i) == 0) return i;
  }
  return -1;
}



long long int change(string &str, int d){
  long long int res = 0LL;
  long long int k = 1LL;
  for(int i = 0; i < str.size(); i++){
    res += (str[i] - '0') * k;
    k *= d;
  }
  return res;
}

int main(void){
  int cnt = 0;
  int t;
  cin >> t;
  int a, b;
  cin >> a >> b;
  
  for(int ll = 0; ll < t; ll++){
    cout << "Case #" << ll + 1 << ":" << endl;
    for(int i = 32769; i < 65536; i+=2){
      if(cnt == 50) break;
      string i2 = "";
      int k = i;
      while(k){
        int w = k / 2;
        i2 += '0' + k - w * 2;
        k = w;
      }
      //reverse(i2.begin(), i2.end());
      vector<long long int> ans;
      //cout << i << " " << endl;
      for(int i = 2; i <= 10; i++){
        long long int x = isPrime(change(i2, i));
        //cout << i <<  "  " << x << endl;

        if(x == -1) break;
        ans.push_back(x);
      }
      reverse(i2.begin(), i2.end());
      if(ans.size() == 9){
        cout << i2;
        for(int i = 0; i < ans.size(); i++){
          cout << " " << ans[i];
        }
        cout << endl;
        cnt++;
      }
    }
  }
}
