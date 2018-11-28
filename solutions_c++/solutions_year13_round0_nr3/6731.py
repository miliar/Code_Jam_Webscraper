#include <iostream>
#include <sstream>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    stringstream sstr;
    
    in.open("inp.txt");
    out.open("out.txt");
    
    
    int t;
   
    
    int a, b;
    
    int is[1001];
    is[1] = 1;
    
    string s;
    for ( int i = 1; i <= 1000; i++ ) is[i] = 0;
    is[1] = 1;
    for ( int i = 2; i*i <= 1000; i++ ) {
        sstr << i;
        sstr >> s;
        
        int ch = 1;
        for ( int  j = 0; j < s.size()/2; j++ ) {
            if ( s[j] != s[s.size()-1-j] ) ch = 0;
        }
        
        sstr.clear();
        if ( ch ) {
             sstr << i*i;
             sstr >> s;
             for ( int  j = 0; j < s.size()/2; j++ )
                   if ( s[j] != s[s.size()-1-j] ) ch = 0;
             if ( ch ) is[i*i] = 1;             
        }              
    } 
    
     in >> t;
    for ( int i = 1; i <= t; i++ ) {
        in >> a >> b;
        int x = 0;
        for ( int j = a; j <= b; j++ ) {
          if ( is[j] ) x++;
        }
        out <<  "Case #" << i << ": " << x << endl;
    }
    
    
 //   system("pause");
    return 0;
}        
        
