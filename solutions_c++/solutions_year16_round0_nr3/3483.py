#include <iostream>
#include <fstream>
#include <bitset>
#include <string>

using namespace std;

ifstream fin  ("jamcoin.in");
ofstream fout ("jamcoin.out");

int divk;

bool isPrime(long long int n, long long int k){
    if(n<2) return true;
    if(n==2) return true;
    if(n%2 == 0){
    	divk = 2;
    	return false;
    }
    for(long long int i = 3; (i*i) <= n; i++){
        if(n%i == 0 ){
        	divk = i;
        	return false;
        }
    }
    return true;
}

bool is_prime(string S, int k){
	long long int n = strtol(S.c_str(), NULL, k);
	return isPrime(n,k);
}

int main(){
	unsigned int T;
	int N; int J;
	string S;

	fin >> T;

	for(int t = 0; t < T; t++){
		fout << "Case #" << t+1 << ": " << endl;
		fin >> N >> J;
		
		int count = 0;
		
		for(size_t n = (1<<N-1) + 1; n < 1<<N; n+=2){
			if(count >= J) break;			
			S = bitset<32>(n).to_string();
			S = S.substr(32-N, N);
						
			int divs[11] = {0};

			bool notprime = true;
			for(int k = 2; k <= 10; k++){
				if(is_prime(S,k)){
					notprime = false;
					break;
				}
				divs[k] = divk;
			}

			if(notprime == true){
				for(int k = 2; k <= 10; k++){
					long long int l = strtol(S.c_str(), NULL, k);
					cout << l << " ";
				}
				cout << endl;

				count++;
				fout << S;
				fout << " " << divs[2] << " " << divs[3] << " " << divs[4];
				fout << " " << divs[5] << " " << divs[6] << " " << divs[7];
				fout << " " << divs[8] << " " << divs[9] << " " << divs[10];
				fout << endl;
			}
		}
	}

	return 0;
}