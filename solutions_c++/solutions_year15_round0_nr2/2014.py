/* 
 * File: main.cpp
 * Copyright © Jan Škoda
 */

#include <cstdlib>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <cmath>

using namespace std;

int solve(int tables, priority_queue<int>& P) {
    int min_time = P.top();
    //int old_max ;
    int time; //= P.top()+2;
    int specials = 0;
    do {
        //old_max = max;
        int top = P.top();
        time = top+specials;
        P.pop();
        specials++;
        if (time < min_time) {
            min_time = time;
        }
        P.push(top/2);
        P.push(top-top/2);
    } while (P.top()>2);
    time = P.top() + specials;
    if (time < min_time) {
        min_time = time;
    }
    return min_time;
}

int solve2(int tables, priority_queue<int>& P) {
    int min_time = P.top();
    for (int normal_minutes = P.top(); normal_minutes > 0; normal_minutes--) {
        int specials = 0;
        priority_queue<int> P2 (P);
        while (P2.size() > 0 && P2.top() > normal_minutes) {
            specials += ceil((double)P2.top() / normal_minutes)-1;
            P2.pop();
        }
        if (normal_minutes + specials < min_time)
            min_time = normal_minutes + specials;
    }
    return min_time;
}

int main(int argc, char** argv) {
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        int D;
        cin >> D;
        priority_queue<int> P; //maximums popped
        
        for (int j = 0; j < D; j++) {
            int Pi;
            cin >> Pi;
            P.push(Pi);
        }

        printf("Case #%d: %d\n",i,solve2(D,P));
        //cout << "Case #" << i << ": " << setw(7) << setprecision(7) << solve(C,F,X) << endl;
    }

    return 0;
}

