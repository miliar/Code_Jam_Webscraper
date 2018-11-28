#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int t;
    scanf("%d", &t);
    ofstream myfile;
    myfile.open("example1.txt");
    for(int T=1; T<=t; T++) {
        int a, i, j;
        int m1[4][4];
        scanf("%d", &a);
        for(i=0; i<4; i++) 
                 for(j=0; j<4; j++)
                          scanf("%d", &m1[i][j]);
        int b;
        int m2[4][4];
        scanf("%d", &b);
        for(i=0; i<4; i++) 
                 for(j=0; j<4; j++)
                          scanf("%d", &m2[i][j]);
        int hash[17] = {0};
        for(i=0; i<4; i++) {
            hash[m1[a-1][i]]++;
        }
        for(i=0; i<4; i++) {
            hash[m2[b-1][i]]++;
        }
        int co = 0, ddd = 0;
        for(i=0; i<17; i++) {
                  if(hash[i] == 2) {
                             co++;
                             ddd = i;
                  }
        }
        if(co == 1) {
              myfile << "Case #" << T << ": "<< ddd << endl;
        }else if(co == 0) {
              myfile << "Case #" << T << ": "<< "Volunteer cheated!\n";
        }else {
              myfile << "Case #" << T << ": "<<"Bad magician!\n";      
        }
    }    
}
