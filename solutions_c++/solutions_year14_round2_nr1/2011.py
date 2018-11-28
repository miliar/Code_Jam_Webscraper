//
//  main.cpp
//  repeat
//
//  Created by Beibin Li on 14-5-3.
//  Copyright (c) 2014年 Beibin. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;



int median(vector<int> &v)
{
    size_t n = v.size() / 2;
    sort(v.begin(), v.end());
    return v[n];
}

int one_case(int caseNum)
{

    int NUM;
    cin >> NUM;
    string curr;

    vector<vector <int> > v;
    v.resize(NUM);

    string s;

    for(int i=0; i<NUM; i++){
        cin >> curr;
        string x;
        x += curr[0];
        v[i].push_back(1);
        int count = 0;

        for(int j=1; j<curr.size(); j++){
            if(curr[j] == curr[j-1]){
                v[i][count]++;
            }else{
                x += curr[j];
                v[i].push_back(1);
                count++;
            }
        }

        if(i==0){
            s = x;
        }else{
            if(strcmp(s.c_str(), x.c_str())){ //not equal
                cout<<"Case #"<<caseNum+1<<": Fegla Won"<<endl;
                return 0;
            }
        }

    }

    int part = (int)s.size();
    int moves = 0;

    for(int i=0; i<part; i++){
        vector<int> temp;
        for(int j=0; j<NUM; j++){
            temp.push_back(v[j][i]);
        }
        int m = median(temp);
        for(int j=0; j<NUM; j++){
            moves += abs(v[j][i] - m);
        }

    }
    cout<<"Case #"<<caseNum+1<<": "<<moves<<endl;


    return 0;
}



int main(int argc, const char * argv[])
{


    //these two lines should be quoted out. Used for Xcode
    //    ifstream arq(getenv("try"));
    //    cin.rdbuf(arq.rdbuf());

    int numCase = 0;
    cin >> numCase;
    
    for(int i=0; i<numCase; i++){
        one_case(i);
    }
    
    
    return 0;
}