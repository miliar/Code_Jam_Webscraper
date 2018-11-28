/*Santiago Zubieta*/
#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>

using namespace std;

int resolvePancakes(int pancakeDistribution[], int maxPancake, int dishes) {
    int finalCost = 1<<30;
    for(int limit = 1; limit <= maxPancake; limit++) {
        int cost = 0;
        for(int j = 0; j < dishes; j++) {
            int pancakeValue = pancakeDistribution[j];
            cost += pancakeValue / limit;
            if(pancakeValue % limit == 0) {
                cost--;
            }
        }
        cost += limit;
        finalCost = min(finalCost, cost);
    }
    return finalCost;
}


int main() {
    int T;
    scanf("%d", &T);
    for(int z = 0; z < T; z++){
        int dishes;
        cin >> dishes;
        // Read the initial amount of dishes that have pancakes on them.
        int pancakeDistribution[dishes];
        // Store the value of pancakes in dishes in so that the dish with the
        // biggest number of pancakes always remains on top.
        int maxPancake = 0;
        for(int k = 0; k < dishes; k++) {
        // Read the amount of pancakes on each of the given dishes, and then
        // push it to the priority queue.
            int pancakeNumber;
            cin >> pancakeNumber;
            pancakeDistribution[k] = pancakeNumber;
            maxPancake = max(pancakeNumber, maxPancake);
        }
        int minutes = 0;
        // Initialize the current amount of elapsed minutes at 0.
        minutes = resolvePancakes(pancakeDistribution, maxPancake, dishes);
        printf("Case #%d: %d", z + 1, minutes);
        if(z + 1 < T){
            puts("");
        }
    }
}
/*
int topPancake = pancakeDistribution.top();
    // The amount of pancakes in the dish with the most pancakes available.
    if(topPancake <= 3) {
    // If the top value is less than three, definitely splitting will have
    // no effect on the time, and if there are more than one with the same
    // value, then splitting will make it even worse.
        return minutes + topPancake;
    }
    else {
        pancakeDistribution.pop();
        int half = topPancake / 2;
        int mod  = topPancake % 2;
        pancakeDistribution.push(half);
        pancakeDistribution.push(half + mod);
    }
    int splittingMinutes = resolvePancakes(minutes + 1, pancakeDistribution);
    //printf("Eating straight from here on takes %d minutes for a total of %d\n", topPancake, topPancake + minutes);
    //printf("Splitting the top value of pancakes %d gives a total of %d\n", topPancake, splittingMinutes);
    //printf("Choose the lesser time!\n");
    //puts("");
    return min(minutes + topPancake, splittingMinutes);
*/