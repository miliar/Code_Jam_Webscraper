#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

typedef long long int ll;

bool is_prime(int num){
	bool check = 1;
	for (int i = 2; i <= sqrt(num); i++){
		if ((num % i) == 0){
			check = 0;
			break;
		}
	}

	return check;
}

int main(){
	ll T,num, N, J;
	//#if 0
	string line;
	getline(cin,line);
	istringstream ss(line);

	ss >> num;
	for (int i = 0; i <= 0; i++){
		getline(cin,line);
	    istringstream ss(line);
		ss >> N;
		ss >> J;
	}
	//#endif
	//cout << num << endl;
	//cout << N << endl;
	//cout << J << endl;

	#if 0
	num = 1;
	N = 16;
	J = 50;
	#endif

	ll a[J][10];
	int dp[N];
	dp[0] = 1;
	dp[N-1] = 1;

	int count = 0;
	int check;
	ll pin;
	int test;

	while(count < J){
	  test = 0;
	  check = 1;
	  for (int i = 1; i <= N-2; i++){
		dp[i] = rand()%2;
	  }


	  for (int i = 2; i <= 10; i++){
	  	pin = 0;
	  	for (int j = 0; j <= N-1; j++){
	  		pin += dp[j]*pow(i,j);
	  	}
	  	if (is_prime(pin) == 1){
	  		check = 0;
	  		break;
	  	}
	 
	  	for (ll j = 2; j <= sqrt(pin); j++){
	  		if ((pin % j) == 0){
	  			a[count][i-1] = j;
	  			test += i;
	  			break;
	  		}
	  	}
	  }

	  if (check == 0){
	  	for (int j = 2; j <= 10; j++){
	  		a[count][j-1] = 0;
	  	}
	  }

	  //cout << pin << endl;
	  for (int i = 0; i <= count-1; i++){
	  	if (a[i][0] == pin){
	  		check = 0;
	  	}
	  }

	  if (check == 1){
	  	//cout << "test" << test << endl;
	  	if (test == 54){
	    a[count][0] = pin;
	    count++;
	    }
	  }
	  //cout << "count:" << count << endl;
	}
	#if 0
	for (int i = 0; i <= count-1; i++){
		cout << a[i][0] << endl;
	}
	#endif

	cout << "Case #1:" << endl;
	for (int i = 0; i <= count-1; i++){
		for (int j = 0; j <= 9; j++){
			cout << a[i][j] << " ";
		}
		cout << endl;
	}

}