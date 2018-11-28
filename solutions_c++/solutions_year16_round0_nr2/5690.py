#include <cmath>
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
    int count = 0 ;
        for( int j = 0 ; j < s.size() - 1 ; j++)
            {
             if(s[j] != s[j+1] ) count++ ;
        }
        if( s[s.size() - 1] == '-') count++ ;
        
        cout << "Case #" << i + 1 << ": " << count << endl ;
    }
    
   
  return 0;
}