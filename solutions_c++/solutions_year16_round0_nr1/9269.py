#include <bits/stdc++.h>

using namespace std;

int main()
{ifstream cin("A-large.in") ;
    ofstream cout("out.txt");
    int t;
    cin >> t ;
    int cp = 1 ;

    while(t--){
         cout << "Case #" << cp++ << ": ";
        int a ;
        cin >> a ;
        if( !a) {cout << "INSOMNIA\n" ; continue ; }
        set<int> s ;
        int b =0;
        while(s.size()!=10){
            b+= a;
            int c= b ;
            while(c){
                s.insert(c%10) ;
                c/=10;
            }
        }
        cout << b << endl;
    }
    return 0;
}
