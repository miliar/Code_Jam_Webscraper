//
//  main.cpp
//  standing_ovation
//
//  Created by Sebastian Coronado on 10/04/15.
//  Copyright (c) 2015 Sebastian Coronado. All rights reserved.
//

#include <iostream>
using namespace std;

int countbetweenindexes(int a, int b, string & array, int l);
int main(int argc, const char * argv[]) {
    int testCases;
    int maxShyness;
    int standingPeople = 0;
    int result = 0;
    int pivot = 0;
    string shynessLevels;
    cin >> testCases;
    
    for (int testCase = 0; testCase < testCases; testCase++) {
        
        cin >> maxShyness;
        cin >> shynessLevels;
        standingPeople = 0;
        result = 0;
        pivot = 0;
        for (int shynessI = 0;shynessI<=maxShyness; shynessI++) {
            
            int currentPeopleWithShynessI = shynessLevels[shynessI] - '0';
            
           
            
            if (standingPeople >= maxShyness) {
                break;
            }
            
//            if (standingPeople == 0 && shynessI == 0 && currentPeopleWithShynessI == 0) {
//                result++;
//            }
            
            if (standingPeople < shynessI && currentPeopleWithShynessI>0) {
                result += shynessI-standingPeople;
                standingPeople += result;
            }
            
            standingPeople += currentPeopleWithShynessI;
        }
        printf("Case #%d: %d\n", testCase+1,result);
    }
}
