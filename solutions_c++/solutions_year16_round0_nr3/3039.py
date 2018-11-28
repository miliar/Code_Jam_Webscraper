// Example program
#include <iostream>
#include <string>
#include <tgmath.h>

using namespace std;

int main() {
  long T,N,J;
  string s;
  string divs;
  long long x;
  long long d;
  bool jam;
  int carry = 0;

  T = 1;
  N = 16;
  J = 50;

  int c = 0;
  s = "1000000000000001";
  //s = "10000000001";
  cout << "Case #1:\n";

  while ( c < J) {
  //for (int kk=0; kk<20; kk++) {
    jam = true;
    divs = "";
    for (int j=2; j<11;j++) {
      //cout << s << "\n";
      x = stoull(s,0,j);
      //cout << x << " ";
      
      if (jam) {
        d = 1;

        for (long long k=2; k<100; k++) {
          if (x%k == 0) {
            d = k; 
            k = x;
          } 
        }

        if (d == 1) { jam = false; j=11;}
      }
      //cout << x << "/" << d << " ";
      divs += to_string(d) + " ";
    }

    if (jam) {
      cout << s << " ";
      cout << divs << "\n";
      c++;
    } else {
      //cout <<  s << " is not a jamcoin!\n";
    }

    carry = 0;
    for (int j=1; j<N-1; j++) {
      if (s[N-1-j] == '0') { 
        s[N-1-j] = '1'; 
        carry = 0;
      } else {
        s[N-1-j] = '0';
        carry = 1;
      }
      if (carry == 0) {j = N;}
    }
  }
}

void C() {
	long T,N,l,c;
	string S;
	char x;

	cin >> T;
	for (int i=0; i<T; i++) {
		cin >> S;
		c = 1;
		l = S.length();
		x = S[l-1];

		if (x == '+') { c--; }

		//cout << l << " " << S[0] << "\n";
		for (int j=0; j<l; j++) {
			//cout << x << " " << (S[l-j-1]) << "\n";
			
			if (x != S[l-j-1]) {
				c++;
				x = (S[l-j-1]);
				//cout << "c++\n";
			}
			
		}

		if (c < 0) { c = 0; }
		cout << "Case #" << i+1 << ": " << c << "\n";
	}
}

void D() {
  long T;
  long N;
  long K, C, S;

  cin >> T;
  for (int i=0; i<T; i++) {
  	cin >> K >> C >> S;
  	if (S < K) {
  		cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
  	} else {
	  	//cout << K << " " << C << " " << S << " \n";
	  	cout << "Case #" << i+1 << ":";
	  	for (int j=0; j<S; j++) {
	  		cout << " " << j+1;
	  	}
		cout << "\n";
  	}
  }
}

void A(){
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