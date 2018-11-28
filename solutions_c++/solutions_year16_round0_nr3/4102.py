/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   xCase.h
 * Author: marlex
 *
 * Created on April 9, 2016, 3:14 AM
 */

#include<string>
#include<vector>

using namespace std;

#ifndef XCASE_H
#define XCASE_H

class xCase 
{
public:
        xCase(int caseIndex, int N, int J);
        ~xCase();
        
        void solveCase();
            int checkBase(int base, vector<int> bitString);
        
        bool hasFoundAllJamCoins();
        
        int caseIndex;
        int N;
        int J;
        int numFoundCoins;
        vector<vector<int> > bigBitStrings;
        vector<vector<int> > bigFactors;
        
};

#endif /* XCASE_H */

