// Example program
#include <iostream>
#include <string>

using namespace std;

int main(){
  long T;
  long N;
  long digits[10];
  int min = 0;
  long k;
  long x;

  cin >> T;

  for (int i=0; i<T; i++) {
  	cin >> N;
  	//cout << "N: " << N << "\n";

  	for (int j=0; j<10; j++) {
  		digits[j] = 0;
  		//cout << digits[j] << " ";
  	}
  	//out << "\n";
  	k = 0;
  	min = 0;

  	if (N == 0) {
  		cout << "Case #" << i+1 << ": " << "INSOMNIA\n";
  	} else {
  		while (min < 1) {
  			k++;
  			x = N*k;
  			//cout << x << " ";
  			while (x >= 1) {
  				digits[x%10]++;
  				x /= 10;
  			}
  			min = 1;
  			for (int j=0; j<10; j++) {
		  		if (digits[j] < min) min = digits[j];
		  	}
  		}
  		cout << "Case #" << i+1 << ": " << N*k << "\n";
  	}
  }
}

void kokotina() {
	cout << "ZLE JE!\n";
}