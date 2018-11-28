//
//  main.cpp
//  google_Codjam_2016
//
//  Created by Sunghyo Chung on 4/9/16.
//  Copyright © 2016 Sunghyo Chung. All rights reserved.
//

#include <iostream>
using namespace std;
#define max 101

char checkarr[max];

void initarr() {
    for(int i = 0; i<max; i++)
        checkarr[i] = NULL;
}

void printarr() {
    for(int i = 0; i<max; i++)
        printf("%c", checkarr[i]);
    printf("\n");

}

int getsize() {
    
    int size = 0;
    for(int i = 0; i<max; i++)
        if(checkarr[i] > 0)
            size++;
        else
            break;
    
    return size;
}

bool donechecking() {
    
    int size = getsize();
    
    for(int i = 0; i<size; i++)
        if(checkarr[i] == '-')
            return false;
    
    return true;
}

void flip(int n) {
    
    char temp[max];
    //copy
    for(int i = 0; i<max; i++)
        temp[i] = checkarr[i];
    
    for(int i = 0; i<=n; i++) {
        
        if(temp[i] == '+')
            temp[i] = '-';
        else if (temp[i] == '-')
            temp[i] = '+';
    }
    
    for(int i = 0; i<=n; i++)
        checkarr[i] = temp[n-i];
    
}

int findrightmost() {
    
    for(int i = getsize()-1; i>=0; i--)
        if(checkarr[i] == '-')
            return i;
    
    return -1;
}

int findleftmost() {
    
    for(int i = 0; i<getsize(); i++)
        if(checkarr[i] == '-')
            return i;
    
    return -1;
}

int main() {
    
    int T;
    int test_case;
    freopen("B-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    scanf("%d", &T);
    
    for(test_case = 1; test_case <= T; ++test_case) {
        
        initarr();
        
//        setbuf(stdout, NULL);
        scanf("%s", checkarr);
        int index = 0;
//        printf("Case #%d: %s\n", test_case, checkarr);
        while(1) {
            
            int pivot = findrightmost();
            
            if(checkarr[0] == '+' && pivot != -1) {
                
                int leftpivot = findleftmost();
                
                flip(leftpivot-1);
//                printarr();
                index++;
                continue;
            }
            
            if(pivot != -1)
                flip(pivot);
            else
                break;
            
            index++;
//            printarr();
            
        }
        
        printf("Case #%d: %d\n", test_case, index);

    }
    
    return 0;
}