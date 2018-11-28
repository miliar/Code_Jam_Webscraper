//
//  main.cpp
//  Google Code Jam Qualification Round 1
//
//  Created by Chunjing Jia on 4/11/14.
//  Copyright (c) 2013 Chunjing Jia. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <set>
using namespace::std;

string oper(string str){
    string strRes = "";
    int i=0;
    while(i<str.size()){
        if(strRes.size()==0 || strRes[strRes.size()-1] != str[i]) {
            strRes = strRes + str[i];
        }
        i++;
    }
    return strRes;
}


int main(int argc, const char * argv[])
{
    int nums;
    ifstream myfile("/Users/cjjia/Documents/Work/Google Code Jam/Round1B/CloneGraph/input");
    myfile >> nums;
    for(int num=0; num<nums; num++){
        int lenWords;
        bool thisRes = true;
        string word = "";
        myfile >> lenWords;
        vector<string> words(lenWords, "");
        for(int i=0; i<lenWords; i++){
            myfile >> words[i];
            if (word == "") {
                word = oper(words[i]);
            }
            else if (word != oper(words[i])){
                thisRes = false;
                break;
            }
        }
              
        if(!thisRes) {
            cout << "Case #" << num+1 << ": Fegla Won" << endl;
        } else {
            vector<int> suml(lenWords, 0);
            vector<int> sumr(lenWords, 0);
            vector<int> lens(lenWords, 0);
            for(int i=0; i<lenWords; i++){
                lens[i] = int(words[i].size());
            }
            sort(lens.begin(), lens.end());
            for(int i=0; i<lenWords; i++){
                if(i==0) suml[i] = lens[i];
                else suml[i] = suml[i-1]+lens[i];
            }
            for(int i=lenWords-1; i>=0; i--){
                if(i==lenWords-1) sumr[i] = lens[i];
                else sumr[i] = sumr[i+1]+lens[i];
            }
            int res = INT_MAX;
            for(int i=0; i<lenWords-1; i++){
                int nminusm = 2*(i+1)-lenWords;
                if(nminusm > 0)
                    res = min(res, sumr[i+1]-suml[i]+nminusm*lens[i]);
                else
                    res = min(res, sumr[i+1]-suml[i]+nminusm*lens[i+1]);
                        
            }
            
            cout << "Case #" << num+1 << ": " << res << endl;
        }
        
    }
    
    return 0;
}

