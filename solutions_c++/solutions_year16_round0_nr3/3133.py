/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Alex
 *
 * Created on 2016年4月10日, 上午 12:35
 */

#include <cstdlib>
#include <string>
#include <map>
#include <vector>
#include <cstring>
#include <iostream>

using namespace std;

#if __COMPILE_SOLVING__
/*
 * 
 */
map<unsigned long long, vector<unsigned long long>> myMaps[19];

void readMap(string mapFilename) {
    FILE* mapFileFD = fopen(mapFilename.c_str(), "r");
    char buf[1024];

    int index = 0;
    while(fgets(buf, 1024, mapFileFD) != NULL) {
        char* pch;
        if(buf[0] == 'i') {
            pch = strtok (buf," ");
            pch = strtok (NULL, " ");
            pch = strtok (NULL, " ");
            index = strtol(pch, NULL, 10);
        }
        else {
            pch = strtok (buf," \n");
            unsigned long long key = strtoull(pch, NULL, 10);
            vector<unsigned long long>& tmpVector = myMaps[index - 2][key];
            while(pch = strtok (NULL, " \n")) {
                tmpVector.push_back(strtoull(pch, NULL, 10));
            }
        }
    }
}

void Solve() {
    int total;
    scanf("%d", &total);
    
    for(int i = 0; i < total; i++) {
        int N, J;
        scanf("%d %d", &N, &J);
        printf("Case #%d:\n", i+1);
        int j = 0;
        for(auto imap: myMaps[N - 2]) {
            cout << imap.first << " ";
            for(auto tmp: imap.second) {
                cout << tmp <<" ";
            }
            cout << endl;
            j++;
            if(j == J)
                break;
        }
    }

    return;
}

int main(int argc, char** argv) {
    readMap(argv[1]);
    Solve();

    return 0;
}
#endif

