//
//  main.cpp
//  CodaJam2014
//
//  Created by Beatka on 12.04.14.
//  Copyright (c) 2014 Beatka. All rights reserved.
//

#include <iostream>

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
        cookies();
    }
    return 0;
}

