#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
using namespace std;

const unsigned long HI = 100000000;//65536;
bool primes[HI+1]; //primes[i] = 1 iff i is prime

void fill_primes(unsigned hi)
{
  for (bool & b : primes)  {b = 1;}
  primes[0] = false;
  primes[1] = false;
  unsigned long c = 2;
  unsigned long top = sqrt(hi);
  while(c <= top)
  {
    if (primes[c])
    {
      //remove all multiples of c
      unsigned long mc = c+c;
      while (mc <= HI)  {primes[mc] = false; mc+=c;}
    }
    c++;
  }
}

void output_primes(unsigned hi)
{
  for (unsigned long i=1; i <= hi; i++)
  {
    if (primes[i])  {cout << i << endl;}
  }
}

bool ones_or_zeros(unsigned long i)
{
  stringstream ss;
  ss << i;
  string s = ss.str();
  //make sure last character is a one
  if (s.back() != '1')  {return false;}

  return (all_of(s.begin(), s.end(), [](char c) {return (c=='0' || c=='1');}));
}

string base10i_2s(unsigned long i)
{
  string res = "";
  while (i > 0)
  {
    int r = i%2;
    res.push_back('0' + r);
    i -= r;
    i /= 2;
  }

  reverse(res.begin(), res.end());
  return res;
}

unsigned pfactor(unsigned long k)
{
  //cout << "factoring " << k << endl;
  for (unsigned long i=2; i < ceil(sqrt(k)); i++)
  {
    if (primes[i])
    {
      if (k % i == 0)  
      {
        //cout << "looks like " << i << " divides " << k << ", since (k % i) is " << (k%i) << endl;
      return i;
      }
    }
  }
  return 1;
}

bool check_jamcoin(string x)
{
  //check that x is non-prime in all bases 2..10
  //if so, output x and non-trivial divisors

  //x is a string of ones and zeros
  unsigned long factors[9]; //factor[i] is a factor in base i+2
  for (int b=2; b <= 10; b++)
  {
    unsigned long k = 0;
    for (int i=0; i < x.size(); i++)
    {
      k += (x[x.size()-1-i] - '0')*pow(b,i);
    }
    //cout << "in base " << b << ", " << x << " is "  << k << endl;

    unsigned long f = pfactor(k);
    if (f == 1)  {return false;}
    else  {factors[b-2] = f;}
  }

  cout << x << ' ';
  for (unsigned i : factors)  {cout << i << ' ';}
  cout << endl;
  return true;
}

void tick()
{
  int ndig,ncoins;
  cin >> ndig;
  cin >> ncoins;

  fill_primes(HI);

  set<string> candidates2; //all non-primes in base2
  for (long i=pow(2,ndig-1); i <= pow(2,ndig); i++)
  {
    if (!primes[i] && (i % 2 == 1) && ceil(log2(i)) == ndig)
    {
      //convert to base 2 and add to candidates
      candidates2.insert(base10i_2s(i));
    }
  }

  //check candidates
  int ncoinsfound = 0;
  for_each(candidates2.begin(), candidates2.end(), [&](string x)  
  {
    if (ncoinsfound < ncoins)
    {
      if (check_jamcoin(x))  {ncoinsfound++;}
    }
  });
}

int smain()
{
  fill_primes(HI);
  check_jamcoin("1000000011101011");
  return 0;
}

int main()
{
  int bigN;
  cin >> bigN;
  for (int i=0; i < bigN; i++)
  {
    cout << "Case #" << (i+1) << ": " << endl;
    tick();
  }
  return 0;
}
