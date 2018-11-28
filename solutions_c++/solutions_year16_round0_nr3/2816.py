#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

#define small 
//#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;

int evenDivisor(ll num){
  //returns 0 if in is prime and otherswise an even divisor (except 1 & in)
  ll posDiv = 2;
  ll sqrtIn = sqrt(num);
  //  std::cerr << "evenDivisor | in: " << num << " posDiv: " << posDiv << " sqrtIn: " << sqrtIn << "\n";
  while(posDiv <= sqrtIn){
    if(num % posDiv == 0)
      return posDiv;
    posDiv++;
  }
  return 0;
  //feasable
}

bool isPrime(int& in){
  return(evenDivisor(in) == 0);
}

vi transform2Base2(int in){
  //transforms in (which is in base 10) 2 base 2
  int newBase = 2;
  vi out;
  while(in > 0){
    out.insert(out.begin(), in%newBase);
    in /= newBase;
  }
  return out;
}

ll transform2Base10(vi& in, int inBase){
  //transforms in (which is in base inBase) 2 base 10
  ll out = 0;
  for (int i = 0; i < in.size(); i++) {
    out += in[in.size()-1-i]*pow(inBase, i);
  }
  return out;
}

bool isJamcoin(int coin, vi &coinInB2, vi &divisors){
  //returns true if coin interpreted base between 2 and 10, inclusive, the resulting number is not prime.
  coinInB2 = transform2Base2(coin);
  std::cerr << coin << " in binary is ";
  for (auto& i : coinInB2)
    std::cerr << i;
    std::cerr << ".\n";
  for (int i = 2; i <= 10; i++) {
    ll b10ForThisBase = transform2Base10(coinInB2, i);
    //std::cerr << "Calling evenDivisor().. ";
    int divisor = evenDivisor(b10ForThisBase);
    //std::cerr << " ..returned.\n";
    if(divisor == 0){ //for some base coin is prime
      std::cerr << "The represantation of this interpreted as base " << i << " is " << b10ForThisBase << " which is prime. Or isn't it?\n"; 
      return false;
    }
    divisors[i-2] = divisor;
  }
  return true;     
}

int main()
{
#if defined(small)
  int N = 16;
  int J = 50; 
#elif defined(large)
  int N = 32;
  int J = 500;
#endif
  freopen("out.out", "w", stdout);
  printf("Case #1:\n");

  int coin = pow(2, N-1)+1;
  while(J > 0){
    //std::cerr << "coin: " << coin << "\n";
    vi coinInB2(N);
    vi divisors(9);
    if(isJamcoin(coin, coinInB2, divisors)){
      J--;
      for(auto& i: coinInB2)
	printf("%d", i);
      for(auto& i: divisors)
	printf(" %d", i);
      printf("\n");

      for(auto& i: coinInB2)
	std::cerr << i;
      for(auto& i: divisors)
	std::cerr << " " << i;
      std::cerr << "   (J = " << J << ")" << std::endl;
    }
    coin += 2;
  }

  /*
  std::cerr << "Calling now evenDivisor(4)\n";
  std::cerr << "evenDivisor(4): " << evenDivisor(4) << "\n";

  std::cerr << "Now let N = 6;\n";
  N = 6;
  vi coinInB2(N);
  vi divisors(9);
  std::cerr << "isJamcoin(55) [55 is 110111 in binary | F] = " << isJamcoin(55, coinInB2, divisors) << "\n";
  std::cerr << "isJamcoin(35) [35 is 100011 in binary | T] = " << isJamcoin(35, coinInB2, divisors) << "\n";
  std::cerr << "isJamcoin(63) [63 is 111111 in binary | T] = " << isJamcoin(63, coinInB2, divisors) << "\n";
  std::cerr << "isJamcoin(57) [57 is 111001 in binary | T] = " << isJamcoin(57, coinInB2, divisors) << "\n";
  */

  return 0;
}
