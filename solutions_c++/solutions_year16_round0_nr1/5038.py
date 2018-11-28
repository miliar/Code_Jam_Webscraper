#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

typedef long long int ll;

int main(){
	ll num, n;
	string line;
	getline(cin,line);
	istringstream ss(line);
	ss >> num;
	//cin >> num;

	for (int i = 0; i <= num-1; i++){
		//cin >> n;
		getline(cin,line);
		istringstream ss(line);
		ss >> n;
		int mult = 1;
		int counter[10];
		for (int j = 0; j <= 9; j++){
			counter[j] = 0;
		}
		bool breakcheck;

		ll m;

		do {
			breakcheck = 1;
			m = mult*n;
			//cout << "m:" << m << endl;

			if (m < 10){
				counter[m] = 1;
			}

			else{
			  while(m > 10){
			  	  //cout << "(floor(log10(m)))" << endl;
			  	  //int l = m/(10*(floor(log10(m))));
			  	  int pin = pow(10,(floor(log10(m))));
			  	  int l = m/pin;
			  	  //cout << "(10*(log10(m) -1))" << (10*(log10(m) -1)) << endl;
			  	  //cout << "l:" << l << endl;
				  counter[l] = 1;
				  if ((floor(log10(m)) - floor(log10(m % pin))) == 2){
				  	counter[0] = 1;
				  }
				  m = (m % pin);
				  if (m < 10){
				    counter[m] = 1;
			      }
			  }

			  if (m == 10){
			  	counter[1] = 1;
			  	counter[0] = 1;
			  }
		    }

			mult++;

			for (int j = 0; j <= 9; j++){
				//cout << "counter" << j << "=" << counter[j] << endl;

			  if (counter[j] == 0){
				breakcheck = 0;
			  }
		    }

		    if (n == 0){
		    	breakcheck = 1;
		    }
		}while(breakcheck == 0);

		cout << "Case #" << (i+1) << ": ";
		if (n == 0){
			cout << "INSOMNIA" << endl;
		}
		else{
			cout << (mult-1)*n << endl;
		}
	}
}