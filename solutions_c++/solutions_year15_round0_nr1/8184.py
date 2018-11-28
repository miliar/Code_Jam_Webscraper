//
//  standingOvation.cpp
//  
//
//  Created by Roy, Sudeshna on 11/04/15.
//
//

#include <stdio.h>
#include <iostream>
#include <string>

int main(){
    int t;
    scanf(" %d ", &t);
    for (int i = 1; i <= t; i++){
        int smax;
        scanf(" %d ", &smax);
        std::string str;
        std::getline (std::cin,str);
        int totalStanding = str.at(0)-'0';
        long long int invited = 0;
        for (int j = 1; j <= smax; j++) {
            int s = str.at(j) - '0';
            int x = s > 0?j - (totalStanding + invited):0;
            invited += x>0?x:0;
            totalStanding += s;
        }
        printf("Case #%d: %lld\n", i, invited);
    }
}