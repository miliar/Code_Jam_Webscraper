#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cmath>
using namespace std;
long N = 60000000;

int main(){

	vector<long> primes;
	vector<bool> composite(N+1, false);
	int temp;
	cin>>temp>>temp>>temp;
	primes.push_back(2);

	for(long p = 2; p <= N; p += 2) composite[p] = true;

	for(long p = 3; p <= 8000; p += 2){
		if(composite[p]) continue;
		primes.push_back(p);
		for(long i = p*p; i <= N; i += p) composite[i] = true;
	}

	for(int p = 8000; p <= N; p++) if(!composite[p]) primes.push_back(p);

	// for(int p : primes) cout<<p<<" is prime"<<endl;

	// cout<<"size of primes is "<<primes.size()<<" and last prime is "<<primes[primes.size()-1]<<endl;
	
	map<string, vector<long> > M;

	int count = 0;

	for(int i = 0; i < 1<<16; i++){

		count = M.size();
		if(count >= 50) break;

		string s(1, '1');
		for(int j = 0; j < 14; j++){
			if(i & (1<<j)){ // jth bit is set in i
				s += '1';
			}
			else s += '0';
		}
		s += '1';
		
		vector<long> v; //holding divisors of n
		
		for(long b = 2; b <= 10; b++){
			
			long n = 0;
			for(long p = 0; p < 16; p++)
				if(s[p] == '1') n += pow(b, 15-p);

			// cout<<"value of "<<s<<" in base "<<b<<" is "<<n<<endl;

			for(int p : primes){
				if(p >= n) break;
				if(n%p == 0){
					v.push_back(p);
					break;
				}
			}
		}

		if(v.size() == 9){
			// cout<<"found prime "<<s<<endl;
			M[s] = v;
		}
	}
	cout<<"Case #1:"<<endl;
	for(auto &kv : M){
		cout<<kv.first;
		for(int i : kv.second) cout<<" "<<i;
		cout<<endl;
	}

}