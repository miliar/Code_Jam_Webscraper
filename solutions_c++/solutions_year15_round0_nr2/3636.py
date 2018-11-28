//
//  main.cpp
//  Infinite Houser of Pancakes
//
//  Created by Yanqiao Zhan on 4/11/15.
//  Copyright (c) 2015 Yanqiao Zhan. All rights reserved.
//
/*
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int main(int argc, const char * argv[]) {
    int T;
    ifstream in("/Users/yanqiaozhan/Code/algorithmexercise/2015googlecodejam/B/B-small-attempt0.in");
    ofstream out("/Users/yanqiaozhan/Code/algorithmexercise/2015googlecodejam/B/out1");
    //  ifstream in("A-small-attempt3.in");
    // ofstream out("out");
    //in>>T;
    in>>T;
    for(int i=0;i<T;i++)
    {
        int D;
        in>>D;
        int m=0,temp;
        for(int j=0;j<D;j++)
        {
            in>>temp;
            if(temp>m)
                m=temp;
        }

        out<<"Case #"<<i+1<<": "<<ceil(sqrt(m)/sqrt(2))+1<<endl;


    }
    return 0;
}
*/
#include <cstdio>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <iostream>
using namespace std ;
int a[1200] ;
int main() {
    int t , step = 0 ;
    int n , i , j , max1=1000 , min1 , sum ;
    ifstream in("/Users/yanqiaozhan/Code/algorithmexercise/2015googlecodejam/B/B-large.in");
    ofstream out("/Users/yanqiaozhan/Code/algorithmexercise/2015googlecodejam/B/out1");
//    scanf("%d", &t) ;
    in>>t;
    while( t-- ) {
//        scanf("%d", &n) ;
        in>>n;
        for(i = 0 ; i < n ; i++) {
//            scanf("%d", &a[i]) ;
            in>>a[i];
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
        //printf("Case #%d: %d\n", ++step, min1) ;
//        cout<<"Case #"<<, ++step, min1)
        out<<"Case #"<<++step<<": "<<min1<<endl;
    }
    return 0 ;
}
