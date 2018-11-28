#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

string get_s(int x , int r , int c){
    string s1 = "RICHARD";
    string s2 = "GABRIEL";
    if (r*c%x != 0) return s1;

    if (x == 3){
       if (r == 1) return s1;
    }
    if (x == 4){
        if (r == 1 || r == 2) return s1;
    }
      return s2;
}
int t , x , r , c;
int main(){
    freopen("4.in" , "r" , stdin);
    freopen("4.out" , "w" , stdout);
    cin >> t;
    for ( int cas = 1; cas <= t; ++ cas){
        cin >> x >> r >> c;
        if (r > c) swap(r , c);
        printf("Case #%d: %s\n" , cas , get_s(x , r , c).c_str());
    }
}
