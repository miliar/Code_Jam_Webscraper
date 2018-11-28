#include <bits/stdc++.h>
using namespace std ;

int main() {
	ifstream cin("r1.in") ;
	ofstream cout("rout1.txt") ;
    int t ;
    cin >> t ;
    for(int x= 1 ; x <= t ; x++) {
        string str;
        cin >> str ;
        char str1[3000] ;
        int len = str.length() ;
        str1[1050] = str[0] ;
        int j = 1050 ;
        int m = 1050 ;
        char chr = str[0] ;
        for(int k = 1 ; k < len ; k ++) {
           if(str[k] >= chr)  {
              j = j-1 ;
              str1[j] = str[k];
              chr = str[k];
           } else {
                m = m + 1 ;
                str1[m] = str[k] ;
            }
        }
        cout << "Case #" << x << ": " ;
       for(int i = j ; i<= m ; i++) {
            cout << str1[i];
        }
        cout << "\n";
    }
    return 0;
}
