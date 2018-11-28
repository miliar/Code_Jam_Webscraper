// gcjA.cpp
#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using namespace boost::multiprecision;
typedef unsigned long long int lint;

void get_primes(vector<lint> &primes, lint Max_prime);

int main()
{

	
	ifstream infile("input.in");  //this code uses a modified input file where N=16
	ofstream OF("output.txt");
	OF << "Case #1:" << endl;
	int T, N, J;
	infile >> T;
	infile >> N >> J;

	lint Max_prime = 30000;  //largest prime to allow
	vector<lint> primes;
	primes.push_back(2);
	get_primes(primes, Max_prime);

	cout << primes.size() << endl;
	int ifound = 0;
	char buf[50];
	for (lint i = pow(2,N-1)+1; i < pow(2,N); i+=2){
		vector<cpp_int> div;
		div.resize(0);
		itoa(i,buf,2);
		//cout << buf << endl;
		string sbuf(buf);
		//cout << "sbuf" << endl;
		//cout << sbuf << endl;
		int iflag = 0;

		
		

		for (int ibase = 2; ibase < 11; ibase++) {
			//cout << sbuf << " " << ibase << endl;
			cpp_int tt = ibase;
			for (int i = 0; i < 30; i++) { tt *= ibase; }
			lint nbuf = stoll(sbuf, nullptr, ibase);
			cpp_int num = nbuf + tt;
			//cout << sbuf << " " << ibase << " "<<num<<endl;

			for (lint ip = 0; ip < primes.size(); ip++) {
				if (primes[ip] >= num) break;
				if (!(num%primes[ip])) {
					div.push_back(primes[ip]);
				//	cout << "div by "<<primes[ip] << endl;
					iflag = 1;
					break;
				}
			}
			if (!iflag) break;
			
		}

		if (iflag&&div.size()==9) { 
			//OF << buf;
			OF <<1000000000000000<< buf;
			cout << 1000000000000000 << buf;
			for (int idiv = 0; idiv < 9; idiv++) {
				OF << " " << div[idiv];
				cout << " " << div[idiv];
			}
			OF << endl;
			cout << endl;
			if (++ifound == J) exit(0);
			//cout << div.size() << endl;
		}


	}

	return 0;
}


void get_primes(vector<lint> &primes, lint Max_prime) {
	cout << "finding primes...";
	for (lint i = 3; i < Max_prime; i += 2) {
		for (lint j = 0; j < primes.size(); j++) {
			if (!(i%primes[j])) break;
			if (j == primes.size() - 1) {
				primes.push_back(i);
				break;
			}
		}
		
	}

	cout << "done." << endl;
}