#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <fstream>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    int file = 1;
    ifstream fin;
    fin.open("F:/B-large.in");
    ofstream fout;
    fout.open("F:/output1.txt");

    int T;
    if (file)fin >> T;
    else
        cin >> T;
    for (int i = 0; i < T; ++i){
        int plant;
        if (file)fin >> plant;
        else cin >> plant;
        
        vector<int> cake(plant+1,0);
        int minute = 0;
        for (int j = 0; j < plant; ++j){
            if (file) fin >> cake[j];
            else cin >> cake[j];
        }
        sort(cake.begin(),cake.end());
        int current = 0;

        int minSub = cake[plant];
        
       

        for (int k = ceil(sqrt(cake[plant])); k <= cake[plant]; ++k){
            current = 0;
            for (int j = plant; j > 0; --j){
                if (cake[j] <= k){
                    //current = minSub;
                    break;
                }
                current += (cake[j]+k-1)/ k  -1;
            }
            minSub = min(minSub, current + k);
        }
        if (file)
        fout << "Case #" << i + 1 << ": " << minSub << endl;
        else
            cout << "Case #" << i + 1 << ": " << minSub << endl;
    }
    fin.close();
    fout.close();

    return 0;
}

