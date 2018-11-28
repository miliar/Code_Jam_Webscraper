#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <fstream>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin;
    fin.open("F:/A-small-attempt0.in");
    ofstream fout;
    fout.open("F:/output1.txt");

    int T;
    //fin >> T;
    fin >> T;
    for (int i = 0; i < T; ++i){
        int smax;
        fin >> smax;
        char shylevel[1001];
        fin >> shylevel;
        int friends = 0;
        int current = 0;
        for (int j = 0; j <= smax; ++j){
            if (shylevel[j]=='0'){
                if (current==0)
                    friends++;
                else
                    current--;
            }
            else
                current += shylevel[j]-'0' - 1;
        }
        fout << "Case #"<<i+1<<": "<<friends << endl;

    }
    fin.close();
   fout.close();

    return 0;
}