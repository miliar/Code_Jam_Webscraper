#include <bits/stdc++.h>

using namespace std;
typedef pair<double, double> pi;
typedef pair<int,pi> pii;
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
const ll MOD = 1e9 + 7;

#define MAXN 200100
#define _PI 3.14159265358979323846
/*
#define N_bit 32
vector<string> jamcoin;


ll _sieve_size;
bitset<MAXN> bs;  
vi primes;  

// first part
void sieve(ll upperbound) {          
  _sieve_size = upperbound + 1;                   
  bs.set();                                            
  bs[0] = bs[1] = 0;                                   
  for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
    for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
    primes.push_back((int)i); 
} }                                           

bool isPrime(ll N) {                 
  if (N <= _sieve_size) return bs[N];                  
  for (int i = 0; i < (int)primes.size(); i++)
    if (N % primes[i] == 0) return false;
  return true;                    
}         

bool jamcoin(int num)
{
	//aggiungiamo 1 all'inizio e alla fine
	num = (num<<1) + 1 + (1<<(N_bit-1)));
	
	ull res;
	for (int i = 2; i <= 10; i++) // in ogni base
	{
		res = 0;
		ull molt = 1;
		for (int j = 0; j < N_bit; j++){
			if ( num & (1<<j)) res+= i;
			molt *= i;
		}
		
	}
}
*/
int main(int argc, char **argv)
{
	freopen("output.txt","w",stdout);
	freopen("input.txt","r",stdin);

	int T; cin>>T;
	int caseN = 1;
	while (T--)
	{
		cout<<"Case #"<<caseN++<<": ";
		
		ull K,C,S; cin>>K>>C>>S;
		ull mm = 1;
		for (int i = 0; i < C-1; i++) mm*=K;
		for (int i = 0; i < S; i++) cout<<(mm*i)+1<<" ";
		cout<<"\n";
		
	}
	return 0;
}

