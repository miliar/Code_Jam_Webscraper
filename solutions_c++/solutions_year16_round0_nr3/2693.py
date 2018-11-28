#include <iostream>
#include <vector>
using namespace std;

vector<long long> divisors, primes;

long long change(long long N, int base){
	long long ans=0LL, b=1LL;
	while(N>0){
		ans += ((N&1)*b);
		b*=base;
		N>>=1;
	} return ans;
}
bool prime(long long N){
	for(unsigned i=0;i<primes.size()&&primes[i]*primes[i] <= N;i++){
		if(N%primes[i]==0){divisors.push_back(primes[i]);return false;}
	} return true;
}
inline void print_jam(long long N){
	string S;
	while(N>0){S.push_back((N&1)+'0');N>>=1;}
	for(unsigned i=0;i<S.size()-1-i;i++)
		swap(S[i],S[S.size()-1-i]);
	cout << S << " ";
}

void solve(int bits, int J){
	long long base, n, nn, N, j = 0;
	for(n=0;n<(1LL<<(bits)) && (j < J);n++){
		nn=(n*2+1)+(1LL<<(bits+1));
		nn = (nn<<(bits+2))+nn;
		//cout << nn << endl;
		divisors.clear();
		for(base=2LL;base<11LL;base++){
			N=change(nn,base);
		//	if(n%10==0)cout << N << endl;
			if(prime(N)){ /*cout << N << "CB" << base << endl;*/ base = 20LL; }
		}
		//cout << n << endl;
		if( base < 20 ){
			print_jam(nn);
			for(unsigned i=0;i<divisors.size();i++){
				if(i<divisors.size()-1)cout << divisors[i] << " ";
				else cout << divisors[i] << endl;
			}
			//ans[j].insert(ans[j].end(),divisors.begin(),divisors.end());
			j++;
		//	cout << j << endl;	
		}
	}// cout << j << endl;
}


inline bool is_prime(long long p){
	for(int i = 0; primes[i]*primes[i]<=p;i++)
		if(p%primes[i]==0)return false;
	return true;
}

void prime_gen(){
	long long n;
	const int MAXP=1000000;
	while(primes.size() < MAXP){
		n=primes.back()+2LL;
		while(!is_prime(n))n+=2LL;
		primes.push_back(n);
	}
}

int main(){
	int T, N, J; cin >> T;
	cout << "Case #1:\n";
	cin >> N >> J;
	primes.push_back(2LL); primes.push_back(3LL);
	prime_gen();
	solve((N/2)-2,J);///
	return 0;
}
