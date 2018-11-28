#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <math.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text



long long isPrime(long long n){
	long long sqrtOfn = floor(sqrt(n));

	if(n % 2 == 0) {
		return 2;
	}

	for(long long i = 3; i < sqrtOfn; i+= 2){
		if(n % i == 0){
			return i;
		}
	}
	return -1;
}

void q3(int i, int n, int j){
  	cout << "Case #" << i << ":" << endl;
	long long num = 1;
	num <<= (n-1);
	num++;

  	long long numbers[9];

  	while(j > 0){
  		bool found = true;

  		for(int q = 0; q < 9; ++q){
  			long long sum = 0;
  			long long w = num;
  			long long add = 1;

  			while(w != 0){

  				if((w & 1) != 0){
  					sum += (long long)add;
  				}
  				add *= (q+2);
  				w >>= 1;
  			}

  			numbers[q] = isPrime(sum);
  			if(numbers[q] == -1){
  				found = false;
  				break;
  			}

  		}

  		if(found){
  			long long mask = 1;
  			mask <<= (n-1);
  			while(mask != 0){
  				cout << (mask & num ? "1" : "0");
  				mask >>= 1;
  			}
  			cout << " ";

  			for(int q = 0; q< 9; ++q){
  				cout << numbers[q] << " ";
  			}
  			if(--j != 0)cout << endl;
  		}

  		num += 2;
  	}
}

int main() {
  int t, n, j;
  string str;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

  for (int i = 1; i <= t; ++i) {
    cin >> n >> j;
    q3(i, n, j);
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
