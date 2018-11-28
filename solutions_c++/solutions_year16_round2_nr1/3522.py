#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std ;
const int maxn = 100000;
char str[maxn];
char numbers[10][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int cnt[30] = {0};
int cntChar[10][30] = {0};
int ans[10];

bool end() {
     for ( int i = 0 ; i < 30 ; ++i)
         if ( cnt[i] != 0 ) 
            return false;
     return true;
}

bool dfs() {

     if ( end() )
        return true;
     for ( int i = 0 ; i < 10 ; ++i ) {
         bool fail = false;
         for ( int j = 0 ; j < 30 ; ++j )
             if ( cntChar[i][j] > cnt[j] )
                fail = true; 
         
         if  ( !fail )  {
             for ( int j = 0 ; j < 30 ; ++j )
                 cnt[j] -= cntChar[i][j] ;
             ans[i]++;
             if ( dfs() )
                return true;
             ans[i]--;
             for ( int j = 0 ; j < 30 ; ++j )
                 cnt[j] += cntChar[i][j] ;
             
         }
     } 
     return false;
}

void work() {
     cin >> str ;
     
     for ( int i = 0 ; i < 30 ; ++i )
         cnt[i] = 0 ;
         
     int l = strlen(str);
     for ( int i = 0 ; i < l ; ++i ) {
         cnt[ str[i]-'A' ] ++ ;
     }
     for ( int i = 0 ; i < 10 ; ++i )
         ans[i] = 0 ;
     if ( dfs() == false)
        cout << "error" << endl ;
     
     
     for ( int i = 0 ; i < 10 ; ++i )
         for ( int j = 0 ; j < ans[i] ; ++j )
             cout << i ; 
     cout << endl ;
}

int main() {
    
    
    for ( int i = 0 ; i < 10 ; ++i )
        for ( int j = 0 ; j < strlen( numbers[i] ) ; ++j )
            cntChar[i][ numbers[i][j]-'A' ]  ++ ;
    
    int T ;
    cin >> T ;
    for ( int cases = 1 ; cases <= T ; ++cases ) {
        cout << "Case #" << cases << ": "; 
        work();
    }
    
    return 0;
} 
