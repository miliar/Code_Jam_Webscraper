#include <iostream>
#include <vector>
#include <bitset>
#include <gmpxx.h> // https://gmplib.org/

using namespace std;

mpz_class divisor(mpz_class n) {
  mpz_t res, r;
  mpz_init(r);
  mpz_init_set_str(res, "1", 10);
  while(mpz_class(res) < n) {
    mpz_nextprime(res,res);
    mpz_mod(r, n.get_mpz_t(), res);
    if(mpz_class(r) == 0)
      return mpz_class (res);
  }
}

int main() {
  cout << "Case #1:" << endl;

  int J = 50;
  const short int K = (1 << 15) + 1;
  unsigned short int N;
  vector<mpz_class> nums;
  vector<mpz_class> divs;
  vector<vector<mpz_class> > _exp(9, vector<mpz_class>(16,1));
  for(int i = 1;  i < 16; ++i)
    for(int j = 2; j < 11; ++j)
      _exp[j-2][i] = _exp[j-2][i-1]*j; 
  
  for(unsigned short int mid = 1; mid < (1 << 14); ++mid) {
    N = K | (mid << 1);
    nums.assign(9,0);
    for(int i = 0; i < 16; ++i)
      if((N >> i) & 1 == 1)
	for(int j = 2; j < 11; ++j)
	  nums[j-2] += _exp[j-2][i];
    
    bool thereIsAPrime = false;
    for(int i = 0; i < 9 && !thereIsAPrime; ++i)
      if(mpz_probab_prime_p(nums[i].get_mpz_t(),2))
	thereIsAPrime = true;
    
    if(!thereIsAPrime && nums.size() > 0) {
      bitset<16> b(N);
      cout << b; 
      for(int i = 0; i < 9; ++i)
	cout << ' ' <<  divisor(nums[i]);
      cout << endl;
      --J;
      if(J == 0) break;
    }
  }
  return 0;
}
