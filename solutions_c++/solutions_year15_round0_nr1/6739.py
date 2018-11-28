#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
   freopen("cj.in", "rt", stdin);
   freopen("cj.out", "wt", stdout);
   
   int n;
   cin >> n;
   for (int i = 0; i < n; ++i) {
      
      int smax;
      cin >> smax;
      
      string audi;
      cin >> audi;
      
      int standing = 0;
      int totalInvite = 0;
      for (int j = 0; j < smax+1; ++j) {
         int nrAudi = (audi[j]-'0');
         if (nrAudi > 0 && standing < j) {
            for (int k = 1;;++k) {
               if (standing+k >= j) {
                  totalInvite += k;
                  standing += k;
                  break;
               }
            }
         }
         standing += nrAudi;
      }
      
      cout << "Case #" << i+1 << ": " << totalInvite << endl;
   }
   
   return 0;
}
