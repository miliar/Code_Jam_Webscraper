//
//  main.cpp
//  CodeJam2016
//
//  Created by Ray Hwang on 4/30/16.
//  Copyright © 2016 Ray Hwang. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int countChars(char c, string s) {
    int count = 0;
    
    for (int i = 0; i < s.size(); i++)
        if (s[i] == c) count++;
    
    return count;
}
int main() {
    
    FILE *fin = freopen("/Users/rayhwang/Projects/CodeJam2016/CodeJam2016/CodeJam2016/A-large.in", "r", stdin);
    assert( fin != NULL );
    
    FILE *fout = freopen("/Users/rayhwang/Projects/CodeJam2016/CodeJam2016/CodeJam2016/A-large.out", "w", stdout);
    assert( fout != NULL );
    
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; t++){

        string str;
        cin >> str;
        
        int digits[10] = {0};
        
        // Find Z. if any found, remove E R O
        //
        int zCount = countChars('Z', str);
        
        for (int i=0; i<zCount; i++) {
            size_t found = str.find_first_of("Z");
            str.erase(found, 1);
            
            found = str.find_first_of("E");
            str.erase(found, 1);
            
            found = str.find_first_of("R");
            str.erase(found, 1);
            
            found = str.find_first_of("O");
            str.erase(found, 1);
            
            digits[0] += 1;
        }
        
        // Find X. if any found, remove S I
        //
        int xCount = countChars('X', str);
        
        for (int i=0; i<xCount; i++) {
            size_t found = str.find_first_of("S");
            str.erase(found, 1);
            
            found = str.find_first_of("I");
            str.erase(found, 1);
            
            found = str.find_first_of("X");
            str.erase(found, 1);
            
            digits[6] += 1;
        }
        
        // Find W. if any found. remove T O
        //
        int wCount = countChars('W', str);
        
        for (int i=0; i<wCount; i++) {
            size_t found = str.find_first_of("T");
            str.erase(found, 1);
            
            found = str.find_first_of("W");
            str.erase(found, 1);
            
            found = str.find_first_of("O");
            str.erase(found, 1);

            digits[2] += 1;
        }
        
        
        // FIND G. if any found. remove E I H T
        //
        int gCount = countChars('G', str);
        
        for (int i=0; i<gCount; i++) {
            size_t found = str.find_first_of("E");
            str.erase(found, 1);
            
            found = str.find_first_of("I");
            str.erase(found, 1);
            
            found = str.find_first_of("G");
            str.erase(found, 1);
            
            found = str.find_first_of("H");
            str.erase(found, 1);
            
            found = str.find_first_of("T");
            str.erase(found, 1);

            digits[8] += 1;
        }
        
        
        // Find U. if any found. remove F O R
        //
        int uCount = countChars('U', str);
        
        for (int i=0; i<uCount; i++) {
            size_t found = str.find_first_of("F");
            str.erase(found, 1);
            
            found = str.find_first_of("O");
            str.erase(found, 1);
            
            found = str.find_first_of("U");
            str.erase(found, 1);
            
            found = str.find_first_of("R");
            str.erase(found, 1);
            
            digits[4] += 1;
        }
        
        // Find O. if any found. remove N E
        //
        int oCount = countChars('O', str);
        
        for (int i=0; i<oCount; i++) {
            size_t found = str.find_first_of("O");
            str.erase(found, 1);
            
            found = str.find_first_of("N");
            str.erase(found, 1);
            
            found = str.find_first_of("E");
            str.erase(found, 1);
            
            digits[1] += 1;
        }
        
        // Find R. if any found. remove T H E E
        //
        int rCount = countChars('R', str);
        
        for (int i=0; i<rCount; i++) {
            size_t found = str.find_first_of("T");
            str.erase(found, 1);
            
            found = str.find_first_of("H");
            str.erase(found, 1);
            
            found = str.find_first_of("R");
            str.erase(found, 1);
            
            found = str.find_first_of("E");
            str.erase(found, 1);
            
            found = str.find_first_of("E");
            str.erase(found, 1);
            
            digits[3] += 1;
        }
        
        // Find F. if any found. remove I V E
        //
        int fCount = countChars('F', str);
        
        for (int i=0; i<fCount; i++) {
            size_t found = str.find_first_of("F");
            str.erase(found, 1);
            
            found = str.find_first_of("I");
            str.erase(found, 1);
            
            found = str.find_first_of("V");
            str.erase(found, 1);
            
            found = str.find_first_of("E");
            str.erase(found, 1);
            
            digits[5] += 1;
        }
        
        // Find V. if any found. remove S E E N
        //
        int vCount = countChars('V', str);
        
        for (int i=0; i<vCount; i++) {
            size_t found = str.find_first_of("S");
            str.erase(found, 1);
            
            found = str.find_first_of("E");
            str.erase(found, 1);
            
            found = str.find_first_of("V");
            str.erase(found, 1);
            
            found = str.find_first_of("E");
            str.erase(found, 1);
            
            found = str.find_first_of("N");
            str.erase(found, 1);
            
            digits[7] += 1;
        }
        
        // Find I. if any found. that's how many 9
        //
        int iCount = countChars('I', str);
        
        digits[9] = iCount;
        
        cout << "Case #" << t << ": ";
        
        for (int i=0; i<10; i++) {
            if (digits[i] > 0) {
                for (int j=0; j<digits[i]; j++) {
                    cout << i;
                }
            }
        }
        cout << endl;
    }
    return 0;
}

//SEVEN
//NINE

//O
//N 799
//E 79
//F
//U
//I 9
//V 7
//S 7
//X
//G
