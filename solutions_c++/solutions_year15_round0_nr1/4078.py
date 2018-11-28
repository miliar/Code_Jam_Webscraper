#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
   int x;
   cin >> x;
   for(int i = 0; i < x; i++)
   {
      int m;
      cin >> m;
      std::string s;
      cin >> s;
      vector< int > sum;
      for(int j = 0; j < m; j++)
      {
         if( j == 0 )
            sum.push_back(  s[j] - '0' );
         else
            sum.push_back( *sum.rbegin() + (s[j] - '0') );
      }
      
      int max = 0;
      for(int j = 1; j <= m; j++)
      {
         if( j - sum[j-1] > max )
            max = j - sum[j-1];
      }
     
    //  std::cout << m << " " << sum << std::endl;
      std::cout << "Case #" << i+1 << ": " << max << std::endl;
   }
}