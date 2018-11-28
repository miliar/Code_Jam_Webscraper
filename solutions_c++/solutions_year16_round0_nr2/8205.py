#include <cstdio>
#include <iostream>
using namespace std ;
char s[1000000];
int change( char s[], int p, char aim ) {
     if ( p == 0 )
        return 0;
     if ( aim == s[p-1] )
        return change(s,p-1,aim);
     else {
          int sum = '+' + '-' ;
          return 1 + change(s,p-1,sum - aim);
     }
}
void work() {
     cin >> s ;
     int l = strlen(s);
     cout << change(s,l,'+') << endl;
}

int main() {
    
    int T ;
    cin >> T ;
    for ( int cases = 1 ; cases <= T ; ++cases ) {
        cout << "Case #" << cases << ": "; 
        work();
    }
    
    return 0;
} 
