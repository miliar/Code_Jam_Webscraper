#include <bits/stdc++.h>
#include <fstream>
using namespace std;
ifstream fentrada("B-large.in");
ofstream fsalida("respuestaBlarga.out");

int main(){
    int t; fentrada >> t;
    for( int i = 1 ; i <= t ; ++i ){
        string s; fentrada >> s;
        int c = 0;
        char comp = '+';
        for( int j = (int)s.size()-1 ; j >= 0 ; j-- ){
            if( s[j] != comp ){
                comp = s[j];
                c++;
            }
        }
        fsalida << "Case #"<< i << ": " << c << '\n';
    }
}
