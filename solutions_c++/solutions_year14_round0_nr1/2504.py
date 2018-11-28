//
//  main.cpp
//  jam
//
//  Created by mac  on 14-4-12.
//  Copyright (c) 2014年 mac . All rights reserved.
//

#include <iostream>
#include "vector"
#include<fstream>
int first[4][4];
int second[4][4];
using namespace std;

void check (vector<int> v1, vector<int>v2, int *flag){
    for (int i =0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (v1[i] == v2[j]) {
                flag[i] = 1;
            }

        }
    }
}
int main()
{

    ifstream fin("input.txt");
    ofstream fout("output.txt");
	int t;
	fin >> t;
	while (t--) {
        int flag[4] = {0,0,0,0};
        int frow;
        fin >> frow;
        vector<int> v1;
        for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				fin >> first[i][j];
			}
		}
        for (int i = 0; i < 4; ++i) {
            v1.push_back(first[frow-1][i]);
        }
        int srow;
        fin >> srow;
        vector<int> v2;
        for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				fin >> second[i][j];
			}
		}
        for (int i = 0; i < 4; ++i) {
            v2.push_back(second[srow-1][i]);
        }
        check(v1, v2, flag);
        int count = 0;
        int which = 0;
        for (int i = 0; i < 4; i++) {
            
            if (flag[i] == 1) {
                count++;
                which = i;
            }
        }
        static int id = 0;

        if (count == 1) {
            fout << "Case #"<< ++id<<": "<< v1[which]<<endl;
        }
        else if (count == 0) {
            fout << "Case #"<< ++id<<": "<< "Volunteer cheated!"<<endl;

        }
        else
            fout << "Case #"<< ++id<<": "<< "Bad magician!"<<endl;

    }
    return 0;
}

