//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Ignas Kancleris on 2014-04-12.
//  Copyright (c) 2014 Ignas Kancleris. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{

    int t;
    scanf("%d",&t);
    
    for (int i = 0; i < t; i++) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        
        
        int factories = 0;
        double time0 = 0;
        double minimum = 1e100;
        
        while (time0 + x/(2+factories*f) < minimum) {
            minimum = time0 + x/(2+factories*f);
            time0 += c/(2+factories*f);
            factories++;
        }
        printf("Case #%d: %.20lf\n", i+1, minimum);
        
        
    }
    
    return 0;
}

