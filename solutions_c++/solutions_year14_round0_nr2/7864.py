//
//  main.cpp
//  cookie
//
//  Created by Jacob on 12/04/14.
//  Copyright (c) 2014 Jacob. All rights reserved.
//

#include <cstdio>

int main(int argc, const char * argv[])
{
    int cases;
    double c, f, x;
    
    scanf("%d", &cases);
    
    for (int i=0; i<cases; i++) {
        scanf("%lf %lf %lf", &c, &f, &x);
        
        double cookies = 0, time = 0, speed = 2;
        
        while (cookies < x) {
            if (x/speed < c/speed+x/(speed+f)) {
                printf("Case #%d: %lf\n", i+1, x/speed+time);
                break;
            }
            time += c/speed;
            speed += f;
        }
    }
    
    return 0;
}

