//
//  main.cpp
//  CodaJam2014
//
//  Created by Beatka on 12.04.14.
//  Copyright (c) 2014 Beatka. All rights reserved.
//

#include <iostream>
#include <set>
#include <queue>
using namespace std;

void blocks()
{
    int n;
    set<double> war_k, d_war_n;
    priority_queue<double> war_n, d_war_k;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++) {
        double a;
        scanf("%lf", &a);
        war_n.push(-a);
        d_war_n.insert(a);
    }
    for (int i = 0; i < n; i ++) {
        double a;
        scanf("%lf", &a);
        war_k.insert(a);
        d_war_k.push(-a);
    }
    //war
    int naomi_w = n;
    while (!war_k.empty()) {
        double top_n = -war_n.top(); //smallest
        set<double>::iterator top_k = war_k.upper_bound(top_n);
        if (top_k == war_k.end()) {
            break;
        }
        if (*top_k > top_n) {
            naomi_w --;
        }
        else break;
        war_k.erase(top_k), war_n.pop();
    }
    //printf("naomi war: %d\n", naomi_w);
    
    //d_war
    int ken_dw = 0;
    while (!d_war_n.empty()) {
        double top_k = -d_war_k.top(); //smallest
        set<double>::iterator top_n = d_war_n.upper_bound(top_k);
        if (top_n == d_war_n.end()) {
            break;
        }
        if (*top_n > top_k) {
            ken_dw ++;
        }
        else break;
        d_war_n.erase(top_n), d_war_k.pop();
    }
    //printf("naomi d_war: %d\n", ken_dw);
    
    printf("%d %d\n", ken_dw, naomi_w);

}

void magician() {
    
    int row1[4], row2[4];
    int num1, num2;
    scanf("%d", &num1);
    for (int i = 1;i <= 4; i++) {
        int a;
        for (int j = 0;j < 4; j++) {
            scanf("%d", &a);
            if (i == num1) {
                row1[j] = a;
            }
        }
    }
    
    scanf("%d", &num2);
    for (int i = 1;i <= 4; i++) {
        int a;
        for (int j = 0;j < 4; j++) {
            scanf("%d", &a);
            if (i == num2) {
                row2[j] = a;
            }
        }
    }
    int answer = 0;
    int cnt = 0;
    for (int i = 0;i < 4; i++)
        for (int j = 0;j < 4; j++) {//printf("(%d, %d) ", row1[j], row2[j]);
            if (row1[i] == row2[j]) {
                answer = row1[i];
                cnt ++;
            }
        }
    switch (cnt) {
        case 0:
            printf("Volunteer cheated!");
            break;
        case 1:
            printf("%d", answer);
            break;
        default:
            printf("Bad magician!");
            break;
    }
    printf("\n");
}

void cookies() {
    double c,f,x;
    scanf("%lf %lf %lf", &c, &f, &x);
    double cps = 2.0;
    double totalTime = 0;
    while (true) {
        double timeToWin = x/cps;
        double timeToFarm = c/cps;
        double nextTimeToWin = timeToFarm + x/(cps + f);
        //printf("ttw: %lf, ttf: %lf, nttw: %lf cpd: %lf\n", timeToWin, timeToFarm, nextTimeToWin, cps);
        if (timeToWin <= nextTimeToWin) {
            printf("%.7lf\n", totalTime + timeToWin);
            return;
        }
        cps += f;
        totalTime += timeToFarm;
    }
}
int main(int argc, const char * argv[])
{
    int t; scanf("%d", &t);
    for (int test = 1; test <= t; test++) {
        printf("Case #%d: ", test);
        //magician();
        //cookies();
        blocks();
    }
    return 0;
}

