#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

long long isPrime(long long X){
	for (long long i=2; i<=sqrt(X); i++){
		if (X%i==0){
			return i;
		}
	}
	return 0;
}

long long getDecimal(long long base, long long X){
	long long dec = 0;
	long long weight = 1;

	while(X>0) {
		if (X%2) {
			dec += weight;
		}
		X/=2;
		weight *= base;
	}

	return dec;
}

string getBinaryStr(long long X){
	string str;

	while(X>0){
		if (X%2) {
			str.push_back('1');
		}else {
			str.push_back('0');
		}
		X /= 2;
	}
	reverse(str.begin(), str.end());
	return str;
}


int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("Coinjam_Sevag.out");

	long long T, N, J;

	cin>>T>>J>>N;

	long long lim = (1LL<<(J-2)) - 1;
	long long upper = (1LL<<(J-1));
	long long numFound=0;
	
	cout<<"Case #1:"<<endl;
	for (long long i=0; i<=lim; i++){
		long long candidate = upper + (i<<1) + 1;
		vector<long long> certs;
		for (long long b=2; b<=10; b++) {
			long long div = isPrime(getDecimal(b, candidate));
			if (div==0) {
				break;
			}else {
				certs.push_back(div);
			}
		}
		if (certs.size()==9){
			numFound++;
			cout<<getBinaryStr(candidate)<<' ';
			for (long long j=0; j<certs.size(); j++) {
				cout<<certs[j]<<' ';
			}
			cout<<endl;
		}
		if (numFound==N){
			break;
		}
	}


	return 0;
}