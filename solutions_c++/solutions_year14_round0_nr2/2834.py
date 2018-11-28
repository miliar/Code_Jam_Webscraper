//
//  main.cpp
//  GCJQB
//
//  Created by Ningchen Ying on 4/12/14.
//  Copyright (c) 2014 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdio>

using namespace std;

int main(int argc, const char * argv[])
{

    int T;
    double C,F,X;
    freopen("/Users/YNingC/Documents/CodeForces/GCJQB/GCJQB/B-large.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJQB/GCJQB/B-large.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>C>>F>>X;
        double opt=X*1.0/2.0;
        double my_t=0;
        double FF=0;
        while(my_t<opt){
            my_t+=C/(2+FF);
            double c_opt=my_t+X*1.0/(2+FF+F);
            FF+=(double)F;
            opt=min(opt,c_opt);
        }
        cout<<"Case #"<<cas<<": ";
        printf("%.7lf\n",opt);
    }
    return 0;
}

