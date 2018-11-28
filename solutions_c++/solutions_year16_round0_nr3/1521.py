//Joe Snider
//4/16
//
//qual c (jamcoin)

#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <iterator>
#include <math.h>

using namespace std;

void disp(const vector<int>& x) {
   copy(x.begin(), x.end(), ostream_iterator<int>(cout, " "));
   //cout << "\n" << flush;
}

long long toVal(const vector<int>& jamcoin, const long long& base) {
   long long ret = 0;
   for(int i = 0; i < jamcoin.size(); ++i) {
      //only 0,1 for digits
      ret += (jamcoin[i]==0)?0:pow(base, jamcoin.size()-1-i);
   }
   return ret;
}

//return a factor or -1 if it's prime
long long factor(const long long n) {
   if (n%2 == 0) {return 2;}
   int m = sqrt(n);
   //could speed up by checking only primes (precalc hint?, this is fast enough)
   for(long long i = 3; i <= m; i += 2) {
      if(n%i == 0) {return i;}
   }
   return -1;
}

//return (b^p) mod m
int modPow(int b, int p, const long long m) {
   int ret = 1;
   int bm = b%m;
   
   while(p > 0) {
      ret = (ret * bm) % m;
      --p;
   }
   
   return ret % m;
}

//directly check the jamcoin since it's overflowing (10^32 is too big, mod to the rescue)
long long modFactor(const vector<int>& jamcoin, const int& base) {
   //hack a cutoff to see if we can get 500
   long long cutoff = 1000;
   int n = jamcoin.size();
   for(long long i = 2; i < cutoff; ++i) {
      int val = 0;
      for(int j = 0; j < n; ++j) {
         val += (jamcoin[j]==0)?0:modPow(base, jamcoin.size()-1-j, i);
         val = val%i;
         //cout << "gh1 " << val << " " << j << "\n" << flush;
      }
      if( val == 0) {return i;}
   }
   return -1;
}

int main() {
//cout << "gh1 " << modPow(3,3,10) << "\n\n\n";

   int N = 32;
   int J = 500;
   
   cout << "Case #1:\n" <<flush;
   vector<int> jamcoin(N);
   jamcoin[0] = 1;
   jamcoin[N-1] = 1;
   for(long long i = 0; i < 1<<(N-2); ++i) {
      int m = 1;
      for(int j = 0; j < N-2; ++j) {
         jamcoin[j+1] = (m&i)?1:0;
         m <<= 1;
      }
      vector<long long> factors;
      for(int j = 2; j <= 10; ++j) {
         //for small
         //long long test = toVal(jamcoin, j);
         //long long q = factor(test);
         //for large
         long long q = modFactor(jamcoin, j);
         //cout << "gh0 " << test << " " << q << "\n" << flush;
         if (q < 0) {break;}
         factors.push_back(q);
      }
      if(factors.size() == 9) {
         copy(jamcoin.begin(), jamcoin.end(), ostream_iterator<int>(cout, ""));
         cout << " ";
         copy(factors.begin(), factors.end(), ostream_iterator<long long>(cout, " "));
         cout << "\n" << flush;
         --J;
         if(J==0) {return 0;}
      }
   }
   
   return 0;
}
