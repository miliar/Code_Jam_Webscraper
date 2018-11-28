//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on 24/03/14.
//  Copyright (c) 2014 Alexandre Decuq. All rights reserved.
//

//#include "main.h"

#include <vector>
#include <set>
#include <map> //set_intersection()
#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <cassert>
#include <iomanip> //for setprecision()
#include <cmath> //ceil() or floor()

using namespace std; //std::to_string(int)

int A, B;

int main()
{
    freopen("/Users/decuqa/Desktop/GoogleJam/GoogleJam/A-small-attempt1.in", "r", stdin);
	freopen("/Users/decuqa/Desktop/GoogleJam/GoogleJam/A-small-attempt1.out", "w", stdout);
    int T;
    cin>> T;
    
    for(int t=1; t<=T; t++)
    {
        char tmp;
        cin >> A >> tmp >> B;
        if (B%2!=0)
            cout<<"Case #"<<t<<": impossible"<<endl;
        else {
            int test=2, cpt=0;
            while(B!=test&&cpt<40) {
                test*=2;
                ++cpt;
            }
            if(cpt>=40) {
                cout<<"Case #"<<t<<": impossible"<<endl;
            }
            else {
                while(A%2==0&&B%2==0) {
                    A=A/2;
                    B=B/2;
                    cout<<"no small here"<<endl;
                }
                int res=1;
                while ( A*2<B) {
                    A*=2;
                    ++res;
                }
                if(res<=40)
                    cout<<"Case #"<<t<<": "<<res<<endl;
                else
                    cout<<"Case #"<<t<<": impossible"<<endl;
            }
        }
    }
}


