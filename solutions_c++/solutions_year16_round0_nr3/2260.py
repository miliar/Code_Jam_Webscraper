# include <bits/stdc++.h>
using namespace std;

typedef __int128 ii;

const int T = 1;
const int N = 32;
const int J = 500;

bool isPrime(int n, vector<int> &vec)
{
	double root = sqrt(n*1.);
	for(int i=0; i<vec.size() && vec[i] <= root; ++i) {
		if (n % vec[i] == 0) {
			return false;
		}
	}
	return true;
}

void gene(vector<int> &vec)
{
	vec = {2, 3};
	for(int i=6; i<1e2; i += 6) {
		if (isPrime(i-1, vec)) vec.push_back(i-1);
		if (isPrime(i+1, vec)) vec.push_back(i+1);
	}
}

int main()
{		
	//int T; cin >> T;
	for(int T_=1; T_<=T; ++T_) {
		//int n, j; cin >> n >> j;
		
		printf("Case #1:\n");
		
		vector<int> prime;
		gene(prime);
		
		int J_ = 0;
		
		ii one = 1;
		ii fst = (one << (N-1)) +1;
		for(ii i=fst; J_ != J; i += 2) {
			bitset<N> jc(i);
			vector<int> nums;
			
			bool all = true;
			for(int k=2; k<=10 && all; ++k) {
				ii cand = 0, mul = 1;
				for(int p=0; p<N; ++p) {
					cand += mul * (jc[p] == 1);
					mul *= k;
				}
				
				bool found = false;
				for(int i=0; i<prime.size() && prime[i] < cand && !found; ++i) {
					if (cand % prime[i] == 0) {
						nums.push_back(prime[i]);
						found = true;
					}
				}
				all &= found;
			}
			
			if (all) {
				J_ += 1;
				
				printf("%s ", jc.to_string().c_str());
				for(auto num:nums) printf("%d ", num);
				printf("\n");
			}
		}
	}
	return 0;
}