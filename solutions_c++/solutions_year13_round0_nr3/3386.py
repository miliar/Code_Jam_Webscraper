//
//  main.cpp
//  fairAndSquare
//
//  Created by Nirbhai Singh on 13/04/13.
//  Copyright (c) 2013 Nirbhai Singh. All rights reserved.
//

#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <cmath>
using namespace std;
string IntToStr( int n )
{
    ostringstream result;
    result << n;
    return result.str();
}
int main(int argc, const char * argv[])
{
    int no_of_tcases;
    cin>>no_of_tcases;
    for (int i=0; i<no_of_tcases; i++) {
        int a,b,count=0;
        cin>>a>>b;
        for (int i=a; i<=b; i++) {
            string s = IntToStr(i);
            //            cout<<s;
            string scopy=s;
            //            cout<<scopy;
            reverse(scopy.begin(), scopy.end());
            //            cout<< "reversed"<<scopy;
            if (s==scopy) {
                double d_sqrt = sqrt(i);
                //                cout << "sqrt"<<d_sqrt;
                int i_sqrt = d_sqrt;
                if ( d_sqrt == i_sqrt ){
                    string sq =IntToStr(i_sqrt);
                    string sqcopy=sq;
                    reverse(sqcopy.begin(), sqcopy.end());
                    if (sq==sqcopy) {
                        count++;
                    }
                }
            }
        }
        cout <<"Case #"<<i+1<<": "<< count << endl;
    }
    //    cout << "Hello, World!\n";
    return 0;
}

