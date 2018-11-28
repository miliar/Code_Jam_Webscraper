#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#define ll long long int
using namespace std;
 
int main() {
	ifstream cin("rql2.in") ;
	ofstream cout("routl2.txt") ;
    ll tt ;
    cin >> tt ;
    for(ll T = 1 ; T <= tt ; T ++) {
        ll arr[2501] = {0} ;
        ll m , x , tmp , y , z ;
        cin >> m ;
        y = m ;
        m = ((m * 2) - 1) ;
        for(x = 1 ; x <= m ; x ++) {
            for(z = 0 ; z < y ; z ++) {
                cin >> tmp ;
                arr[tmp] ++ ;
            }
        }
        cout << "Case #" << T << ":" ;
        for(x = 1 ; x < 2501 ; x ++) {
            if(arr[x] % 2 != 0)
                cout<< " " << x ;
        }
        cout<<"\n";
    }
    return 0 ;
}
