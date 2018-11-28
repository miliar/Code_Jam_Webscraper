#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

bool Palin(int );

int main()
{
   int T, a, b, nr;
   double root;
   cin >> T;
   for (int caseNo = 1; caseNo <= T; ++caseNo) {
      cin >> a >> b;
      nr = 0;
      
      for (int i = a; i <= b; ++i)
         if (Palin(i) && abs( (root = sqrt(i)) - (int) root) < 0.00001
             && Palin(root))
            nr ++;
      cout << "Case #" << caseNo << ": " << nr << '\n';
   }
   return 0;
}

bool Palin (int nr)
{
   vector<int> digits;
   while (nr) {
      digits.push_back(nr % 10);
      nr /= 10;
   }
   int n = digits.size();
   for (int i = 0; i < n / 2; ++i)
      if (digits[i] != digits[n - i - 1])
         return false;
   return true;
}
