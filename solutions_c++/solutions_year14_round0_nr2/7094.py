//
//  main.cpp
//  codejam
//
//  Created by Alexandru Grigoroi on 12/04/2014.
//  Copyright (c) 2014 Alexandru Grigoroi. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

double c, f, x;

double s(int k) {
    double res = 0;
    for (int i=0; i<k; i++)
        res += c/(2+f*i);
    return res + x/(2+f*k);
}

int main(int argc, const char * argv[])
{
    int t;
    cin>>t;
    cout<<setprecision(15);
    int k;
    for(int qw =1;qw<=t;qw++) {
        cin>>c>>f>>x;
        if(x>c)
            k = floor(x/c - 1 - 2/f) + 1;
        else
            k=0;
        if(k<0)
            k=0;
        cout<<"Case #"<<qw<<": "<<s(k)<<'\n';
    }
}

