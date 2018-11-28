
#include <iostream>
#include <vector>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <string.h>
#include <assert.h> 

using namespace std;


char ctbl[10] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };

class palin_sq{
public:
	palin_sq(string min, string max)
		:mins(min),
		maxs(max),
		palinsq_count(0)
	{
 		mpz_init(mmin);
 		mpz_set_str(mmin, min.c_str(), 10);

 		mpz_init(mmax);
 		mpz_set_str(mmax, max.c_str(), 10);

		// We only need to go till the sqrt(mmax)
 		mpz_init(sqrtmmax);
		mpz_sqrt (sqrtmmax, mmax);

		// We only need to go till the sqrt(mmax)
 		mpz_init(sqrtmmin);
		mpz_sqrt (sqrtmmin, mmin);
	}

	~palin_sq()
	{
 		mpz_clear(mmin);
 		mpz_clear(sqrtmmin);
 		mpz_clear(sqrtmmax);
 		mpz_clear(mmax);
	}

	int count_palin_sq();

private:

	int gen_palindrome(char *c, int pos, int size);
	bool check_palinsq(mpz_t &pal);
	bool check_palindrome(char *c, int size);

	int palinsq_count;
	string mins, maxs;
	mpz_t mmin;
	mpz_t mmax;
	mpz_t sqrtmmax;
	mpz_t sqrtmmin;
};

bool palin_sq::check_palindrome(char *c, int size)
{
	int clen = strlen(c);
	assert(size>clen);
	for(int i=0; i < (clen/2+1); ++i)
	{
		if ( c[i] != c[clen-i-1] )
		{
			// not palindrome.. stop and return false
			return false;
		}
	}

	return true;
}


bool palin_sq::check_palinsq(mpz_t &pal)
{
	mpz_t result;
	mpz_init(result);
	mpz_mul(result, pal, pal);

	if (mpz_cmp(result, mmax)>0)  {
		// beyond range. ignore
		mpz_clear(result);
		return false;
	}

	if (mpz_cmp(result, mmin)<0)  {
		// beyond range. ignore
		mpz_clear(result);
		return false;
	}

	bool is_palin_sq = false;

	char cStr[110];
	char *pStr;
	memset(cStr, 0, sizeof(cStr));
	pStr = mpz_get_str (cStr, 10, result);

	is_palin_sq = check_palindrome(pStr, 110);
			
	mpz_clear(result);
	return is_palin_sq;
}

int palin_sq::gen_palindrome(char *c, int pos, int size)
{
	if ( pos>=(size/2)) {
		int ret;
		// We got a palindrome
		// NULL terminate it
		if((size%2 
			&& (pos%2) && (size>1))||((0==pos)&&(1==size))) {
			// When size is odd and pos is the middle even index

			// This loop takes care of the middle most odd index
			for(int i= pos==0?1:0;
				i < 10; ++i) {
				c[pos]=ctbl[i];

				ret = gen_palindrome(c, pos+1, size);
				if ( ret < 0 )	{
					if ( i=0 ) {
						// This means that all the numbers are going to beyond the max
						// propogate the error up  the state
						return -1;
					}

					break;
				}
			}
			return 0;
		}

		c[size]=0;

		mpz_t pal;
 		mpz_init(pal);
	 	mpz_set_str(pal, c, 10);

		/*
		// Makesure that the value is not bigger than mmax or smaller than mmin
		if (mpz_cmp(pal, mmin) < 0) {
			// beyond range. ignore
 			mpz_clear(pal);
			return 0;
		}
		*/

		if (mpz_cmp(pal, mmax)>0) {
			// beyond range. stop at this position
 			mpz_clear(pal);
			return -1;
		}

		if ( check_palinsq(pal) ) {
			palinsq_count++;	
		}
 		
		mpz_clear(pal);
		return 0;
	}

	int ret;
	for(int i= pos==0?1:0;
		i < 10; ++i) {
		c[pos]=ctbl[i];
		c[size-pos-1]=ctbl[i];

		ret = gen_palindrome(c, pos+1, size);
		if ( ret < 0 ) {
			
			if ( i=0 ) {
				// This means that all the numbers are going to beyond the max
				// propogate the error up  the state
				return -1;
			}

			break;
		}
	}
	return 0;
}

int palin_sq::count_palin_sq()
{
	int maxDigits = maxs.length();
	char palC[100+1];

	char cStr[110];
	char *pStr;
	memset(cStr, 0, sizeof(cStr));
	pStr = mpz_get_str (cStr, 10, sqrtmmin);
	int minDigits = strlen(pStr);

	memset(palC, 0, sizeof(palC));

	for(int i=minDigits; i < maxDigits+1; ++i) {
		gen_palindrome(palC, 0, i);
	}

	return palinsq_count;
}

int main(void)
{
	int n;
	cin>>n;

	for(int i=0; i < n; ++i) {
		string min, max;
		cin>>min;
		cin>>max;
		
		palin_sq ps(min, max);

		int count = ps.count_palin_sq();

		cout <<"Case #"<<i+1<<": "<<count<<endl;
	}

	return 0;
}

