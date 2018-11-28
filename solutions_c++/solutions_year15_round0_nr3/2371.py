#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long LL;

//*******************
int repeat, counter;   
string letters;
char mapl[128];
//*******************

int sgn(int x) {
   return (x > 0) ? 1 : ((x < 0) ? -1 : 0);
}

int mul(int a, int b) {
   if(abs(a) == 1 || abs(b) == 1)
      return a * b;
   int sign = sgn(a) * sgn(b);
   if(abs(a) == abs(b))
      return -1 * sign;

   if(abs(a) == 2) {
      if(abs(b) == 3) return 4 * sign;
      if(abs(b) == 4) return -3 * sign;
   }
   if(abs(a) == 3) {
      if(abs(b) == 2) return -4 * sign;
      if(abs(b) == 4) return 2 * sign; 
   }
   if(abs(a) == 4) {
      if(abs(b) == 2) return 3 * sign;
      if(abs(b) == 3) return -2 * sign;
   }
   return 0;
}

inline int compute_result(int begin, int end) {
   int result = 1;
   for(int i = begin; i < end; ++i)
      result = mul(result, mapl[letters[i]]);
   return result;
}

bool possible() {
   vector<int> ipos, kpos;
   int result = 1;
   for(int i = 0; i < letters.size(); ++i) {
      result = mul(result, mapl[letters[i]]);
      if(result == mapl['i'])
         ipos.push_back(i);
   }
   result = 1;
   for(int k = letters.size()-1; k >= 0; --k) {
      result = mul(mapl[letters[k]], result);
      if(result == mapl['k'])
         kpos.push_back(k);
   }
   for(int i : ipos) {
      int result = 1;
      int last = i+1;
      for(int k : kpos) {
         while(last < k) 
            result = mul(result, mapl[letters[last++]]);
         if(result == mapl['j'])
            return true;
      }
   }
   return false;
}

string solve() {
   cin >> counter >> repeat;
   string letters_init;
   cin >> letters_init;
   letters = "";
   letters.reserve(letters_init.size() * repeat);
   for(int i = 0; i < repeat; ++i)
      letters += letters_init;
   if(possible())
      return "YES";
   return "NO";
}

int main() {
   ios::sync_with_stdio(false);
   mapl['i'] = 2;
   mapl['j'] = 3;
   mapl['k'] = 4;
   int T;
   cin >> T;
   for(int i = 1; i <= T; ++i)
      cout << "Case #" << i << ": " << solve() << endl;
   return 0;
}