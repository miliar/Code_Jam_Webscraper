#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

void bincount(string& num);
long isprime(long n);
long frbase(string n, int base);

int main() {
	ifstream in;
	ofstream out;
	string fname, num;
	cout << "Input file: ";
	cin >> fname;
	
	in.open(fname.c_str());
	out.open("outtest.txt");
	
	int T, N, J;
	
	in >> T;
	
	for (int j = 0; j < T; j++) {
		out << "Case #" << j+1 << ":\n";
		int count = 0;
		bool wegucci = true;
		
		in >> N >> J;
		string rusl = string(N-2,'0');
		
		while (count < J && wegucci) {
			string jimis = '1' + rusl + '1';
			bool jc = true;
			long div[9];
			
			for (int i = 2; i <= 10; i++) {
				long cur = frbase(jimis, i);
				cout <<jimis<<" " <<i<<" "<< cur << " ";
				div[i-2] = isprime(cur);
				cout << div[i-2] << endl;
				if (div[i-2] == cur) {
					jc = false;
					break;
				}
			}
			
			if(jc){
				out << jimis;
				for (int i = 0; i < 9; i++) {
					out << " " << div[i];
				}
				out << endl;
				count++;
			}
			
			bincount(rusl);
			wegucci = !(rusl == "");
		}
		
	}
	
	return 0;
}

void bincount(string& num){
	for (int i = num.length()-1; i >= 0; i--) {
		if (num[i] == '0') {
			num[i] = '1';
			
			for (int j = i + 1; j < num.length(); j++)
				num[j] = '0';
			
			break;
		}
		
		if (i == 0 && num[i] == '1') {
			num = "";
			break;
		}
	}
	
}

long isprime(long n){
	long lim = (long) sqrt(n);
	
	for (long k = 2; k <= lim; k++) {
		if(n%k == 0)
			return k;
	}
	
	return n;
}

long frbase(string n,int base){
	long sum = 0;
	int j = 0;
	for (int i = n.length()-1; i >= 0; i--) {
		sum += (n[i] - '0')*pow(base,j);
		j++;
	}
	
	return sum;
}