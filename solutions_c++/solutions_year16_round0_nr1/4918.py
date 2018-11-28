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
        xCase(int caseIndex, int bleatrixNumber);
        ~xCase();
        
        void solveCase();
            void addToSeenDigits();
                vector<int> extractDigits();
            bool haveSeenAllDigits();    
        
        int myBleatrixNumber;
        int lastNamedNumber;
        int index;
        int caseIndex;
        vector<bool> seenDigits;
        string lastNumber;
};

#endif /* XCASE_H */

