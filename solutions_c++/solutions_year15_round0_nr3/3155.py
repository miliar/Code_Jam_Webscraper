//
//  main.cpp
//  probA
//
//  Created by Bong-Jin Lee on 2015. 4. 10..
//  Copyright (c) 2015년 Bong-Jin Lee. All rights reserved.
//

#include <stdio.h>

#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>

using namespace std;



const int convtable[5][5] = {
    {0, 0, 0, 0, 0}
    ,{0, 1, 2, 3, 4}
    ,{0, 2, -1, 4, -3}
    ,{0, 3, -4, -1, 2}
    ,{0, 4, 3, -2, -1}
};


int calc(int r, int c) {
    int retval = convtable[abs(r)][abs(c)];
    
    if(r*c < 0) {
        retval *= -1;
    }
    
    return retval;
}

int convChar(const char c)
{
    switch(c) {
        case 'i':
            return 2;
        case 'j':
            return 3;
        case 'k':
            return 4;
    }
    return 0;
}



int main(int argc, const char * argv[]) {
    
    char inputname[1000] = "/Users/lbjcom/Downloads/C-small-attempt4.in.txt";
//        char inputname[1000] = "/Users/lbjcom/Downloads/in.txt";
    
    
    char outputname[1000] = "/Users/lbjcom/Downloads/_OUT.txt";
    FILE *fp = fopen(inputname, "r");
    
    FILE *fpout = fopen(outputname, "w");
    
    int number_of_tests = 0;
    
    int num_chars = 0;
    long long repeat = 0;
    char text[20000];
    
    // 먼저 테스트 갯수를 읽는다.
    fscanf(fp, "%d", &number_of_tests);
    
    for(int i = 0; i < number_of_tests; i++) {
        
        fscanf(fp, "%d", &num_chars);
        fscanf(fp, "%lld", &repeat);
        
        fscanf(fp, "%s", text);
        
        string s = text;
        
        int value = 1;
        
        int found = 0;
        
        int goal = 2;
        
        int k = 0;
        int iter = 0;
        
        while(1) {
            
            value = calc(value, convChar(s[k]));
            
            if(abs(value) == goal) {
                
                if((goal == 4) && (value >= 0)) {
                    // found k
                    found = 1;
                } else if((goal == 3) || (goal == 2)) {
                    // found 'ij'
                    goal++;
                    
                    if(value < 0) {
                        value = -1;
                    } else {
                        value = 1;
                    }
                }
                
            } else {
                found = 0;
            }
            
            k++;
            if(k >= s.size()) {
                iter++;
                k = 0;
                if(iter >= repeat) {
                    break;
                }
            }
            
            
            
        }
        
        if(found == 1) {
            fprintf(fpout, "Case #%d: YES\n", i+1);
        } else {
            fprintf(fpout, "Case #%d: NO\n", i+1);
        }
        
        
    } //for(int i = 0; i < number_of_tests; i++) {
    
    fclose(fpout);
    fclose(fp);
    
}























