#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <numeric>
#include <cassert>
#include <cmath>
#include <string>
#include <set>
#include <gmp.h>

using namespace std;
typedef unsigned int uint;
typedef unsigned long long LL;

#define FOR(k,a,b) for(uint k(a); k < (b); ++k)
#define FORD(k,a,b) for(uint k(b-1); k >= (a); --k)
#define REP(k,a) for(uint k=0; k < (a); ++k)

int is_prime(mpz_t a,const vector<unsigned int>& primes)
{
	REP(i,primes.size())
	{
		if(mpz_cmp_ui(a,primes[i])>0 && mpz_divisible_ui_p(a,primes[i]))
			return i;
	}
	return -1;
}

int main (int argc, char** argv) {
	bool small = 0;
	vector<unsigned int> primes;
	vector<bool> p(1e6,1);
	FOR(i,2,1e6) if(p[i])
	{
		int k=2*i;
		while(k<1e6)
		{
			p[k]=0;
			k+=i;
		}
		primes.push_back(i);
	}
	int ms = small ? 15 : 31;
	unsigned int st = (1<<ms)+1;
	mpz_t stv,act;
	mpz_init(stv);

	mpz_t fres[505];
	vector<vector<int> > divisors;
	REP(i,505)
		mpz_init(fres[i]);
	int ctr = 0;
	int mc = small? 50: 500;
	while(ctr<mc)
	{
		mpz_set_ui(stv,st);
		char c[100];
		mpz_get_str(c,2,stv);
		int g = 0;
		vector<int> divi;
		FOR(i,2,11)
		{
			mpz_init_set_str(act,c,i);
			int tmp = is_prime(act, primes);
			if(tmp == -1)
				break;
			divi.push_back(tmp);
		}
		if(divi.size() == 9)
		{
			mpz_init_set(fres[ctr],stv);
			++ctr;
			divisors.push_back(divi);
		}
		st += 2;	
	}
	printf("Case #1:\n");
	REP(i,ctr)
	{
		char c[100];
		mpz_get_str(c,2,fres[i]);
		printf("%s",c);
		REP(j,divisors[i].size())
		{
			printf(" %d",primes[divisors[i][j]]);
		}
		printf("\n");
	}
	
	return 0;
}
