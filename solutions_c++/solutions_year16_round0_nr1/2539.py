//
//  main.cpp
//  Google Code Jam
//
//  Created by xiaoxin ren on 4/8/16.
//  Copyright © 2016 xiaoxin ren. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
const string FILENAME = "A-large";

string caseTest(int id, int num){
    if (num==0) return "Case #"+to_string(id)+": INSOMNIA";
    if (num < 0) num = -num;
    int count = 0, num2 = 0;
    vector<bool> table(10, false);
    
    while (1) {
        num2 += num;
        int num3 = num2;
        while (num3 > 0) {
            if (!table[num3%10]) {table[num3%10] = true; count ++;}
            num3 /= 10;
        }
        if (count == 10) return "Case #" + to_string(id) + ": "+ to_string(num2);
    }
    return "Case #"+to_string(id)+": INSOMNIA";
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int n = 0;
    ifstream fin (FILENAME+ ".in");
    ofstream fout (FILENAME + ".out");
    
    if (fin.is_open()){
        fin >> n;
        int num = 0;
        for (int i = 0; i < n; i++) {
            fin >> num;
            // fout << num << '\n';
            fout << caseTest(i+1, num)<< '\n';
        }
        fin.close();
        fout.close();
    }
    return 0;
}
