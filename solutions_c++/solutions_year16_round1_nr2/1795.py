#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
	ifstream cin("r2.in") ;
	ofstream cout("rout2.txt") ;
    int64_t tt ;
    cin >> tt ;
    for(int64_t T = 1 ; T <= tt ; T ++) {
        int64_t arr[2501] = {0} ;
        int64_t m , rti , tmp , y , z ;
        cin >> m ;
        y = m ;
        m = ((m * 2) - 1) ;
        for(rti = 1 ; rti <= m ; rti ++) {
            for(z = 0 ; z < y ; z ++) {
                cin >> tmp ;
                arr[tmp] ++ ;
            }
        }
        cout << "Case #" << T << ":" ;
        for(rti = 1 ; rti < 2501 ; rti ++) {
            if(arr[rti] % 2 != 0)
                cout<< " " << rti ;
        }
        cout<<"\n";
    }
    return 0 ;
}
