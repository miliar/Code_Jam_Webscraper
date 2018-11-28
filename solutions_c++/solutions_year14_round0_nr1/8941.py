//
//  main.cpp
//  MagicTricks
//
//  Created by xanxus on 14-4-12.
//  Copyright (c) 2014年 xanxus. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <set>
using namespace std;

int main(int argc, const char * argv[])
{

    // insert code here...
    FILE* inputFile=fopen(argv[1], "r");
    int testCount=0;
    fscanf(inputFile,"%d",&testCount);
    string* testCase=new string[testCount];
    for (int i=0; i<testCount; i++) {
        int firstarrange[16],secondarrange[16];
        int firstrow,secondrow;
        fscanf(inputFile,"%d",&firstrow);
        for (int j=0; j<4; j++) {
            fscanf(inputFile,"%d %d %d %d",&firstarrange[j*4],&firstarrange[j*4+1],&firstarrange[j*4+2],&firstarrange[j*4+3]);
        }
        fscanf(inputFile,"%d",&secondrow);
        for (int j=0; j<4; j++) {
            fscanf(inputFile,"%d %d %d %d",&secondarrange[j*4],&secondarrange[j*4+1],&secondarrange[j*4+2],&secondarrange[j*4+3]);
        }
        set<int>firstset;
        for (int j=0; j<4; j++) {
            firstset.insert(firstarrange[4*(firstrow-1)+j]);
        }
        int findCount=0,findNum=0;
        for (int j=0; j<4; j++) {
            int current=secondarrange[4*(secondrow-1)+j];
            set<int>::iterator myiterator=firstset.find(current);
            if (myiterator!=firstset.end()) {
                findCount++;
                findNum=*myiterator;
            }
        }
        char answer[100];
        switch (findCount) {
            case 0:
                sprintf(answer, "%s","Volunteer cheated!");
                break;
            case 1:
                sprintf(answer, "%d",findNum);
                break;
            default:
                sprintf(answer,"%s", "Bad magician!");
                break;
        }
        testCase[i]=answer;
    }
    fclose(inputFile);
    FILE* outputFile=fopen("./output", "w");
    for (int i=0; i<testCount; i++) {
        fprintf(outputFile,"Case #%d: %s\n",i+1,testCase[i].c_str());
    }
    fclose(outputFile);
    return 0;
}

