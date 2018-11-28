//
//  main.cpp
//  CodeJam2016
//
//  Created by Young Seok Kim on 4/9/16.
//  Copyright © 2016 TonyKim. All rights reserved.
//

#include <iostream>
#include <string.h>
//#include "bigint.cpp"

using namespace std;


int T;


char originalString[1005];
char outputString[1005];


int outputStringindex = 0;
int stringLength = 0;

void initialize() {
    for (int k=0; k<1005; k++) {
        originalString[k]=0;
        outputString[k]=0;
    }
    stringLength = 0;
    outputStringindex = 0;
}


int main(int argc, const char * argv[]) {
    // insert code here...
    
    freopen("A-large.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d", &T);
    
    int t;
    for (t = 1; t<=T; t++) {
        initialize();
        scanf("%s", originalString);
        stringLength = (int) strlen(originalString);
        for (int i=0; i<stringLength; i++) {
            if (i==0) {
                outputString[0] = originalString[0];
                continue;
            }
            if (originalString[i] >= outputString[0]) { // append to the first
                char tempstr[1005];
                // init tempstr
                for (int j=0; j<1005; j++) {
                    tempstr[j] = 0;
                }
                tempstr[0] = originalString[i];
                strcat(tempstr, outputString);
                strcpy(outputString, tempstr);
            } else {
                outputString[i] = originalString[i]; // append to the last
            }
        }
        printf("Case #%d: %s\n", t, outputString);
    }
    
    
    
    
    return 0;
}
