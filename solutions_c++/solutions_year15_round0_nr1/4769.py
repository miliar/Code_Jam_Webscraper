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

int countFriends(int s_max, char *s_in_string)
{
    int invited = 0;
    int total_count = 0;
    
    for(int i = 0; i <= s_max; i++) {
        char tt[2] = "0";
        memcpy(tt, &s_in_string[i], 1);
        int si = atoi(tt);
        
        total_count += si;
        
        if(total_count > (i)) {
            continue;
        } else {
            invited += (i+1) - total_count;
            total_count += ((i+1) - total_count);
        }
    }
    
    return invited;
}

int main(int argc, const char * argv[]) {
    
//    char inputname[1000] = "/Users/lbjcom/Downloads/A-small-attempt1.in.txt";
    char inputname[1000] = "/Users/lbjcom/Downloads/A-large.in.txt";
//    char inputname[1000] = "/Users/lbjcom/Downloads/in.txt";
    char outputname[1000] = "/Users/lbjcom/Downloads/A-large-practice.out.txt";
    FILE *fp = fopen(inputname, "r");
    
    FILE *fpout = fopen(outputname, "w");
    
    int number_of_tests = 0;
    
    int s_max = 0;
    
    char s_in_string[10000] = "";
    
    // 먼저 테스트 갯수를 읽는다.
    fscanf(fp, "%d", &number_of_tests);
    
    for(int i = 0; i < number_of_tests; i++) {
    
        fscanf(fp, "%d", &s_max);
        fscanf(fp, "%s", s_in_string);
        
        int answer = countFriends(s_max, s_in_string);
        fprintf(fpout, "Case #%d: %d\n", i+1, answer);
        
    
    } //for(int i = 0; i < number_of_tests; i++) {
    
    fclose(fpout);
    fclose(fp);
    
}
