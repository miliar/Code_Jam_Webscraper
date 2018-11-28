//
//  main.cpp
//  QR_A_Standing_2015
//
//  Created by Umair Sheikh on 4/11/15.
//  Copyright (c) 2015 Umair Sheikh. All rights reserved.
//


#include<algorithm>
#include<map>
#include<iomanip>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#include <fstream>
#include <stack>

using namespace std;

#define lld long long int

int main(int argc, const char * argv[]) {
    
    ifstream fin("file.in");
    ofstream fout("file.out");
    int tt;
    fin>>tt;
    int cNo = 0;
    while(tt--) {
        cNo ++;
        lld size;
        fin>>size;
        string data;
        fin>>data;
        lld bucket = 0;
        bucket +=  data[0] -'0';
        lld persons = 0;
        for(lld i=1; i< data.length(); i++) {
            lld next = data[i] -'0';
            if(i>(persons + bucket)) {
                persons+= (i-(persons+bucket));
            }
            bucket += next;
        }
        fout<<"Case #"<<cNo<<": "<<persons<<endl;
    }
    
    return 0;
}
