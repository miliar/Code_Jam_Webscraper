#include <cmath>
#include <cstdio>
#include <math.h>
#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;




int main() {
  int T ;
    cin >> T ;
    for( int i = 0 ; i < T ; i++)
        {
        string s ;
        cin >> s ;
        cout << "Case " << "#" << i+1 << ": " ;
        string maxstr = "" ;
        maxstr += s[0] ;
        for( int j = 1 ; j < s.size() ; j++)
            {
              if( s[j] >= maxstr[0]) { string prefix = "" ;
                                       prefix += s[j] ;
                                 prefix += maxstr ;
                                 maxstr = prefix ;}
             else maxstr += s[j] ;
        }
         cout << maxstr << endl ;
    }
  return 0;
}