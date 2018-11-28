#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
using namespace std;

int non_triv_div(long n)
{
   long threshold = 10000;
   long last=0;
   for (long i=2; i<=min(threshold, n/2); ++i) {
      if ((n % i) == 0) {
         last = i;
         break;
      }
   }
   return last;
}


int main()
{
   int n, j, one;
   cin >> one;
   cin >> n >> j;
   cout << "Case #1:" << endl;
   int count = 0;

   for (int i=0; i< pow(2, (n-2)); ++i) {
      bitset<32> b(i);
      vector<int> ntdivs(9, 0);
      string jamcoin = "1" + b.to_string().substr(34-n) + "1";
      bool bad_number = false;
      for (int base = 2; base <=10; ++base) {
         long ntd = non_triv_div(stol(jamcoin, nullptr, base));
         if (ntd == 0) {
             bad_number = true;
             break;
         }
         ntdivs[base-2] = ntd;  
      }
      if (bad_number) {
         continue;
      }
      cout << jamcoin;
      for (auto ntd: ntdivs) {
         cout << " " << ntd;
      }
      //cerr << endl;
      //for (int base = 2; base <=10; ++base) {
      //   cerr << stol(jamcoin, nullptr, base) << " ";
      //}
      //cerr << endl;
      cout << endl;
      if (++count == j) {
         return 0;
      }
   }
   return 0;
}
