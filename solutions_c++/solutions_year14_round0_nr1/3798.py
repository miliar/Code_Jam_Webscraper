//
//  main.cpp
//  Verizon
//
//  Created by bcstyle on 14-2-26.
//  Copyright (c) 2014年 bcstyle. All rights reserved.
//

#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int numCases;
    scanf("%d\n", &numCases);
    for(int curCase = 1; curCase <= numCases; curCase++) {
        int firstAns, secondAns;
        int pot1[4], pot2[4];
        int temp;
        scanf("%d\n", &firstAns);
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++){
                scanf("%d", &temp);
                if(i == firstAns - 1) {
                    pot1[j] = temp;
                }
            }
        }
        scanf("%d\n", &secondAns);
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++){
                scanf("%d", &temp);
                if(i == secondAns - 1) {
                    pot2[j] = temp;
                }
            }
        }
        int matchcount = 0;
        int output = 0;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++){
                if(pot1[i] == pot2[j]) {
                    matchcount++;
                    output = pot1[i];
                }
            }
        }
        cout << "Case #" << curCase << ": ";
        if(matchcount == 1) cout << output << endl;
        else if(matchcount > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
}

