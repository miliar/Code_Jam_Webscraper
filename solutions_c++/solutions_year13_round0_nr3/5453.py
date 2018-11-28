/* 
 * File:   main.cpp
 * Author: kingGreed
 *
 * Created on 13 avril 2013, 01:26
 */

#include <cstdlib>
#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;

/*
 * 
 */
bool isPalindrome(int x) {
  if (x < 0) return false;
  int div = 1;
  while (x / div >= 10) {
    div *= 10;
  }        
  while (x != 0) {
    int l = x / div;
    int r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}

int main(int argc, char** argv) {
    int testCases, count;
    
    cin >> testCases;
    for (int i = 0; i < testCases; i++) {
        int superior, inferior;
        
        cin >> inferior;
        cin >> superior;
        count = 0;
        for (int j = inferior; j <= superior; j++) {
            if(isPalindrome(j) && sqrt(j) == floor(sqrt(j)) && isPalindrome(sqrt(j))) {
                count++;
            }
        }
        
        cout << "Case #" << (i+1) << ": " << count << endl;

    }

    
    return 0;
}

