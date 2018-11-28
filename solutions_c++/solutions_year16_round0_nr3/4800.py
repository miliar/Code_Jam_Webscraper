#include <iostream>
#include <sstream>
#include <string>
#include <math.h>
#include <string.h>
#include <bitset>

#define mp(a, b) make_pair(a, b)
typedef long long ll;
using namespace std;


ll isPrime(ll a){

	for (ll i = 2; i < sqrt(a); i++){
		if (a%i == 0){
			return i;
		}
	}
	return 1;
}

int main(){
	long  in;
	ll inc[11];
	int N, J;
	int st,end;
	int num;
	int count = 0;
	cin >> num;


	for (int i = 0; i < num; i++){//
		
		cin >> N>>J;
		
		//init

		cout << "Case #" << i + 1 << ":" << endl;

		//out num
		for (int j = (1 << (N-1)); j < (1 << N); j++){//base 2
			int breakflag = 0;
			if (j % 2 != 1 || j >> (N-1) != 1){// 1111
				continue;
			}
			cerr << static_cast<std::bitset<16>>(j) << endl;
			
			//base 2-10 
			for (int k = 2; k <= 10; k++){
				ll num10 = 0;
				ll tmp = j;
				for (int keta = 0; keta < N; keta++){
					num10 += tmp % 2*(ll)powl(k,keta);
					tmp = tmp >> 1;
				}
				cerr << num10<< " ";
				ll pr = isPrime(num10);
				if (pr == 1){
					breakflag = 1;
					break;
				}
				else{
					inc[k] = pr;//2-10
				}
				
			}
			cerr<<endl;
			if (breakflag == 0){
				cout << static_cast<std::bitset<16>>(j);
				for (int k = 2; k <= 10; k++){
					cout << " " << inc[k];
				}
				cout << endl;
				count++;
			}
			if (count == J){
				break;
			}
		}

		

	}


	return 0;
}