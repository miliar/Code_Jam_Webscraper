#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

void redirectIO(string fileName)
{
   static ofstream fout ((fileName + ".out").c_str());
   static ifstream fin ((fileName + ".in").c_str());
   cin.rdbuf(fin.rdbuf());
   cout.rdbuf(fout.rdbuf());
}

bool isPalindrome(unsigned long long a)
{
   stringstream ss;
   ss << a;
   string str = ss.str();

   unsigned N = str.size();
   if (N == 1)
      return true;

   bool ret = true;
   for (unsigned i = 0; i <= N/2; ++i)
   {
      if (str[i] != str[N-1-i])
      {
         ret = false;
         break;
      }
   }
   return ret;
}

int main()
{
   redirectIO("test");

   unsigned T;
   unsigned long double A, B;
   cin >> T;

   typedef vector<pair<unsigned long double, unsigned long double> > Cont;
   vector<unsigned> numbers(T,0);
   Cont rangs;

   for (unsigned i = 0; i < T; ++i)
   {
      cin >> A >> B;
      rangs.push_back(make_pair(A, B));
   }

   unsigned long double big, small;
   for (unsigned i = 0; i < T; ++i)
   {
      small =  static_cast<unsigned long long>(ceil(sqrt(rangs[i].first)));
      big = static_cast<unsigned long long>(floor(sqrt(rangs[i].second)));
      for ( unsigned long long j = small; j <= big; ++j)
      {
         if (isPalindrome(j) && isPalindrome(j*j))
         {
            ++numbers[i];
         }
      }
   }

   for (unsigned i = 0; i < T; ++i)
   {
      cout << "Case #"<<i+1<<": "<<numbers[i]<<endl;
   }
 
   return 0;
}