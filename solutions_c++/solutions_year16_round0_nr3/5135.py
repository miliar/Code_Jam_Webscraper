#include<iostream>
#include<string>
using namespace std;
string toBinary(unsigned long long int n) {
	string r;
	while(n!=0) {
		r=(n
		   %2==0 ?"0":"1")+r;
		n/=2;
	}
	return r;
}
int isPrime( unsigned long long int n ) {
	// check if n is a multiple of
	if ( n % 2 == 0) return 2 ;
	// if not , then just check the o
	for ( int i = 3 ; i * i <= n; i += 2 ) {
		if ( n% i == 0 )
			return i ;
	}
	return -1 ;											//-1 means it's prime
}
////////////////////////////////

int main() {
	string s, coin, cpyCoin;
	int t, n, j, z;
	bool isValid;
	unsigned long long int tmp, num;

	cin>>t;
	for(int i = 1; i <= t; i++) {
		cin>>n>>j;
		cout<<"Case #"<<i<<":"<<endl;
		coin = "1";											//Initialize the string with starting 1000000
		for(int k = 1; k < n-1; k++) {
			coin += "0";
		}
		num = stoull(coin, nullptr, 2);									//Convert it number
		while(j != 0) {
			isValid = true;
			//num += 1;													//don't increament number
			coin = toBinary(num);										//Convert it to binary number string
			cpyCoin = coin + "1";										//Add remaining 1


			for(z = 2; z <= 10; z++) {
				tmp = stoull(cpyCoin, nullptr, z);						//convert string to all baese
				if(isPrime(tmp) == -1) {									//means prime
					isValid = false;
				}
			}
			if(isValid) {										//if valid coin
				cout<<cpyCoin<<" ";
				for(z = 2; z <= 10; z++) {
					tmp = stoull(cpyCoin, nullptr, z);
					cout<<" "<<isPrime(tmp);
				}
				num += 1;
				j--;
				cout<<endl;
			} else {
				num += 1;
			}
		}
	}
}
