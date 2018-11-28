/*
 ID: nhatminh12369
 PROG: castle
 LANG: C++11
 */
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <math.h>
#include <stdlib.h>

using namespace std;

void resetFlag(int flag[10]) {
    for (int i=0;i<10;i++) {
        flag[i] = 0;
    }
}

bool checkFlag(int flag[10]) {
    for (int i=0;i<10;i++) {
        if (flag[i] == 0) return 0;
    }
    return 1;
}

void markFlag(long long a, int flag[10]) {
    string strA = to_string(a);
    for (int i=0;i<strA.size();i++) {
        flag[strA[i]-'0'] = 1;
    }
}

int main() {
    ifstream fin ("/Users/LeonardNguyen/Documents/projects/ios/usaco/A-large.in");
    int T;
    fin>>T;
    
    int flag[10];
    
    for (int i=0;i<T;i++) {
        long long N;
        fin >> N;
        bool foundFlag = 0;
        resetFlag(flag);
        for (int j=1;j<10000;j++) {
            markFlag(N*j,flag);
            if (checkFlag(flag)) {
                cout<<"Case #"<<(i+1)<<": "<<N*j<<endl;
                foundFlag = 1;
                break;
            }
        }
        if (!foundFlag) {
            cout<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
        }
    }
    
    fin.close();
    
    return 0;
}

