#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;
int main()
{
	int t , n ;
   cin >> t ;
   string s ;
   for (int i =  1  ; i<= t ; i++ )
   {
       int sum = 0  , nas = 0 ;
       cin >> n >> s ;
       for (int j = 0 ; j< s.size(); j++ )
       {
           if (sum < j ) {nas += j - sum ; sum +=(j - sum ) ; }
           sum += int(s[j])-48 ;
       }
       cout<<"Case #"<<i<<": "<<nas<<endl;
   }
}
