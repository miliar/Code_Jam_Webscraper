#include<iostream>
#include<vector>
#include<algorithm>
#include<cstddef>
#include<bitset>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/miller_rabin.hpp>
#include <iomanip>

using namespace std;
using namespace boost::random;
using namespace boost::multiprecision;

#define Number 1000000

unsigned long long Prime[Number];
unsigned long long PrimeCount = 0;
void GenerateList()
{
  Prime[0] = 2;
  Prime[1] = 3;
  Prime[2] = 5;
  Prime[3] = 7;
  Prime[4] = 11;
  PrimeCount = 5;

  for(unsigned long long Test = 13 ; PrimeCount < Number ; Test+=2)
  {
    bool IsPrime = true;
    for(unsigned long long PrimeIndex = 0 ; Prime[PrimeIndex] <= std::sqrt(Test) ; ++PrimeIndex )
    {
      if( Test % Prime[PrimeIndex] == 0)
      {
        IsPrime = false;
        break;
      }
    }
    if(IsPrime)
      Prime[PrimeCount++] = Test;
  }
}
int main()
{
  GenerateList();
  std::vector<unsigned long long> Primes(Prime,Prime+Number);
//  cout << "IN" << endl;

  typedef cpp_int int_type;
  boost::random::mt11213b base_gen(clock());
  boost::random::independent_bits_engine<mt11213b, 256, int_type> gen(base_gen);
  //
  // We must use a different generator for the tests and number generation, otherwise
  // we get false positives.
  //
  boost::random::mt19937 gen2(clock());

  unsigned long long Test;
  cin >> Test;
  for(unsigned long long tt=1 ; tt<=Test ; tt++)
  {

    unsigned long long Size, Count;
    cin >> Size >> Count;

    cout << "Case #"<< tt << ": " << endl;
    string Start = "1" ;
    while(Start.size()!=Size-1) Start +="0";
    Start+="1";

//    cout << "Start" << endl;
    char * End;
    unsigned long long StartNumber = strtoull(Start.c_str(),&End,2);
    unsigned long long Found = 0;
    for(unsigned long long ii = StartNumber; Found < Count ; ii+=2)
    {
      bool IsJam = true;
      string Binary = bitset<128>(ii).to_string().substr(128-Size,Size);
      for(unsigned long long Base = 2 ; Base <= 10 ; Base++)
      {
        unsigned long long Test = strtoull(Binary.c_str(),&End,Base);
        if(Test > Prime[Number-1])
        {
          if(miller_rabin_test(Test, 25, gen2))
          {
            IsJam = false;
            break;
          }
        }
        else
        {
          if(binary_search(Primes.begin(),Primes.end(),Test))
          {
            IsJam = false;
            break;
          }
        }
      }
      if(IsJam)
      {
        Found++;
        string Binary = bitset<128>(ii).to_string().substr(128-Size,Size);
        cout << Binary;
        for(unsigned long long Base = 2 ; Base <= 10 ; Base++)
        {
          unsigned long long Test = strtoull(Binary.c_str(),&End,Base);
          for(unsigned long long ff = 0 ; ff < Number ; ff++)
          {
            if(Test % Prime[ff] == 0)
            {
//              cout << " " << Test  << ":" << Prime[ff];
              cout << " " << Prime[ff];
              break;
            }
          }
        }
        cout << endl;
      }
    }
//    cout << "Case #"<< tt << ": " << "INSOMNIA" << endl;
  }
  return 0;
}
