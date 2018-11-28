//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on 24/03/14.
//  Copyright (c) 2014 Alexandre Decuq. All rights reserved.
//

#include "main.h"

#include <vector>
#include <set>
#include <map> ///set_intersection()
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <iostream>
#include <string>  ///memset
#include <cstring>
#include <cassert>
#include <iomanip> ///setprecision()
#include <cmath> ///ceil() or floor()
#include <climits> ///INT_MAX

using namespace std; ///std::to_string(int)

//check isPrime
int getJamDivisor(long long N) {
    if(N%2==0)
        return 2;
    for(int i=3;i<=sqrt(N);i+=2) {
        if(N%i==0)
            return i;
    }
    return 1;
}

void display(string jamcoin,vector<int> divisors) {
    cout << jamcoin<< " ";
    for(int i=0;i<divisors.size();++i)
        cout << divisors[i] << " ";
    cout << endl;
}

int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/C-small-attempt0.in", "r", stdin); //small-attempt2
    freopen("/home/alex/Projects/googlecodejam/C-small-attempt0.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow
    for(int t=1; t<=T; t++)
    {
        int J, N;
        cin >> N >> J;
        int cpt = 0;

        cout << "Case #"<<t<<": "<< endl;

        int i=1<<(N-1);
        while (i<(1<<N)) {
            //jamcoin property: end with 1
            if((i&1LL) == 0) {
                i++;
                continue;
            }

            bool aPrimeExists = false;
            vector<int> divisors;
            for(int p=2;p<=10;++p) {    //each base
                long long number = 0;
                for(int j=0;j<N;++j) {
                    if(i&(1<<j)) {
                        number += pow(p,j);
                    }
                }
                //
                int divisor = getJamDivisor(number);
                if(divisor == 1) {
                    //cout << number << " is prime"<<endl;
                    aPrimeExists = true;
                    break;
                } else {
                    //cout << number << " no prime"<<endl;
                    divisors.push_back(divisor);
                }
            }

            //save this number
            if(!aPrimeExists)  {
                string str = "";
                for(int j=0;j<N;++j) {
                    if(i&(1<<j))
                        str="1"+str;
                    else
                        str="0"+str;
                }
                display(str,divisors);
                cpt += 1;
            }
            if(cpt>=J)
                break;
            i++;
        }
    }
    /** END ALGORITHM */
}


