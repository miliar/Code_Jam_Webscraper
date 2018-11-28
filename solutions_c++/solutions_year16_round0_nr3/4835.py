#include<iostream>
#include<vector>
#include<cmath>
#include<cstdint>
using namespace std;
#define MAXPRIME 100000000
#define BITS 16
vector<uint64_t> primes;

uint64_t pow(uint64_t base, uint64_t exp)
{
  if(exp == 0)
    return 1;
  if(exp % 2 == 0)
    {
      uint64_t temp = pow(base, exp / 2);
      return temp * temp;
    }
  else
    {
      uint64_t temp = pow(base, exp - 1);
      return temp * base;
    }
}

uint64_t basevalue(int base, bitset<BITS> bits)
{
  uint64_t num = 0;
  for(int i=0; i < BITS; i++)
    {
      num += bits[i] * pow(base, i);
    }
  return num;
}

pair<bool, vector<uint64_t> > check_primes(bitset<BITS> &binary, const vector<uint64_t> primes)
{
  vector<uint64_t> factors;
  for(int base = 2; base <= 10; base++)
    {
      uint64_t num = basevalue(base, binary);
      for(auto p : primes)
        {
          if(p * p > num)
            break;
          if(num % p == 0)
            {
              factors.push_back(p); 
              break;
            }
        }
    }
  return make_pair(factors.size() ==  9, factors);
}

int main()
{
  vector<bool> isPrime(MAXPRIME, true);
  isPrime[1] = true;
  for(uint64_t p=2; p * p < MAXPRIME; p++)
    {
      if(isPrime[p] == true)
        {
          for(uint64_t j = p * p; j < MAXPRIME; j += p)
            isPrime[j] = false;
        }
    }
  for(uint64_t p=2; p < MAXPRIME; p++)
    {
      if(isPrime[p])
        primes.push_back(p);
    }

  int t;
  cin>>t;
  uint64_t N;
  cin>>N;
  uint64_t J;
  cin>>J;
  cout<<"Case #1:"<<endl;
  int count = 0;
  for(int i=0; i < pow(2, BITS - 2); i++)
    {
      if(count >= J)
        break;
      bitset<BITS> binary = bitset<BITS>(i);

      binary <<= 1;
      binary[0] = 1;
      binary[BITS - 1] = 1;
      pair<bool, vector<uint64_t> > check = check_primes(binary, primes);
      if(check.first)
        {
          count++;
          cout<<binary.to_string()<< " ";
          for(int j=0; j < check.second.size();j++)
            cout<<check.second[j]<< " ";
          cout<<endl;

        }
    }
}

