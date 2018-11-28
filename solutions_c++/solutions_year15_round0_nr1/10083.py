#include <iostream>
#include <cstdio>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

int main () {
    ofstream myfile;
    myfile.open ("/Users/johnvelez/Desktop/A-small-3.out");
    
    int cases, sum;
    char audience[1010];
    scanf("%d", &cases);
    
    int amount, invitations;
    for (int i = 1; i <= cases; ++i) {
        sum = invitations = 0;
        scanf("%d %s", &amount, audience);
        
        int length = (int)strlen(audience);
        sum += audience[0]-'0';
        
        for (int j = 1; j < length; ++j) {
            //Audience doe not exceed sum
            if(audience[j] != '0') {
                if(j <= sum) {
                    //Audience will stand up. Add them
                    sum += audience[j]-'0';
                }
                else {
                    //Invite the difference. Add it and audience
                    invitations += j-sum;
                    sum += invitations + audience[j] - '0';
                }
            }
        }
        
        myfile << "Case #" << i << ": " << invitations << "\n" << endl;
    }
    
    myfile.close();
    
    return 0;
}