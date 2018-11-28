#include <iostream>  
using namespace std; 
long long calc(long long n){
	int a[10] = {0};
	int cnt = 0 ;
	int i =1 , rem;
	long long m ;
	long long temp = n;
	while(cnt < 10){
		n = i * temp;
		m = n;
		while(m){
			rem = m%10;
			if(a[rem] == 0) { cnt++; a[rem]=1;}
			m = m/10;
		}
		i++;
	}
	return n;
} 
int main() {
  int t;
  long long n;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if(n == 0){
        cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
    else{
    	cout << "Case #" << i << ": " << calc(n) << endl;
    }
  }
}