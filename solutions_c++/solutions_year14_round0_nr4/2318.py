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
#include <iomanip>
using namespace std;
double v1[1000], v2[1000];
int flag[1000];

int main()
{

    ifstream fin("input.txt");
    ofstream fout("output.txt");
	int t;
	fin >> t;
	while (t--) {
        int n;
        fin >> n;
      
        for (int i =0; i < n; i++) {
            fin >> v1[i];
        }
        for (int i =0; i < n; i++) {
            fin >> v2[i];
        }
        vector<double> w1, w2;
        for (int i = 0; i < n; i++) {
            w1.push_back(v1[i]);
        }
        for (int i = 0; i < n; i++) {
            w2.push_back(v2[i]);
        }
        sort(w1.begin(), w1.end());
        sort(w2.begin(), w2.end(),greater<double>());
        int count1=0, count2=0;
        
        for (int i = 0; i < n; i++) {
            flag[i] = 1;
        }

        for (int i = 0; i < n; i++) {
            int sen=0;
            for (int j = 0; j < n; j++) {
              if (w1[j] > w2[i] && flag[j]) {
                flag[j] = 0;
                count1++;
                sen = 1;
                break;
               }
            }
            if (sen == 0) {
                for (int j = 0; j < n; j++) {
                    if (flag[j]){
                        flag[j] = 0;
                        break;
                    }
                }

            }
        }
    
        for (int i = 0; i < n; i++) {
            flag[i] = 1;
        }
        sort(w2.begin(), w2.end());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (flag[j]&&(w2[j] > v1[i])) {
                    flag[j] = 0;
                    count2++;
                    break;
                }
            }
        }
        count2 = n -count2;
        

        
        static int id = 0;

            fout << "Case #"<< ++id<<": "<<count1<< " "<<count2<<endl;
    }
    
    return 0;
}

