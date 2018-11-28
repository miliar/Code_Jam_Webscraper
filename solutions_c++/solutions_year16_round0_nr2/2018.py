/* 
 * File:   main.cpp
 * Author: juro
 *
 * Created on April 9, 2016, 11:55 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string.h>

using namespace std;

/*
 * 
 */
long long sort_top_sad(string pancakes, int n);
long long sort_top_happy(string pancakes, int n);

long long sort_top_sad(string pancakes, int n) {
    if (n == 0) return 0;
    return pancakes[n-1] == '-' ? sort_top_sad(pancakes, n-1) : (sort_top_happy(pancakes, n-1) + 1);
}

long long sort_top_happy(string pancakes, int n) {
    if (n == 0) return 0;
    return pancakes[n-1] == '+' ? sort_top_happy(pancakes, n-1) : (sort_top_sad(pancakes, n-1) + 1);
}

int main(int argc, char** argv) {
    
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        string pancakes;
        cin >> pancakes;
        printf("Case #%d: %lld\n", i+1, sort_top_happy(pancakes, pancakes.length()));
    }
    
    
    return 0;
}

