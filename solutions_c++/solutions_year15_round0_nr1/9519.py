//
//  main.cpp
//  CJ2015_Opera
//
//  Created by CCA on 4/11/15.
//  Copyright (c) 2015 cca. All rights reserved.
//

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include "stdio.h"

using namespace std;

int computeMinFriends(vector<int>& people);

int main (){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int qq = 1; qq <= tt; qq++) {
        printf("Case #%d: ", qq);
        fflush(stdout);
        int maxShyness;
        scanf("%d", &maxShyness);
//        printf("\n maxShyness = %d\n", maxShyness);
        // create vector w/ D elements
        char personsWithShyness;
        vector<int>shyArray(maxShyness + 1);
        scanf("%c", &personsWithShyness);
        
//        splitNumber(shyArray, personsWithShyness);
        for (int i = 0; i < maxShyness + 1; i++) {
            scanf("%c", &personsWithShyness);
            shyArray[i] = personsWithShyness - (int)'0';
        }
        int friendsNeeded = computeMinFriends(shyArray);
        printf("%d\n", friendsNeeded);
        shyArray.clear();
        
//        printf("\n");
    }
    
    return 0;
}

int computeMinFriends(vector<int>& people) {
    int totalStanding = 0;
    int friendsNeeded = 0;
    
    for (int i = 0; i < people.size(); i++) {
        if (totalStanding < i) {
            friendsNeeded += i - totalStanding;
            totalStanding = i;
            totalStanding += people[i];
        } else {
            totalStanding += people[i];
        }
    }
    return friendsNeeded;
}

