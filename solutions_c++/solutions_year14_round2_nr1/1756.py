//
//  main.cpp
//  Qualification Round
//
//  Created by Ha Young Park on 4/12/14.
//  Copyright (c) 2014 Ha Young Park. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <set>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char * argv[])
{
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("A-large.out");
    int T;
    fin >> T;
    for(int i = 1; i <= T; i++){
        int N;
        fin >> N;
        string* pS = new string[N];//vector<int>* pvCount = new vector<int>[N];
        int** ppCount = new int*[N];
        
        string::iterator it;
        for(int j = 0; j < N; j++){//vector<int> vCount;
            string temp, newString;
            fin >> temp;

            it = temp.begin();
            char curr = *it++;
            int nCount = 1;
            int x = 0;
            int* pCount = new int[100];
            while(it != temp.end()){
                if(curr == *it){
                    nCount++;
                    temp.erase(it);
                }
                else{
                    pCount[x++] = nCount;//vCount.push_back(nCount);
                    curr = *it;
                    nCount = 1;
                    it++;
                }
            }
            pCount[x++] = nCount;//vCount.push_back(nCount);
            pS[j] = temp;
            ppCount[j] = pCount;//pvCount[j] = vCount;
            /*fout << pS[j] << endl;
            for(int y = 0; y < x; y++)
                fout << ppCount[j][y] << " ";
            fout << endl;
            for(vector<int>::iterator k = pvCount[j].begin(); k != pvCount[j].end(); k++)
                fout << *k << " ";
            fout << endl;
            */
            
        }
        fout << "Case #" << i << ": ";
        bool fl = true;
        for(int z = 1; z < N; z++){
            if(pS[0] != pS[z]){
                fout << "Fegla Won";
                fl =false;
                break;
            }
        }
        
        if(fl){
            int acc = 0;
            for(int h = 0; h < pS[0].size(); h++){
                set<int> distance;
                for(int a = 0; a < N; a++){
                    int sum = 0;
                    for(int b = 0; b < N; b++)
                        sum += abs(ppCount[a][h] - ppCount[b][h]);
                    distance.insert(sum);
                }
                acc += *(distance.begin());
            }
            fout << acc;
        }
        fout << endl;
    }
    
    fout.close();
    fin.close();
    return 0;
}

