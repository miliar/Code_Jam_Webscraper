#include <cstdio>
    #include <cstring>
    #include <algorithm>
    #include <bits/stdc++.h>
#include <iostream>
#include <fstream>
    using namespace std ;
    int a[1200] ;
    int main() {
        ofstream myfile;
	myfile.open ("Pancakes.txt");
        int t , step = 0 ;
        int n , i , j , max1 , min1 , sum ;
        freopen("1.in","r",stdin) ;

        scanf("%d", &t) ;
        while( t-- ) {
            scanf("%d", &n) ;
            for(i = 0 ; i < n ; i++) {
                scanf("%d", &a[i]) ;
                max1 = max(max1,a[i]) ;
            }
            min1 = max1 ;
            for(i = 1 ; i <= max1 ; i++) {
                sum = i ;
                for(j = 0 ; j < n ; j++) {
                    if( a[j] > i ) {
                        if( a[j]%i == 0 )
                            sum += (a[j]/i-1) ;
                        else
                            sum += (a[j]/i) ;
                    }
                }
                min1 = min(min1,sum) ;
            }
             myfile<<"Case #"<<++step<<": "<<min1<<endl;

        }
        myfile.close();
        return 0 ;
    }
