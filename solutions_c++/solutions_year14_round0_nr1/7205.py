#include <iostream>
#include <cmath>
#include <string.h>
#include <vector>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int g;
        scanf("%d", &g);
        vector<int> dat;
        for(int j=1; j<=4; j++) {
            for(int k=1; k<=4; k++) {
                int d;
                scanf("%d", &d);
                if(j==g) {
                    dat.push_back(d);
                }
            }
        } 
        int g2;
        vector<int> dat2;
        scanf("%d", &g2);
        for(int j=1; j<=4; j++) {
            for(int k=1; k<=4; k++) {
                int d;
                scanf("%d", &d);
                if(j==g2) {
                    dat2.push_back(d);
                }
            }
        }
        int c = 0;
        int res;
        for(int p=0; p<4; p++) {
            int v1 = dat[p];
            for(int q=0; q<4; q++) {
                int v2 = dat2[q];
                if(v1 == v2) {
                    c++;
                    res = v1;
                }
            }
        }
        if(c==1) {
            cout << "Case #" << i+1 << ": " << res << endl;
        } else if(c==0) {
            cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
        } else {
            cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
        }
    }
}
