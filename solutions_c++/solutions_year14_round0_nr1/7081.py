#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <sys/time.h>
using namespace std;

int main() {
    int t_c;
    int tt = 1;
    int r1;
    int r2;
    int f;
    int c;
    int t=0;
    int a[16];
    int b[16];
    ofstream outputFile("output.txt");
    ifstream myfile("A-small-attempt1.in");
    string line;
    myfile >> line;
    t_c = atoi(line.c_str());
    while(tt<t_c+1) {
    myfile >> line;
    r1 = atoi(line.c_str());
    for (int i = 0; i<16;i++) {
        myfile >> line;

        c = atoi(line.c_str());
        a[i] = c;
    }
    myfile >> line;
    r2 = atoi(line.c_str());
    for (int i = 0; i<16;i++) {
        myfile >> line;
        c = atoi(line.c_str());
        b[i] = c;
    }
    if(r1 == r2) {
        int l = r1*4;
        for(int i =l-4; i<l;i++) {
            for(int m = l-4;m<l;m++) {
               if (a[i]==b[m]){
                t = t+1;
                f = a[i];
                }
            }
        }
    }
    if(r1 > r2) {
        int d = r1-r2;
        d=d*4;
        int l = (r2*4)-4;
        for(int i =l; i<l+4;i++) {
            for (int m = l+d; m<l+d+4;m++) {
               if (a[m]==b[i]){
                t = t+1;
                f = b[i];
                }
            }
        }
    }
        if(r2 > r1) {
        int d = r2-r1;
            d=d*4;
        int l = (r1*4)-4;
        for(int i =l; i<l+4;i++) {
            for (int m = l+d; m<l+d+4;m++) {
               if (b[m]==a[i]){
                t = t+1;
                f = a[i];
                }
            }
        }
    }
    if (t == 1) {
    outputFile << "Case #"<<tt << ": "  << f<<endl;
    }
    if (t>1) {
    outputFile << "Case #"<<tt << ": "  << "Bad magician!" << endl;
    }
    if (t==0) {
    outputFile << "Case #"<<tt << ": "  << "Volunteer cheated!"<<endl;
    }
    tt++;
    t=0;
    }
return 0;
}
